from tensorflow.keras.models import load_model
from transformers import AutoTokenizer
import numpy as np
from twitter.utils.logger import logger


def predict(data):
    
    try:
        logger.info("Model Preduction Initialzied")

        ml=load_model("resource/model.h5")

        logger.info("Recieved Data and Model")

        tokenizer=AutoTokenizer.from_pretrained("bert-base-uncased")

        logger.info("Tokenization Successful")

        tokens=tokenizer.tokenize(data)

        ids=tokenizer.convert_tokens_to_ids(tokens)

        ytest=ids

        logger.info("Predicting")
        while len(ytest)<110:
            ytest.append(0)

        logger.info("Prediction Successful")

        return np.argmax(ml.predict([ids]))

    except Exception as e:
        logger.critical(str(e))


preidctor=predict