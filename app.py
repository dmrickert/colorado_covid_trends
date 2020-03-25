#!/usr/bin/env python3

import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

#current_path = os.path.dirname(os.path.realpath(__file__))
#csv_path = os.path.join(current_path, '..', 'data', 'colorado_covid_data.csv')
csv_url = 'https://raw.githubusercontent.com/dmrickert/colorado_covid_trends/master/data/colorado_covid_data.csv'
df = pd.read_csv(csv_url, parse_dates=['Date'])

app = dash.Dash()
server = app.server

colors = {
    'background': '#F9F9F9',
    'text': '#000000'
}

'''
# Traces for bar graphs
trace_bar_tested = go.Bar(x=df['Date'], y=df['# Tested'], name="# tested")
trace_bar_confirmed = go.Bar(x=df['Date'], y=df['# Confirmed'], name="# confirmed")
trace_bar_hospitalized = go.Bar(x=df['Date'], y=df['# Hospitalized'], name="# hospitalized")
trace_bar_death = go.Bar(x=df['Date'], y=df['# Death'], name="# dead")
'''

# Our traces for our scatter plots
trace_scat_tested = go.Scatter(x=df['Date'], y=df['# Tested'], name="# tested")
trace_scat_confirmed = go.Scatter(x=df['Date'], y=df['# Confirmed'], name="# confirmed")
trace_scat_hospitalized = go.Scatter(x=df['Date'], y=df['# Hospitalized'], name="# hospitalized")
trace_scat_death = go.Scatter(x=df['Date'], y=df['# Death'], name="# dead")

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Colorado Covid Trends',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='This graph pulls from: https://github.com/dmrickert/colorado_covid_trends/blob/master/data/colorado_covid_data.csv', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Div(children='Original data from: https://covid19.colorado.gov/case-data', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.H2(
        children='# Tested',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(
        id='Graph_tested',
        figure={
            'data': [trace_scat_tested],
            'layout': {
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),
    html.H2(
        children='# Confirmed',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(
        id='Graph_confirmed',
        figure={
            'data': [trace_scat_confirmed],
            'layout': {
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),
    html.H2(
        children='# Hospitalized',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(
        id='Graph_hospitalized',
        figure={
            'data': [trace_scat_hospitalized],
            'layout': {
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),
    html.H2(
        children='# Dead',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(
        id='Graph_death',
        figure={
            'data': [trace_scat_death],
            'layout': {
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)