"""
Data ingestion for Job-Salary-Analytics.
Loads and preprocesses real BLS OEWS dataset.
"""
import os
import pandas as pd
from typing import Tuple, Optional

def load_bls_data(bls_path: str) -> pd.DataFrame:
    if bls_path.endswith('.csv'):
        df = pd.read_csv(bls_path, dtype=str)
    else:
        df = pd.read_parquet(bls_path)
    return df

def preprocess_bls(df: pd.DataFrame) -> pd.DataFrame:
    # Rename real BLS columns to app-friendly names
    df = df.rename(columns={
        'OCC_TITLE': 'Job Title',
        'AREA_TITLE': 'Region',
        'NAICS_TITLE': 'Industry',
        'A_MEAN': 'Salary'
    })
    # Keep only needed columns
    cols = ['Job Title', 'Region', 'Industry', 'Salary']
    df = df[[c for c in cols if c in df.columns]]
    # Convert salary to numeric, drop invalid
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    df = df.dropna(subset=['Salary', 'Job Title', 'Region'])
    df = df[df['Salary'] > 0]
    df['Job Title'] = df['Job Title'].str.strip().str.title()
    df['Region'] = df['Region'].str.strip().str.title()
    return df

def load_ilo_data(ilo_path: Optional[str] = None) -> Optional[pd.DataFrame]:
    if ilo_path and os.path.exists(ilo_path):
        return pd.read_csv(ilo_path)
    return None

def get_data(bls_path: str, ilo_path: Optional[str] = None) -> Tuple[pd.DataFrame, Optional[pd.DataFrame]]:
    bls_df = load_bls_data(bls_path)
    bls_df = preprocess_bls(bls_df)
    ilo_df = load_ilo_data(ilo_path)
    return bls_df, ilo_df
        
       
       
