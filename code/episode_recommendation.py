'''
----------------------------------------------
Project: The Office
File: episode_recommendation.py
Description:
    
    content based recommender module which
    recommends based on similar episode 
    description
    
-----------------------------------------------
'''

import pandas as pd
import numpy as np
import re
import nltk
#nltk.download('stopwords')
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings('ignore')
from utils import load_yaml_data

DATA_PATH = '../data/'

def filter_dataset(df):
    cols_list = ['sno', 'title' ,'description']
    df= df[cols_list]
    return df

def transform_data(df):
    stemmer = PorterStemmer()
    stop_words = stopwords.words('english')
    corpus = []

    for i in range(0,len(df)):

        about = re.sub('[^a-zA-Z]', ' ', df['description'][i])
        about = about.lower()
        about = about.split()

        about = [stemmer.stem(word) for word in about if not word in stop_words]
        about = ' '.join(about)

        corpus.append(about)

    return  corpus 

def compute_cos_sim_df(df, corpus):
    cv = CountVectorizer()
    X = cv.fit_transform(corpus)
    cos_sim = cosine_similarity(X, X)

    cos_sim_df = pd.DataFrame(data=cos_sim,columns=[df.title])

    return cos_sim_df

def show_recommendation(cos_sim_df, episode_name):
    for i in range(0,len(df)):
        if df.values[i][1] == episode_name:
            episode_index = df.values[i][0]

            sorted_data = cos_sim_df.iloc[episode_index].sort_values(ascending=False)
            sorted_df = pd.DataFrame(sorted_data)

            return sorted_df.iloc[1:4]

def display_top_3_episodes(result):
    episode_list = result.index.tolist()
    for episode in episode_list:
        print(episode[0])

if __name__ == '__main__':

    data = load_yaml_data()

    imdb_file_name = data['imdb_file_name']
    episode_name = data['episode_name']

    df = pd.read_csv(DATA_PATH + imdb_file_name)
    df = filter_dataset(df)

    corpus = transform_data(df)
    cos_sim_df = compute_cos_sim_df(df, corpus)

    output = show_recommendation(cos_sim_df, episode_name)

    display_top_3_episodes(output)