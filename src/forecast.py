import pandas as pd


def generate_forecast(model, df):
    future = df.tail(24).copy()

    features = [
        'hour',
        'day',
        'month',
        'day_of_week',
        'lag_1',
        'lag_24',
        'rolling_mean_24'
    ]

    predictions = model.predict(future[features])

    forecast_df = pd.DataFrame({
        'Forecast': predictions
    })

    forecast_df.to_csv('outputs/future_forecast.csv', index=False)

    print('Future forecast generated.')