import re
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import numpy as np
from scraping import save_to_csv

DATA_PATH = '../data/'

def clean_dataset(df):
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


if __name__ == '__main__':

    file_name = 'office.csv'

    df = pd.read_csv(DATA_PATH + file_name)

    cleaned_df = clean_dataset(df)

    save_to_csv(cleaned_df, file_name)