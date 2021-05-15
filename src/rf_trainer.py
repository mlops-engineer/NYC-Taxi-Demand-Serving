import os
from sklearn.ensemble import RandomForestRegressor
from utils import evaluation, root_path
import pickle


class Trainer:
    def __init__(self, config):
        self.save_folder = config['save_folder']
        self.project = config['project']
        self.jwt = os.path.join(root_path, config['jwt'])

    def train(self, x_train, y_train):
        rf_reg = RandomForestRegressor(n_estimators=10, n_jobs=-1)
        self.model = rf_reg.fit(x_train, y_train)
        pickle.dump(self.model, open(f"{self.save_folder}/models/rf_model", 'wb'))
        print("Model Save Success!")
        return self.model
