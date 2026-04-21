"""
Data ingestion for Job-Salary-Analytics.
Loads and preprocesses BLS and ILO datasets.
If files don't exist, uses synthetic sample data.
"""

import os
import pandas as pd
import numpy as np
from typing import Tuple, Optional

def generate_sample_data(n: int = 200) -> pd.DataFrame:
    """Generate realistic sample labor data."""
    np.random.seed(42)
    job_titles = ['Data Scientist', 'Software Engineer', 'Nurse', 'Accountant', 'Project Manager', 'Teacher']
    regions = ['Northeast', 'Midwest', 'South', 'West']
    industries = ['Tech', 'Healthcare', 'Finance', 'Education', 'Business']
    years = [2023, 2024]

    data = {
        "Job Title": np.random.choice(job_titles, n),
        "Salary": np.random.normal(90000, 25000, n).clip(35000, 220000).round(-2),
        "Region": np.random.choice(regions, n),
        "Industry": np.random.choice(industries, n),
        "Experience Level": np.random.randint(0, 21, n),
        "Year": np.random.choice(years, n)
    }
    return pd.DataFrame(data)

def load_bls_data(bls_path: str) -> pd.DataFrame:
    """Load BLS data from disk; use synthetic data if file is missing."""
    if os.path.exists(bls_path):
        if bls_path.endswith('.csv'):
            df = pd.read_csv(bls_path)
        else:
            df = pd.read_parquet(bls_path)
    else:
        df = generate_sample_data()
    return df

def load_ilo_data(ilo_path: Optional[str] = None) -> Optional[pd.DataFrame]:
    """Load ILO Labor data if available; use synthetic if path is given but missing."""
    if ilo_path:
        if os.path.exists(ilo_path):
            if ilo_path.endswith('.csv'):
                df = pd.read_csv(ilo_path)
            else:
                df = pd.read_parquet(ilo_path)
            return df
        else:
            return generate_sample_data()
    return None

def preprocess_bls(df: pd.DataFrame) -> pd.DataFrame:
    """Perform data cleaning, NA handling, standardize columns, etc."""
    cols = ["Job Title", "Salary", "Region", "Industry", "Experience Level", "Year"]
    for col in cols:
        if col not in df.columns:
            df[col] = np.nan  # Ensure required columns exist
    df = df[cols]
    df = df.dropna(subset=['Job Title', 'Salary', 'Region'])
    df['Job Title'] = df['Job Title'].astype(str).str.strip().str.title()
    df['Industry'] = df['Industry'].astype(str).str.title()
    # Add more cleaning as needed
    return df

def get_data(bls_path: str, ilo_path: Optional[str] = None) -> Tuple[pd.DataFrame, Optional[pd.DataFrame]]:
    bls_df = load_bls_data(bls_path)
    bls_df = preprocess_bls(bls_df)
    ilo_df = load_ilo_data(ilo_path)
    if ilo_df is not None:
        ilo_df = preprocess_bls(ilo_df)
    return bls_df, ilo_df
   
