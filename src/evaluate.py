from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np


def evaluate_models(y_test, predictions):
    xgb_pred = predictions['xgboost']

    mae = mean_absolute_error(y_test, xgb_pred)
    rmse = np.sqrt(mean_squared_error(y_test, xgb_pred))
    r2 = r2_score(y_test, xgb_pred)

    print(f"MAE: {mae}")
    print(f"RMSE: {rmse}")
    print(f"R2 Score: {r2}")

    with open('outputs/metrics.txt', 'w') as f:
        f.write(f"MAE: {mae}\n")
        f.write(f"RMSE: {rmse}\n")
        f.write(f"R2 Score: {r2}\n")