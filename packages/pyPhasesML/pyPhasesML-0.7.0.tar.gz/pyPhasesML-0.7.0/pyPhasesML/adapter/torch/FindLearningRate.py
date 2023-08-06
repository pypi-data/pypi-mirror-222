import math
import numpy as np

import torch
from pyPhases import classLogger
from pyPhasesML.Model import ModelConfig
from pyPhasesML.adapter.torch.Callback import Callback


@classLogger
class FindLearningRate(Callback):
    def __init__(self, config: ModelConfig, minLR, maxLR, iterations=3) -> None:
        super().__init__(config)
        self.smoothing = 0.05
        self.findLearningRatePlotPath = self.getLogPath() + "/lrRangeTest.png"
        self.minLR = minLR
        self.maxLR = maxLR
        self.iterations = iterations

    def onTrainingStart(self, model, dataset):
        model.maxEpochs = self.iterations
        start_lr = self.minLR
        end_lr = self.maxLR

        def cyclical_lr(x):
            return math.exp(x * math.log(end_lr / start_lr) / (model.maxEpochs * len(dataset.trainingData)))

        model.batchScheduler = torch.optim.lr_scheduler.LambdaLR(model.optimizer, cyclical_lr)
        self.lr_find_loss = []
        self.lr_find_lr = []

    def onBatchEnd(self, model, batchIndex):
        lr_step = model.optimizer.state_dict()["param_groups"][0]["lr"]
        self.lr_find_lr.append(lr_step)

        # smooth the loss
        loss = model.runningStats["loss"]
        if batchIndex == 0 and model.epoch == 0:
            self.lr_find_loss.append(loss)
        else:
            loss = self.smoothing * loss + (1 - self.smoothing) * self.lr_find_loss[-1]
            self.lr_find_loss.append(loss)

    def onTrainingEnd(self, model):
        from matplotlib import pyplot as plt

        plt.ylabel("loss")
        plt.xlabel("Learning Rate")
        plt.xscale("log")
        plt.plot(self.lr_find_lr, self.lr_find_loss)
        plt.savefig(self.findLearningRatePlotPath)
        minLr = self.lr_find_lr[np.argmin(self.lr_find_loss)]
        print("Lowest Loss LR: %f" % minLr)
        print("Suggested LR range max bound: %f" % minLr)
        print("Graph save in: %s" % self.findLearningRatePlotPath)
        self.lr_find_lr = self.lr_find_lr
        self.lr_find_loss = self.lr_find_loss
