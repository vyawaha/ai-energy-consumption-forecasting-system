import pandas as pd


def load_data():

    # Read CSV with comma separator
    df = pd.read_csv(
        'data/raw/energy_consumption.csv',
        sep=',',
        low_memory=False
    )

    print("Dataset Columns:")
    print(df.columns)

    # Create Datetime column
    df['Datetime'] = pd.to_datetime(
        df['Date'] + ' ' + df['Time'],
        format='%d/%m/%Y %H:%M:%S',
        errors='coerce'
    )

    # Convert energy column to numeric
    df['Global_active_power'] = pd.to_numeric(
        df['Global_active_power'],
        errors='coerce'
    )

    # Keep required columns
    df = df[['Datetime', 'Global_active_power']]

    # Rename column
    df.rename(
        columns={
            'Global_active_power': 'Energy'
        },
        inplace=True
    )

    # Remove missing values
    df.dropna(inplace=True)

    # Reduce dataset size for faster execution
    df = df.sample(50000, random_state=42)

    return df