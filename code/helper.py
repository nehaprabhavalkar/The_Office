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


def plot_table(df, column_1, column_2, column_3, values, title_str):

    fig = go.Figure(data=[go.Table(header=dict(values=values,
                                          fill_color='blue',
                                          height=30),
                    cells=dict(values=[column_1, column_2, column_3],
                            height=30))
                    ])

    fig.update_layout(title_text=title_str, template='plotly_dark')


    return fig 