import pymongo
import pyfiglet
import pandas  as pd
import numpy 
import os 
import sys
from dataclasses import dataclass
import tensorflow as tf
from twitter.utils.logger import logger

@dataclass
class DataIngestionConfig():
    
    TrainDataUrl="mmongodb+srv://pymongo:pymongo@cluster0.yksijnk.mongodb.net/"
    TrainDataPath="resource/train.csv"
    MongoDataBase="twitter"
    MongoCollection="twitter"

class DataIngestion():
     
     def __init__(self) -> None:
        self.config=DataIngestionConfig()

     def cursor_pymongo(self):
         
         try:
            logger.info("Py Mongo Initialized")
            client=pymongo.MongoClient(self.config.TrainDataUrl)
            
            db=client[self.config.MongoDataBase]
            collection=db[self.config.MongoCollection]

            self.cursor=collection

         
            logger.info("Cursor Recieved")
         
         except Exception as e:
         
             logger.critical(str(e))
      
     def fetch_data(self):
         
         try:
            logger.info("fetching data")
            cursor=self.cursor

            data=cursor.find({})

            collection=[]

            logger.info("Data Has Been Fetched")

            for document in data:
               collection.append(document)
            
            logger.info("Collection has been created")

            DataFrame=pd.DataFrame(collection)

            self.DataFrame=DataFrame

         except Exception as e:
             logger.critical(str(e))
   
     def save_csv(self):
         
         try:
         
            logger.info("saving csv")

            self.DataFrame.to_csv(self.config.TrainDataPath)

            logger.info("Data Ingestion Successful")
        
         except Exception as e:
          
             logger.critical(str(e))




data_ingestion=DataIngestion

