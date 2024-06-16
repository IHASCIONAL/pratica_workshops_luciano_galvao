"""Módulo de Execução do Pipeline."""

from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concatenate_dataframes

if __name__ == '__main__':
    dataframe_list = extract_from_excel('../data/input')
    dataframe = concatenate_dataframes(dataframe_list)
    load_excel(dataframe, '../data/output', 'output')
