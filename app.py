from src.mlprojects.logger import logging
from src.mlprojects.exception import CustomException
from src.mlprojects.components.data_ingestion import DataIngestion
#from src.mlprojects.components.data_ingestion import DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)