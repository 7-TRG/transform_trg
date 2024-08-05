import pandas as pd
from transform_trg.transform_trg import mer 
def test_mer():
    df = mer()
    assert isinstance(df,pd.DataFrame)
