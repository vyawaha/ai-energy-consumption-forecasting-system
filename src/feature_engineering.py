import pandas as pd


def create_features(df):
    df['hour'] = df['Datetime'].dt.hour
    df['day'] = df['Datetime'].dt.day
    df['month'] = df['Datetime'].dt.month
    df['day_of_week'] = df['Datetime'].dt.dayofweek

    df['lag_1'] = df['Energy'].shift(1)
    df['lag_24'] = df['Energy'].shift(24)

    df['rolling_mean_24'] = df['Energy'].rolling(window=24).mean()

    df = df.dropna()

    return df