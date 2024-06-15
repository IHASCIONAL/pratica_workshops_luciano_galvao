import pandas as pd
from typing import List

"""
Função para transformar uma lista de dataframes em um único dataframe
"""

def concatenate_dataframes(dataframe_list: List[pd.DataFrame])  -> pd.DataFrame:
    return pd.concat(dataframe_list, ignore_index=True)