from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.feature_engineering import create_features
from src.train_model import train_models
from src.evaluate import evaluate_models
from src.forecast import generate_forecast
from src.visualize import generate_visualizations

print("Loading dataset...")
df = load_data()

print("Preprocessing data...")
df = preprocess_data(df)

print("Creating advanced features...")
df = create_features(df)

print("Training models...")
models, X_test, y_test, predictions = train_models(df)

print("Evaluating models...")
evaluate_models(y_test, predictions)

print("Generating forecast...")
generate_forecast(models['xgboost'], df)

print("Generating visualizations...")
generate_visualizations(df, y_test, predictions)

print("Project execution completed successfully.")