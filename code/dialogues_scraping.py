import requests
from bs4 import BeautifulSoup 
import pandas as pd
import re
import math

DATA_PATH = '../data/'

df = pd.read_csv(DATA_PATH+'office.csv')

g1 = df.groupby(['season'], as_index=False).count()
g1 = g1[['season','title']]
g1.rename(columns={'title':'no'}, inplace=True)

seasons = g1['season'].tolist()
nos = g1['no'].tolist()

s = []
d = []
seas = []
eps = []

for i in range(1,10):
    for j in range(1,nos[i-1]+1):
        eps.append(j)
        digits = int(math.log10(j))+1
        if digits < 2:
            j = format(j, '02')
        url = "https://www.officequotes.net/no"+ str(i) + "-"+str(j)+".php"
       
        response=requests.get(url)
        
        if response.status_code == 200:
            print(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        officetable=soup.find_all('div',{'class':"quote"})
        
        for k in officetable:
            bs = k.find_all('b')
            
            for ba in bs:
                d.append(ba.next_sibling)
                seas.append(i)
                s.append(ba.text)
                eps.append(j)
               
            
dataframe = pd.DataFrame()

dataframe['season'] = seas
dataframe['speaker']= s
dataframe['dialogue']= d

dataframe.to_csv(DATA_PATH + 'dialogues.csv',index=False)