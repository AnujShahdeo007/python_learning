import requests
import pandas as pd

def fetch_api_data(url: str, params=None, headers=None) -> pd.DataFrame:
    """Fetch data from a public e-commerce API and return as DataFrame."""
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    # Example: flatten and convert to DataFrame
    if isinstance(data, dict) and 'results' in data:
        data = data['results']
    return pd.json_normalize(data)
