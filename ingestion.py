"""
Data ingestion for Job-Salary-Analytics.
Loads and preprocesses BLS and ILO datasets.
"""

import os
import pandas as pd
from typing import Tuple, Optional

def load_bls_data(bls_path: str) -> pd.DataFrame:
    """Load BLS data from CSV or Parquet."""
    if bls_path.endswith('.csv'):
        df = pd.read_csv(bls_path)
    else:
        df = pd.read_parquet(bls_path)
    return df

def load_ilo_data(ilo_path: Optional[str] = None) -> Optional[pd.DataFrame]:
    """Load ILO Labor data if available."""
    if ilo_path and os.path.exists(ilo_path):
        if ilo_path.endswith('.csv'):
            df = pd.read_csv(ilo_path)
        else:
            df = pd.read_parquet(ilo_path)
        return df
    return None

def preprocess_bls(df: pd.DataFrame) -> pd.DataFrame:
    """Perform data cleaning, NA handling, standardize columns, etc."""
    # Example cleaning (customize as needed)
    df = df.dropna(subset=['Job Title', 'Salary', 'Region'])
    df['Job Title'] = df['Job Title'].str.strip().str.title()
    # Add more data cleaning as required
    return df

def get_data(bls_path: str, ilo_path: Optional[str] = None) -> Tuple[pd.DataFrame, Optional[pd.DataFrame]]:
    bls_df = load_bls_data(bls_path)
    bls_df = preprocess_bls(bls_df)
    ilo_df = load_ilo_data(ilo_path)
    return bls_df, ilo_df
