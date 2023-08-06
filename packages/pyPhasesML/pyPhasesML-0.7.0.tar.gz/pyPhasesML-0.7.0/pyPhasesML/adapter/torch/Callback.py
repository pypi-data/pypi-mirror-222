from pyPhasesML.Model import ModelConfig


class Callback:
    def __init__(self, config: ModelConfig) -> None:
        self.config = config

    def getLogPath(self):
        return f"{self.config.logPath}/"

    def trigger(self, event, *args, **kwargs):
        if event == "trainingStart":
            self.onTrainingStart(*args, **kwargs)
        elif event == "trainingEnd":
            self.onTrainingEnd(*args, **kwargs)
        elif event == "validationStart":
            self.onValidationStart(*args, **kwargs)
        elif event == "validationEnd":
            self.onValidationEnd(*args, **kwargs)
        elif event == "batchEnd":
            self.onBatchEnd(*args, **kwargs)

    def onTrainingStart(self, model, dataset):
        pass

    def onTrainingEnd(self, model):
        pass

    def onValidationStart(self, model, validationData):
        pass

    def onValidationEnd(self, model, results, scorer):
        pass

    def onBatchEnd(self, model, batchIndex):
        pass
