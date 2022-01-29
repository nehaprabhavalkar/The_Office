'''
----------------------------------------------
Project: The Office
File: graphs.py
Description:

    plots graph using plotly
  
-----------------------------------------------
'''

import pandas as pd
import re
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from utils import load_yaml_data, plot_indicator_chart


DATA_PATH = '../data/'


def plot_graph_1(df):
    michael_count = 0
    dwight_df = df[df['speaker']=='Dwight'].reset_index()

    for i in range(0,len(dwight_df)):
        find_michael = re.search('Michael',dwight_df['dialogue'][i])

        if type(find_michael)==re.Match:
            michael_count = michael_count + 1

    str = 'Number of times Dwight said \'MICHAEL\''
    fig = plot_indicator_chart(michael_count, str)

    return fig



def plot_graph_2(df):
    ang_df = df[df['speaker']=='Angela'].reset_index()

    cat_count = 0

    for i in range(0,len(ang_df)):
        x = re.search('Cats',ang_df['dialogue'][i])
        y = re.search('cats',ang_df['dialogue'][i])
        z = re.search('cat',ang_df['dialogue'][i])
        w = re.search('Cat',ang_df['dialogue'][i])

        if type(x)==re.Match:
            cat_count = cat_count + 1
        if type(y)==re.Match:
            cat_count = cat_count + 1
        if type(z)==re.Match:
            cat_count = cat_count + 1
        if type(w)==re.Match:
            cat_count = cat_count + 1

    str = 'Number of times Angela talks about her Cats'
    
    fig = plot_indicator_chart(cat_count, str)

    return fig


def plot_graph_3(df):
    andy_df = df[df['speaker']=='Andy'].reset_index()

    cornell_count = 0

    for i in range(0,len(andy_df)):
        x = re.search('Cornell',andy_df['dialogue'][i])
        y = re.search('cornell',andy_df['dialogue'][i])
        if type(x)==re.Match:
            cornell_count = cornell_count + 1
        if type(y)==re.Match:
            cornell_count = cornell_count + 1

    str = 'Number of times Andy mentions Cornell'

    fig = plot_indicator_chart(cornell_count, str)

    return fig 


def plot_graph_4(df):
    kelly_df = df[df['speaker']=='Kelly'].reset_index()

    ryan_count = 0

    for i in range(0,len(kelly_df)):
        x = re.search('Ryan',kelly_df['dialogue'][i])
        y = re.search('ryan',kelly_df['dialogue'][i])
        if type(x)==re.Match:
            ryan_count = ryan_count + 1
        if type(y)==re.Match:
            ryan_count = ryan_count + 1

    str = 'Number of times Kelly said \'Ryan\''

    fig = plot_indicator_chart(ryan_count, str)

    return fig


if __name__ == '__main__':

    data = load_yaml_data()

    imdb_file_name = data['imdb_file_name']
    dialogue_file_name = data['dialogue_file_name']

    df = pd.read_csv(DATA_PATH + dialogue_file_name)

    fig = plot_graph_1(df)

    fig = plot_graph_2(df)

    fig = plot_graph_3(df)

    fig = plot_graph_4(df)
