from transformers import BertTokenizer
import pandas as pd 
from dataclasses import dataclass
import os 
import sys
from twitter.utils.logger import logger
import numpy 
import tensorflow as tf

@dataclass
class DataTransformationConfig():
    
    RawDataPath="resource/train.csv"
    TransformedDataPath="resource/transformed_data.csv"
    TokenizerModel="bert-base-uncased"


class DataTransformation():
    
    def __init__(self):
        self.config=DataTransformationConfig()
    
    def fetch_data(self): 

        try:
            logger.info("Fetching Data for Transformation")
            self.DataFrame=pd.read_csv(self.config.RawDataPath)
            logger.info("Data Read Successfully")
        except Exception as e:
            logger.critical(str(e))

    def data_wrangling(self):

        try:

            logger.info("Data Wrangling Initialized")
            
            x=self.DataFrame['text']
            
            self.text=[]

            for i in x:
                self.text.append(str(i))    


            self.sentiment=self.DataFrame['sentiment'].replace({
                "negative" :0 ,
                "neutral": 1, 
                "positive":2
            
            })

            logger.info("Data Wrangling successful")
        
        except Exception as e:
            logger.critical(str(e))

    def tokeize_data(self):
            
        try:
            logger.info("Preparing BERT Base Uncased Tokenizer")

            self.tokens=[]
            tokenizer=BertTokenizer.from_pretrained(self.config.TokenizerModel)

            logger.info("Transformer Model Successfully fetched")

            logger.info("Initializing Tokenization")


            for _ in self.text:
                
                i=tokenizer.tokenize(_)
                self.tokens.append(i)

            self.ids=[]

            for _ in self.tokens:
                i=tokenizer.convert_tokens_to_ids(_)
                self.ids.append(i)

            self.padded_ids=tf.keras.utils.pad_sequences(self.ids,padding='post')

            return self.padded_ids

            logger.info("Successfully Tokenized")
        
        except Exception as e:
            logger.critical(str(e))


    def save_csv(self):

        try:

            logger.info("saving transformed data")
            
            Transformed_Data=pd.concat(objs=[pd.DataFrame(self.padded_ids),self.sentiment],axis=1)

            Transformed_Data.to_csv(self.config.TransformedDataPath)

            logger.info("Successfully Saved Tranformed data")
        
        except Exception as e:
            logger.critical(str(e))





data_transformation=DataTransformation

        

    