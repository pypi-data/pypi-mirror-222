from pathlib import Path
import pickle
import signal

import torch
from pyPhases import classLogger
from pyPhasesML.Model import ModelConfig
from pyPhasesML.adapter.torch.Callback import Callback

@classLogger
class SystemCheckPoint(Callback):
    def __init__(self, config: ModelConfig) -> None:
        super().__init__(config)
        signal.signal(signal.SIGTERM, self.shutdown)
        self.shutdownRequest = False

    def shutdown(self, signum, frame):
        self.shutdownRequest = True
        self.logError("Shutdown requested received, waiting for the next checkpoint")

    def onTrainingStart(self, model, dataset):
        restorePath = self.getLogPath()

        if Path(f"{restorePath}.resumeModel").exists():
            self.logSuccess("Restore training")
            modelState = torch.load(f"{restorePath}.resumeModel")
            model.loadState(modelState)
            optimizerState = torch.load(f"{restorePath}.resumeOptimizer")
            model.optimizer.load_state_dict(optimizerState)

            if Path(f"{restorePath}/.resumeBatchScheduler").exists():
                batchSchedulerState = torch.load(f"{restorePath}.resumeBatchScheduler")
                model.batchScheduler.load_state_dict(batchSchedulerState)

            with open(f"{restorePath}.resumeAdapter", "rb") as f:
                adapterState = pickle.load(f)

            model.startEpoch = adapterState["epoch"]
            model.bestMetric = adapterState["bestMetric"]
            
            # delete all resume files
            Path(f"{restorePath}.resumeModel").unlink()
            Path(f"{restorePath}.resumeOptimizer").unlink()
            Path(f"{restorePath}.resumeBatchScheduler").unlink(missing_ok=True)
            Path(f"{restorePath}.resumeAdapter").unlink()

    def onValidationEnd(self, model, results, scorer):
        # If a checkpoint is reached and shutdown signal received, exit gracefully
        if self.shutdownRequest:
            restorePath = self.getLogPath()
            self.logSuccess("Shutdown ... Saving everything")
            torch.save(model.model.state_dict(), f"{restorePath}.resumeModel")
            torch.save(model.optimizer.state_dict(), f"{restorePath}.resumeOptimizer")
            if model.batchScheduler is not None:
                torch.save(model.batchScheduler.state_dict(), f"{restorePath}.resumeBatchScheduler")

            with open(f"{restorePath}.resumeAdapter", "wb") as f:
                pickle.dump({"epoch": model.epoch, "bestMetric": model.bestMetric}, f, protocol=pickle.HIGHEST_PROTOCOL)

            self.log("Shutdown")
            exit()
