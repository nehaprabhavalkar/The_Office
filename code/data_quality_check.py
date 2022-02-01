'''
----------------------------------------------
Project: The Office
File: data_quality_check.py
Description:
    
    performs the following checks:-
    - row count check
    - null values check
    
-----------------------------------------------
'''

import pandas as pd 
from helper import load_yaml_data

DATA_PATH = '../data/'

def dq_on_imdb(df):
    check_row_count(df)
    check_null_values(df)

def dq_on_dialogues(df):
    check_row_count(df)
    check_null_values(df) 

def check_row_count(df):
    if len(df) > 0:
        print("Row count check is successful")

    else:
        raise Exception("Row count check has failed")

def check_null_values(df):
    if df.isnull().values.any() == False:
        print("No null values found")

    else:
        raise Exception("There are null values in data")

if __name__ == '__main__':

    data = load_yaml_data()

    imdb_file_name = data['imdb_file_name']
    dialogue_file_name = data['dialogue_file_name']

    df = pd.read_csv(DATA_PATH + imdb_file_name)

    dq_on_imdb(df)

    df = pd.read_csv(DATA_PATH + dialogue_file_name)

    dq_on_dialogues(df)