import pandas as pd
from typing import List

def transform_data(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    """Example transformation: concatenate and drop duplicates."""
    df = pd.concat(dfs, ignore_index=True)
    df = df.drop_duplicates()
    # Add more transformation logic as needed
    return df
