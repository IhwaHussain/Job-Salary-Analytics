"""
Job Salary Prediction Model using BLS + LinkedIn data.
Combines features from both sources for improved prediction.
"""

import pandas as pd
import numpy as np
from typing import Tuple
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

MODEL_PATH = "bls_li_salary_model.pkl"

def featurize(df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
    """
    Feature engineering for BLS+LinkedIn salary data.
    One-hot encode categorical, combine features.
    """
    feature_cols = ['Job Title', 'Region', 'Industry', 'Experience Level']
    for col in feature_cols:
        if col not in df.columns:
            df[col] = "Unknown"
    features = pd.get_dummies(df[feature_cols], drop_first=True)
    target = df.get('Salary', np.zeros(len(df)))
    return features.values, target.values

def train_model(df: pd.DataFrame, save_path: str = MODEL_PATH):
    """Train and save a Gradient Boosting model on BLS + LI data."""
    X, y = featurize(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, save_path)
    print(f"Model saved to {save_path}. Test score: {model.score(X_test, y_test):.2f}")

def load_model(model_path: str = MODEL_PATH):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file {model_path} not found.")
    return joblib.load(model_path)

def predict_salary(job_title: str, region: str, experience_level: float, industry: str, model=None) -> float:
    """
    Predict salary from combined features.
    """
    if model is None:
        model = load_model()
    df = pd.DataFrame([{
        'Job Title': job_title,
        'Region': region,
        'Experience Level': experience_level,
        'Industry': industry
    }])
    X, _ = featurize(df)
    pred = model.predict(X)[0]
    return pred
