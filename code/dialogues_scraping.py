'''
----------------------------------------------
Project: The Office
File: dialogues_scraping.py
Description:
    
    scrapes data from officequotes website 
    and stores into a csv file
    
-----------------------------------------------
'''

import requests
from bs4 import BeautifulSoup 
import pandas as pd
import re
import math
from utils import load_yaml_data

DATA_PATH = '../data/'


def get_num_episodes(df):
    grouped_seasons = df.groupby(['season'], as_index=False).count()
    grouped_seasons = grouped_seasons[['season','title']]
    grouped_seasons.rename(columns={'title':'no'}, inplace=True)

    seasons = grouped_seasons['season'].tolist()
    nos = grouped_seasons['no'].tolist()

    return seasons , nos


def extract_transcripts(seasons, nos):
    min_season = min(seasons)
    max_season = max(seasons)

    for season in range(min_season, max_season+1):

        for episode in range(1,nos[season-1]+1):
            
            digits = int(math.log10(episode))+1
            if digits < 2:
                episode = format(episode, '02')

            url = "https://www.officequotes.net/no"+ str(season) + "-"+str(episode)+".php"
        
            response=requests.get(url)
            
            # if response.status_code == 200:
            #     print(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            
            quote_content =soup.find_all('div',{'class':"quote"})
            
            for quote in quote_content:
                b_tags = quote.find_all('b')
                
                for tag in b_tags:
                    dialogue = tag.next_sibling
                    speaker = tag.text

                    dialogue_list.append(dialogue)
                    speaker_list.append(speaker)
                    seasons_list.append(season)

        print("Data scraped for Season {}".format(season))

    return seasons_list, speaker_list, dialogue_list

               
def create_dataframe(seasons_list, speaker_list, dialogue_list, output_file_name):
    dataframe = pd.DataFrame()

    dataframe['season'] = seasons_list
    dataframe['speaker'] = speaker_list
    dataframe['dialogue'] = dialogue_list

    dataframe.to_csv(DATA_PATH + output_file_name, index=False)        

    print("DataFrame created successfully")


if __name__ == '__main__':

    data = load_yaml_data()

    imdb_file_name = data['imdb_file_name']
    dialogue_file_name = data['dialogue_file_name']

    speaker_list = []
    dialogue_list = []
    seasons_list = []

    df = pd.read_csv(DATA_PATH + imdb_file_name)

    seasons, nos = get_num_episodes(df)

    seasons_list, speaker_list, dialogue_list = extract_transcripts(seasons, nos)

    create_dataframe(seasons_list, speaker_list, dialogue_list, dialogue_file_name)


