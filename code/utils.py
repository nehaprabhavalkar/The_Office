'''
----------------------------------------------
Project: The Office
File: utils.py
Description:
    
    contains helper functions used frequently
    in other modueles
    
-----------------------------------------------
'''

import yaml
import plotly.graph_objects as go
import plotly.express as px

def load_yaml_data():
    with open('../conf/config.yml', 'r') as file:
        data = yaml.safe_load(file)

    return data


def plot_indicator_chart(value, title_str):

    fig = go.Figure(go.Indicator(
        mode = 'number',
        value = value,
        title = {'text': title_str}
    
    ))

    fig.update_layout(template='plotly_dark')

    return fig


def plot_bar_chart(df, x_column, y_column, graph_title):

    fig = px.bar(df,x=x_column,y=y_column, color_discrete_sequence=['green'])

    fig.update_layout(title_text=graph_title, template='plotly_dark')

    return fig 


def plot_line_chart(df, x_column, y_column, graph_title):
    
    fig = px.line(df, x=x_column, y=y_column)

    fig.update_layout(title_text=graph_title, template='plotly_dark')

    return fig 
