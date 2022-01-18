import requests
from bs4 import BeautifulSoup 
import pandas as pd
import re
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime

DATA_PATH = '../data/'

def scrape_data():
    
    for season in range(1,10):
        wikiurl="https://en.wikipedia.org/wiki/The_Office_(American_season_{})".format(season)
       
        response=requests.get(wikiurl)
    
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            officetable=soup.find('table',{'class':"wikitable"})
        
            for table in officetable:
                rows = table.find_all('tr',{'class':"vevent"})
    
            for row in rows:
                cells = row.find('td',{'class':"summary"})
                titlelist.append(cells.text)
        
            rows = table.find_all('td', attrs={'style':'text-align:center'})
    
            for row in rows:
                other_list.append(row.text)
        
            desc = officetable.find_all('td',{'class':"description"})

            for row in desc:
                desc_list.append(row.text)
                season_list.append(season)
                
            print("Data scraped for Season {}".format(season))
                
        else:
            raise Exception("Cannot extract data")

def create_dataframe():
    sno = []
    director = []
    writer = []
    dates = []
    views = []

    for i in range(0,len(other_list),6):
        sno.append(other_list[i])
        director.append(other_list[i+1])
        writer.append(other_list[i+2])
        dates.append(other_list[i+3])
        views.append(other_list[i+5])
        
    dataframe = pd.DataFrame()

    dataframe['sno'] = sno
    dataframe['season'] = season_list
    dataframe['title']= titlelist
    dataframe['description']= desc_list
    dataframe['director'] = director
    dataframe['writer'] = writer
    dataframe['dates'] = dates
    dataframe['views'] = views
    
    print("DataFrame created successfully")
    
    return dataframe

def save_to_csv(df,filename):
    df.to_csv(DATA_PATH + filename,index=False)
    print("Data saved in the file {}".format(filename))

if __name__ == '__main__':

    titlelist = []
    other_list = []
    desc_list = []
    season_list = []

    file_name = 'office.csv'

    scrape_data()
    df = create_dataframe()
    save_to_csv(df,file_name)