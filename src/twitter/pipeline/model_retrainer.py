from twitter.pipeline.data_ingestion import Ingest_Data
from twitter.pipeline.data_transformation import data_transform
from twitter.pipeline.model_trainer import model_train

Ingest_Data()
data_transform()
model_train()

