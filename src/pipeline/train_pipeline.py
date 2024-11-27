import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

def start_training_pipeline():
    try:
        # Data Ingestion
        logging.info("Starting the data ingestion process.")
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed.")
        
        # Data Transformation
        logging.info("Starting the data transformation process.")
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
            train_path=train_data_path, 
            test_path=test_data_path
        )
        logging.info(f"Data transformation completed. Preprocessor saved at: {preprocessor_path}")
        
        # Model Training
        logging.info("Starting the model training process.")
        model_trainer = ModelTrainer()
        model_path = model_trainer.initiate_model_trainer(
            train_array=train_arr,
            test_array=test_arr
        )
        logging.info(f"Model training completed. Model saved at: {model_path}")
    
    except Exception as e:
        logging.error("Error occurred during the training pipeline.")
        raise CustomException(e, sys)

if __name__ == "__main__":
    start_training_pipeline()
