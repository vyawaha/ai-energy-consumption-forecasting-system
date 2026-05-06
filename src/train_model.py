from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

from xgboost import XGBRegressor

import joblib


def train_models(df):

    features = [
        'hour',
        'day',
        'month',
        'day_of_week',
        'lag_1',
        'lag_24',
        'rolling_mean_24'
    ]

    X = df[features]

    y = df['Energy']

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Random Forest Model
    rf_model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    # XGBoost Model
    xgb_model = XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    )

    print("Training Random Forest...")
    rf_model.fit(X_train, y_train)

    print("Training XGBoost...")
    xgb_model.fit(X_train, y_train)

    # Predictions
    rf_predictions = rf_model.predict(X_test)

    xgb_predictions = xgb_model.predict(X_test)

    # Save models
    joblib.dump(
        rf_model,
        'models/random_forest_model.pkl'
    )

    joblib.dump(
        xgb_model,
        'models/xgboost_energy_model.pkl'
    )

    models = {
        'random_forest': rf_model,
        'xgboost': xgb_model
    }

    predictions = {
        'rf': rf_predictions,
        'xgboost': xgb_predictions
    }

    return models, X_test, y_test, predictions