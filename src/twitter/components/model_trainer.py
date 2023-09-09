import tensorflow as tf
from tensorflow.keras.layers import LSTM,Dense,Bidirectional,Embedding,Input
from transformers import AutoTokenizer
import pandas as pd
from dataclasses import dataclass
from twitter.utils.logger import logger



@dataclass
class ModelTrainerConfig():
    DataPath="resource/transformed_data.csv"
    TokenizerModel="bert-base-uncased"

class ModelTrainer():
    
    def __init__(self):
        self.config=ModelTrainerConfig()

    def fetch_data(self):
            
        try:
            logger.info("Fetching Data")
            
            DataFarme=pd.read_csv("resource/transformed_data.csv")
            
            self.y=DataFarme['sentiment'].values.tolist()      
            
            DataFarme.drop(['sentiment'],inplace=True,axis=1)
            self.x=DataFarme.values.tolist()

            print(tf.shape(self.x),tf.shape(self.y))

            logger.info("Data Has been read succcessfully")
        except Exception as e:
            logger.critical(str(e))


    def build_model(self):
            
        try:
            logger.info("Building Model")  
            ml=tf.keras.Sequential([
            
            Input(shape=(109,)),
            Embedding(input_dim=30000,output_dim=256,input_length=109,),

            Bidirectional(LSTM(256,return_sequences=True)),

            Bidirectional(LSTM(512)),

            tf.keras.layers.Flatten(),

            Dense(1024,activation='relu'),
            Dense(512,activation='relu'),
            Dense(256,activation='relu'),
            Dense(128,activation='relu'),
            Dense(3,activation='softmax'),      
            
        ])


            ml.compile(optimizer="adam",loss=tf.keras.losses.SparseCategoricalCrossentropy(),metrics=['accuracy'])
            self.ml=ml
            logger.info("Model Build Successful")
        except Exception as e:
            logger.critical(str(e))

    def train_model(self):
            
        try:
            logger.info("Model Training Initialized")
            ml=self.ml

            ml.fit(x=self.x,y=self.y)

            self.ml=ml
            logger.info("Model Training Successful")
        except Exception as e:
            logger.critical(str(e))

    def save_model(self):
            
        try:

            logger.info("Save Model")
            self.ml.save_model("resource/model.h5")
            logger.info("Model Saved Successfully")

        except Exception as e:
            
            logger.critical(str(e))




model_trainer=ModelTrainer
