from sklearn.preprocessing import LabelEncoder
from utils import split_train_and_test


def preprocess_df(df):
    zip_code_le = LabelEncoder()
    df['zip_code_le'] = zip_code_le.fit_transform(df['zip_code'])

    train_df, test_df = split_train_and_test(df, '2015-01-24')
    print('data split end')

    del train_df['zip_code']
    del train_df['pickup_hour']
    del test_df['zip_code']
    del test_df['pickup_hour']

    y_train_raw = train_df.pop('cnt')
    y_test_raw = test_df.pop('cnt')

    train_df = train_df.fillna(method='backfill')
    test_df = test_df.fillna(method='backfill')
    return train_df, y_train_raw, test_df, y_test_raw
