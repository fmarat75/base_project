import pandas as pd
import numpy as np
import os

def get_df():

    df = pd.DataFrame({
        'first column': list(range(1, 11)),
        'second column': np.arange(10, 101, 10)
    })

    return df



def get_titanic():

    parent_dir = os.getcwd()
    filepath = os.path.join(parent_dir,'raw_data', "ML_Titanic_dataset.csv")
    titanic_df = pd.read_csv(filepath)

    return titanic_df
