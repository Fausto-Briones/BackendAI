import joblib
import sklearn
import os

class Model:
    def __init__(self):

        model_dir = os.path.dirname(os.path.realpath(__file__))
        model_path = os.path.join(model_dir, 'gbm_model.joblib')

        self.model = joblib.load(model_path)

    def predict(self, input_data):
        return self.model.predict(input_data)