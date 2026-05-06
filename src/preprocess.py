def preprocess_data(df):

    # Sort data
    df = df.sort_values('Datetime')

    # Fill missing values
    df = df.ffill()

    # Remove duplicates
    df = df.drop_duplicates()

    return df