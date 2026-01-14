import sys
import pandas as pd
from src.components.exception import CustomException
from src.logger import logging


class DataTransformation:
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("DataTransformation: loaded train and test data")
            # simple stub: return numpy arrays and a placeholder object
            return train_df.values, test_df.values, None
        except Exception as e:
            raise CustomException(e, sys)
