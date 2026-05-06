import matplotlib.pyplot as plt


def generate_visualizations(df, y_test, predictions):
    plt.figure(figsize=(15, 5))
    df['Energy'].plot()
    plt.title('Energy Consumption Trend')
    plt.savefig('images/energy_trend.png')

    plt.figure(figsize=(12, 5))
    plt.plot(y_test.values[:200], label='Actual')
    plt.plot(predictions['xgboost'][:200], label='Predicted')
    plt.legend()
    plt.title('Actual vs Predicted')
    plt.savefig('images/actual_vs_predicted.png')

    plt.figure(figsize=(12, 5))
    monthly = df.groupby('month')['Energy'].mean()
    monthly.plot(kind='bar')
    plt.title('Monthly Energy Consumption')
    plt.savefig('images/monthly_consumption.png')

    plt.figure(figsize=(15, 5))
    df['rolling_mean_24'].plot()
    plt.title('24 Hour Rolling Average')
    plt.savefig('images/rolling_average.png')