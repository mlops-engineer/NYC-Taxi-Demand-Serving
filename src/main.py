import argparse
import os
import pandas as pd
import rf_trainer
from base_data import base_query
from preprocess import preprocess_df
from nyc_taxi_prediction import NycTaxiPredictionRFService
from utils import init_config

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--dev_env", help="Development Env [local], [dev], [prod]", type=str,
                        default="local")

    flag = parser.parse_args()

    config = init_config(flag.dev_env)
    print(f"Config : {config}")
    model_dir = f"{config['save_folder']}/models/"

    print('load data')
    base_df = pd.read_gbq(query=base_query, dialect='standard', project_id=config['project'], auth_local_webserver=True)
    train_df, y_train_raw, test_df, y_test_raw = preprocess_df(base_df)

    x_train = train_df.copy()
    x_test = test_df.copy()

    if not os.path.isdir(model_dir):
        os.mkdir(model_dir)

    print('train start')
    train_op = rf_trainer.Trainer(config)
    model = train_op.train(x_train, y_train_raw)
    bento_service = NycTaxiPredictionRFService()
    bento_service.pack('model', model)
    saved_path = bento_service.save()
    print(f"Bento Service Save! : {saved_path}")
