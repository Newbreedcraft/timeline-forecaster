import pandas as pd
from datetime import datetime

def preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])
    df['actual_completion_date'] = pd.to_datetime(df['actual_completion_date'])
    df['duration'] = (df['actual_completion_date'] - df['start_date']).dt.days
    df = df.dropna(subset=['duration'])
    df.to_csv('data/processed/processed_data.csv', index=False)
    return df

if __name__ == "__main__":
    preprocess_data('data\\raw\\data.csv')
