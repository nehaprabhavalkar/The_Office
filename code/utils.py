import yaml
import plotly.graph_objects as go

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
