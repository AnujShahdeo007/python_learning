import os
import pandas as pd
from sqlalchemy import create_engine
from etl.extract import extract_from_csv, extract_from_json

def test_extract_from_csv():
    df = extract_from_csv(os.path.join(os.path.dirname(__file__), '../data/sample.csv'))
    assert isinstance(df, pd.DataFrame)

def test_extract_from_json():
    df = extract_from_json(os.path.join(os.path.dirname(__file__), '../data/sample.json'))
    assert isinstance(df, pd.DataFrame)
