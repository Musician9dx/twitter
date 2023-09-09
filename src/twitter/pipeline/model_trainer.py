from twitter.components.model_trainer import ModelTrainer


def train_model():
    obj=ModelTrainer()
    obj.fetch_data()
    obj.build_model()
    obj.train_model()
    obj.save_model()

model_train=train_model