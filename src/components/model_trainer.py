import sys
from src.components.exception import CustomException
from src.logger import logging


class ModelTrainer:
    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("ModelTrainer: starting (stub)")
            # stub: pretend we trained a model and return a message
            return "Model training completed (stub)"
        except Exception as e:
            raise CustomException(e, sys)
