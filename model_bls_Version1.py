"""
Job Salary Prediction Model using BLS data only.
Trains a scikit-learn regression model and exposes prediction functions.
"""

import pandas as pd
import numpy as np
from typing import Tuple
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

MODEL_PATH = "bls_salary_model.pkl"

def featurize(df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
    """
    Feature engineering for BLS salary data.
    Returns X (features) and y (target).
    """
    # Example: one-hot encode job title, region, etc.
    features = pd.get_dummies(df[['Job Title', 'Region']], drop_first=True)
    if 'Experience Level' in df.columns:
        features['Experience Level'] = df['Experience Level']
    target = df['Salary']
    return features.values, target.values

def train_model(df: pd.DataFrame, save_path: str = MODEL_PATH):
    """Train and save a Random Forest regression model."""
    X, y = featurize(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, save_path)
    print(f"Model saved to {save_path}. Test score: {model.score(X_test, y_test):.2f}")

def load_model(model_path: str = MODEL_PATH):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file {model_path} not found.")
    return joblib.load(model_path)

def predict_salary(job_title: str, region: str, experience_level: float, model=None) -> float:
    """
    Predict salary given job parameters. 
    """
    if model is None:
        model = load_model()
    # Create single-row dataframe for input
    df = pd.DataFrame([{
        'Job Title': job_title,
        'Region': region,
        'Experience Level': experience_level
    }])
    X, _ = featurize(df)
    pred = model.predict(X)[0]
    return pred