import pandas as pd
from app.pipeline.transform import concatenate_dataframes

df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3,4]})
df_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7,8]})

def testar_a_concatenacao_da_lista_de_dataframes():
    # arrange
    dataframe_list = [df_1, df_2]
    dataframe = pd.concat(dataframe_list, ignore_index=True)
     
    # act
    df = concatenate_dataframes([df_1, df_2])
    
    # assert
    assert df.shape == (4,2)
    assert dataframe.equals(df)
