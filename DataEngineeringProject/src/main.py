
import pandas as pd
from sqlalchemy import create_engine
import yaml
import os
from urllib.parse import quote_plus
from etl.extract import extract_from_mysql, extract_from_csv, extract_from_json
from etl.kaggle_ingest import load_kaggle_csv
from etl.api_ingest import fetch_api_data
from etl.transform import transform_data
from etl.load import load_to_mysql

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../config/db_config.yaml')
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data')

def safe_load_kaggle():
    kaggle_path = os.path.join(DATA_PATH, 'kaggle_ecommerce.csv')
    if os.path.exists(kaggle_path):
        return load_kaggle_csv(kaggle_path)
    else:
        print("[INFO] Kaggle dataset not found, skipping.")
        return pd.DataFrame()

def safe_fetch_api():
    try:
        return fetch_api_data('https://fakestoreapi.com/products')
    except Exception as e:
        print(f"[INFO] API fetch failed: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Load DB config
    with open(CONFIG_PATH, 'r') as f:
        config = yaml.safe_load(f)
    db_conf = config['mysql']
    password_encoded = quote_plus(str(db_conf['password']))
    engine = create_engine(
        f"mysql+mysqlconnector://{db_conf['user']}:{password_encoded}@{db_conf['host']}:{db_conf['port']}/{db_conf['database']}"
    )

    # Extract
    df_mysql = extract_from_mysql(engine, 'source_table')
    df_csv = extract_from_csv(os.path.join(DATA_PATH, 'input.csv'))
    df_json = extract_from_json(os.path.join(DATA_PATH, 'input.json'))
    df_kaggle = safe_load_kaggle()
    df_api = safe_fetch_api()

    # Transform (advanced)
    df_transformed = transform_data([
        df for df in [df_mysql, df_csv, df_json, df_kaggle, df_api] if not df.empty
    ])

    # Load
    load_to_mysql(engine, df_transformed, 'output_table')
    print("Advanced pipeline completed successfully.")
