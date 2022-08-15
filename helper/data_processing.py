# import the libraries
import numpy as np
import pandas as pd

def get_files(path):
    '''
        Get All records from the dataset
    '''
    return pd.read_csv(path);