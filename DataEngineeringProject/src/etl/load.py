import pandas as pd
from sqlalchemy.engine.base import Engine

def load_to_mysql(engine: Engine, df: pd.DataFrame, table_name: str):
    """Load DataFrame to a MySQL table."""
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
