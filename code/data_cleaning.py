'''
----------------------------------------------
Project: The Office
File: data_cleaning.py
Description:
    
  performs the following functions:-
    - removal of extra white spaces
    - removal of irrelevant punctuations
    - converts date into proper format
    
-----------------------------------------------
'''

import re
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import numpy as np
from imdb_scraping import save_to_csv
from helper import load_yaml_data

DATA_PATH = '../data/'

def clean_imdb_dataset(df):
    for i in range(0,len(df)):
        df['title'][i] = re.sub('[^A-Za-z0-9]+', ' ', df['title'][i])
        df['title'][i] = df['title'][i].strip()
        
    for i in range(0,len(df)):
        df['description'][i] = df['description'][i].strip()
        
    pattern = r'\[.*?\]'
    for i in range(0,len(df)):
        df['views'][i] = re.sub(pattern, '', df['views'][i])

    pattern = r'\(.*?\)'
    for i in range(0,len(df)):
        df['dates'][i] = re.sub(pattern, '', df['dates'][i])
        df['dates'][i] = df['dates'][i].replace('\xa0',' ').strip()
        
    for i in range(0,len(df)):
        df['dates'][i] = datetime.strptime(df['dates'][i], '%B %d, %Y')
        df['dates'][i]=df['dates'][i].date()

    Index = np.arange(0,186)
    df['sno'] = Index
        
    df['views'] = pd.to_numeric(df['views'])
    
    df['title'] = df['title'].astype(str)
    
    print("Dataset cleaned successfully")
    
    return df


def clean_dialogues_dataset(df):
    for i in range(0,len(df)):
        df['speaker'][i] = df['speaker'][i].replace(':','')

    df = df.drop(df[df['speaker'].str.contains('Deleted Scene')].index)

    null_count = df.isnull().sum().any()

    if null_count == True:
        non_null_df = df.dropna()

    print("Dataset cleaned successfully")

    return non_null_df


if __name__ == '__main__':

    data = load_yaml_data()

    imdb_file_name = data['imdb_file_name']
    dialogue_file_name = data['dialogue_file_name']

    df = pd.read_csv(DATA_PATH + imdb_file_name)

    cleaned_df = clean_imdb_dataset(df)

    save_to_csv(cleaned_df, imdb_file_name)

    df = pd.read_csv(DATA_PATH + dialogue_file_name)

    cleaned_df = clean_dialogues_dataset(df)

    save_to_csv(cleaned_df, dialogue_file_name)