import pandas as pd
from etl.transform import transform_data

def test_transform_data():
    df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    df2 = pd.DataFrame({'a': [2, 3], 'b': [4, 5]})
    result = transform_data([df1, df2])
    assert result.shape[0] == 3  # 2 + 2 rows minus 1 duplicate
