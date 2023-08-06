import os
import timeit
import psutil

import torch
from pyPhases import classLogger
from pyPhasesML.adapter.torch.Callback import Callback


@classLogger
class CheckPoint(Callback):

    def onTrainingStart(self, model, dataset):
        self.epochStartTime = timeit.default_timer()

    def onValidationStart(self, model, dataset):
        self.epochEndTime = timeit.default_timer()
        
    def prettyPrintConfusionMatrix(self, confusion_matrix):
        num_rows, num_cols = confusion_matrix.shape
        max_value_length = max(len(str(confusion_matrix.max())), len(str(confusion_matrix.min())))
        separator = "-" * ((max_value_length + 2) * num_cols)

        rows = []
        for i in range(num_rows):
            row_data = [f"{int(confusion_matrix[i, j]):>{max_value_length}}" for j in range(num_cols)]
            rows.append(" | ".join(row_data))

        print(separator)
        print("\n".join(rows))
        print(separator)

    def onValidationEnd(self, model, results, scorer):
        metricsValues = {m: results[m] for m in scorer.metrics}
        metricDiffStrings = []
        metricValuetrings = []
        improved = False
        modelId = "checkpointModel_%i_" % model.epoch

        metrics = model.validationMetrics
        metricDefinitions = {m: scorer.getMetricDefinition(m) for m in metrics}
        globalBestMetric = model.validationMetrics[0]

        metricStrings = []
        for metricName, metricVal in metricsValues.items():
            bestValue, useAsBest, biggerIsBetter = metricDefinitions[metricName]
            diff = metricVal - bestValue
            metricStrings.append(
                f"{metricName}: "
                + "{:.3f}".format(metricVal)
                + " [best: {:.3f}]".format(bestValue)
            )
            metricDiffStrings.append(f"{metricName}: " + "{:.3f}".format(diff))
            metricValuetrings.append("{:.3f}".format(metricVal))

            isBigger = metricVal > bestValue

            if (biggerIsBetter and isBigger) or (not biggerIsBetter and not isBigger):
                metricDefinitions[metricName][0] = metricVal
                if useAsBest:
                    improved = True
                    if metricName == globalBestMetric:
                        model.bestMetric = max(model.bestMetric, metricsValues[globalBestMetric])

        validationEndTime = timeit.default_timer()

        self.log(
            f"Validation-Epoch Number: {str(model.epoch)}  Training Time: {str(self.epochEndTime - self.epochStartTime)}  Validation Time: {str(validationEndTime - self.epochStartTime)}"
        )

        if "confusion" in scorer.results:
            self.prettyPrintConfusionMatrix(scorer.results["confusion"])

        trainingStats = " | ".join([f"{n}:{v}" for n, v in model.runningStats.items()])
        self.log(f"Training Stats: {trainingStats} ")
        self.log(" ".join(metricStrings))

        if improved:
            self.log("Model Improved: " + " ".join(metricDiffStrings))
            path = f"{self.getLogPath()}/{modelId}" + "_".join(metricValuetrings) + ".pkl"
            with open(path, "wb") as f:
                torch.save(model.model.state_dict(), f)
            notImprovedSince = 0
            self.bestModelPath = path
        else:
            notImprovedSince += 1
            self.log("Model not improving since %i epochs" % (notImprovedSince))

        if self.config.stopAfterNotImproving > 0 and notImprovedSince >= self.config.stopAfterNotImproving:
            model.fnished = True

        process = psutil.Process(os.getpid())
        self.log(f"memory usage: {process.memory_info().rss / 1024 / 1024}M")