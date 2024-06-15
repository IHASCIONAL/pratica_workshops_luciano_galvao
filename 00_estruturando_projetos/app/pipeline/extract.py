"""Módulo de Extração."""

import glob
import os
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Lê arquivos e retorna um dataframe

    args: input_path(str): caminho da pasta com os arquivos

    return: lista de dataframes

    """
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    dataframe_list = []

    for file in all_files:
        dataframe_list.append(pd.read_excel(file))

    return dataframe_list


if __name__ == '__main__':
    path = "../../data/input"
    dataframe_list = extract_from_excel(path)
    print(dataframe_list)
