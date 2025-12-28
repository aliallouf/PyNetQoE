import pandas as pd
import numpy as np

def preprocess_qoe_data(df):
    """Cleans the data and encodes categorical features."""
    # Group low frequency categories (OS and API levels)
    df = _group_low_freq(df, 'QoD_os-version')
    df = _group_low_freq(df, 'QoD_api-level')
    
    # One-Hot Encoding for Resolution
    if 'QoA_VLCresolution' in df.columns:
        df = pd.get_dummies(df, columns=['QoA_VLCresolution'], prefix='res', dtype=int)
    
    # Map and Encode Network Type
    qos_map = {1: 'EDGE', 2: 'UMTS', 3: 'HSPA', 4: 'HSPAP', 5: 'LTE'}
    if 'QoS_type' in df.columns:
        df['network'] = df['QoS_type'].map(qos_map)
        df = pd.get_dummies(df, columns=['network'], prefix='net', dtype=int)
    
    # Drop IDs and raw categorical columns
    cols_to_drop = ['id', 'user_id', 'QoS_type', 'QoS_operator']
    return df.drop(columns=[c for c in cols_to_drop if c in df.columns], errors='ignore')

def _group_low_freq(df, column, threshold=0.01):
    counts = df[column].value_counts()
    low_freq = counts[counts < (len(df) * threshold)].index
    df[f'{column}_grouped'] = df[column].replace(low_freq, 'Other')
    return pd.get_dummies(df, columns=[f'{column}_grouped'], dtype=int).drop(columns=[column])