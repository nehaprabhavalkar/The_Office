'''
----------------------------------------------
Project: The Office
File: graphs.py
Description:

    plots graph using plotly
  
-----------------------------------------------
'''

import re
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from helper import load_yaml_data, plot_indicator_chart, plot_bar_chart, plot_line_chart, plot_table


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


def plot_graph_5(df):
    season_group = df.groupby(['season'], as_index=False).count()
    season_group = season_group[['season','title']]

    no_eps_df = season_group.rename(columns={'title':'no_of_episodes'})

    x_column = 'season'
    y_column = 'no_of_episodes'
    graph_title = 'Number of episodes per Season'

    fig = plot_bar_chart(no_eps_df, x_column, y_column, graph_title)

    return fig 


def plot_graph_6(df):
    top_10_view = (df.sort_values(by=['views'],ascending=False)).iloc[:10,:]

    x_column = 'season'
    y_column = 'views'
    graph_title = 'Top 10 highest viewed episodes of all time'

    fig = plot_bar_chart(top_10_view, x_column, y_column, graph_title)

    return fig 


def plot_graph_7(df):
    views_per_season = pd.DataFrame(df.groupby(['season'])['views'].mean()).reset_index()

    x_column = 'season'
    y_column = 'views'
    graph_title = 'Views for each season'

    fig = plot_line_chart(views_per_season, x_column, y_column, graph_title)

    return fig 


def plot_graph_8(df):
    top_5_viewed_dirs = (df.sort_values(by=['views'],ascending=False)).iloc[:5,:]

    eps = top_5_viewed_dirs['title'].tolist()
    dirs = top_5_viewed_dirs['director'].tolist()
    season = top_5_viewed_dirs['season'].tolist()

    title_str = 'Names of directors who directed top 5 highest rated episodes'

    values = ['season','title','director']

    fig = plot_table(top_5_viewed_dirs, eps, dirs, season, values, title_str)

    return fig 



if __name__ == '__main__':

    data = load_yaml_data()

    imdb_file_name = data['imdb_file_name']
    dialogue_file_name = data['dialogue_file_name']

    imdb_df = pd.read_csv(DATA_PATH + imdb_file_name)

    dialogues_df = pd.read_csv(DATA_PATH + dialogue_file_name)

    fig = plot_graph_1(dialogues_df)

    fig = plot_graph_2(dialogues_df)

    fig = plot_graph_3(dialogues_df)

    fig = plot_graph_4(dialogues_df)

    fig = plot_graph_5(imdb_df)

    fig = plot_graph_6(imdb_df)

    fig = plot_graph_7(imdb_df)

    fig = plot_graph_8(imdb_df)
