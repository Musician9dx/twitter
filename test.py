import pandas as pd
import tensorflow as tf
import sklearn as sk
from transformers import AutoTokenizer
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import drive
from tensorflow.keras.layers import Dense, Embedding,Input,LSTM,Bidirectional


data=pd.read_csv("/content/drive/MyDrive/Data Sets/twittertrain.csv",delimiter=',',)

data.drop(['textID','selected_text'],inplace=True,axis=1)