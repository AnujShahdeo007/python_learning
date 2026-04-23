import pandas as pd
from sqlalchemy.engine.base import Engine

def extract_from_mysql(engine: Engine, table_name: str) -> pd.DataFrame:
    """Extract data from a MySQL table."""
    return pd.read_sql(f"SELECT * FROM {table_name}", engine)

def extract_from_csv(file_path: str) -> pd.DataFrame:
    """Extract data from a CSV file."""
    return pd.read_csv(file_path)

def extract_from_json(file_path: str) -> pd.DataFrame:
    """Extract data from a JSON file."""
    return pd.read_json(file_path)
