import os
import pandas as pd

def load_kaggle_csv(file_path: str) -> pd.DataFrame:
    """Load a large Kaggle CSV dataset."""
    return pd.read_csv(file_path)
