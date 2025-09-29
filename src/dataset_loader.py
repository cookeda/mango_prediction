import pandas as pd

def load_dataset(path:str='data/mango_data.csv'):
    df = pd.read_csv(path)
    X = df['length_cm']
    y = df['mango_type']
    return X, y
