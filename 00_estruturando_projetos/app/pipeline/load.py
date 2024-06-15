import os

import pandas as pd


def load_excel(
    dataframe: pd.DataFrame, output_path: str, file_name: str
) -> str:
    """
    Receber um dataframe e salvar como excel

    args:
    dataframe (pd.DataFrame): dataframe a ser salvo como excel
    output_path (str): caminho do arquivo a ser salvo
    file_name (str): nome do arquivo a ser salvo

    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    dataframe.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return 'Arquivo salvo com sucesso'
