import pandas as pd
import numpy as np

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import plotly.express as px

from dash.dependencies import Input, Output

import plotly.graph_objects as go
 
app = dash.Dash(__name__)
server = app.server

data = pd.read_csv('data/data.csv', index_col = 0)
paises = data['Country'].unique()
data['value'] = data['value'].astype(float)


iris_data = px.data.iris()
tips_data = px.data.tips()
gapminder = px.data.gapminder().query("year == 2007 & continent == 'Americas'")


fig111 = px.scatter(iris_data, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])

fig112 = px.histogram(iris_data, x="sepal_width")

fig121 = px.scatter_geo(gapminder, locations="iso_alpha",
                     size="pop", # size of markers, "pop" is one of the columns of gapminder
                     fitbounds = 'locations')

fig122 = px.histogram(iris_data, x="sepal_width", color = 'species')

fig131 = px.density_heatmap(tips_data, x="total_bill", y="tip", marginal_x="histogram", marginal_y="histogram")

fig132 = px.box(tips_data, y="total_bill")

gapminder["world"] = "world" # in order to have a single root node

fig211 = px.treemap(gapminder, path=['world', 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(gapminder['lifeExp'], weights=gapminder['pop']))

fig212 = px.sunburst(gapminder, path=['continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(gapminder['lifeExp'], weights=gapminder['pop']))

fig221 = px.pie(gapminder, values='pop', names='country', title='Population of America')


fig222 = px.violin(iris_data, y="sepal_width", color="species", box=True,
          hover_data=iris_data.columns)

c11 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c11-left-chart', figure = fig111)),
        dbc.Col(
            dcc.Graph(id = 'c11-right-chart', figure = fig112))])])

c12 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c12-left-chart', figure = fig121)),
        dbc.Col(
            dcc.Graph(id = 'c12-right-chart', figure = fig122))])])

c13 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c13-left-chart', figure = fig131)),
        dbc.Col(
            dcc.Graph(id = 'c13-right-chart', figure = fig132))])])

c21 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c21-left-chart', figure = fig211)),
        dbc.Col(
            dcc.Graph(id = 'c21-right-chart', figure = fig212))])])

c22 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c22-left-chart', figure = fig221)),
        dbc.Col(
            dcc.Graph(id = 'c22-right-chart', figure = fig222))])])

c23 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c23-left-chart')),
        dbc.Col(
            dcc.Graph(id = 'c23-right-chart'))])])

c24 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c24-left-chart')),
        dbc.Col(
            dcc.Graph(id = 'c24-right-chart'))])])

c25 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c25-left-chart')),
        dbc.Col(
            dcc.Graph(id = 'c25-right-chart'))])])

c31 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c31-left-chart')),
        dbc.Col(
            dcc.Graph(id = 'c31-right-chart'))])])

c32 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c32-left-chart')),
        dbc.Col(
            dcc.Graph(id = 'c32-right-chart'))])])

c33 = html.Div([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'c33-left-chart')),
        dbc.Col(
            dcc.Graph(id = 'c33-right-chart'))])])

app.layout = html.Div([
    dcc.Tabs(
        id='tabs-1',
        value='tab-1',
        children=[
            dcc.Tab(
                label='Elige paises',
                value='paises',
                children=[
                    html.Div("Elige los países para el análisis"),
                    dbc.Row([
                        dbc.Col(
                            dbc.Card(
                                dbc.Checklist(
                                id = 'radiopais', options = [
                                {
                                'label': p, 'value': p 
                                } for p in paises])
                                ),
                                width = 2),
                        dbc.Col(
                            dcc.Graph(id='map1'),
                            width = 8)
                    ], justify="center", align="center", className="h-50")
                ]
            ),
            dcc.Tab(
                label='Entorno',
                value='entorno',
                children=[
                    html.Div("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", style = {'margin':'80px'}),
                    dcc.Tabs(
                        id='tabs-2',
                        value='tab-1-1',
                        children=[
                            dcc.Tab(label='Internacional', value='int', children=[c11]),
                            dcc.Tab(label='Sanitario', value='sanit', children=[c12]),
                            dcc.Tab(label='Político', value='polit', children=[c13])
                        ]
                    )
                ]
            ),
            dcc.Tab(
                label='Medio',
                value='medio',
                children=[
                    html.Div("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", style = {'margin':'80px'}),
                    dcc.Tabs(
                        id='tabs-3',
                        value='tab-2-1',
                        children=[
                            dcc.Tab(label='Actividad', value='actividad', children=[c21]),
                            dcc.Tab(label='Gasto', value='gasto', children=[c22]),
                            dcc.Tab(label='Externo', value='externo', children=[c23]),
                            dcc.Tab(label='Financiero', value='financiero', children=[c24]),
                            dcc.Tab(label='Monetario', value='monetario', children=[c25])
                        ]
                    )
                ]
            ),
            dcc.Tab(
                label='Empresas',
                value='empresas',
                children=[
                    html.Div("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", style = {'margin':'80px'}),
                    dcc.Tabs(
                        id='tabs-4',
                        value='tab-3-1',
                        children=[
                            dcc.Tab(label='Confianza del consumidor', value='confianza', children=[c31]),
                            dcc.Tab(label='Expectativas empresariales', value='expectativas', children=[c32]),
                            dcc.Tab(label='Innovación', value='innovacion', children=[c33])
        ]
    )
])
            ])
            ])
@app.callback(Output('map1','figure'), [Input('radiopais','value')])

def update_map1(radiopais):
    formap = data[['Country','ISO']].drop_duplicates()
    formap['selection'] = 0

    if radiopais == None:
        radiopais = []
    formap.loc[formap['Country'].isin(radiopais),'selection'] = 1

    figure = go.Figure()
    figure = px.choropleth(formap, locations="ISO",
    color="selection",
    color_continuous_scale=px.colors.sequential.BuGn,
    fitbounds = 'locations')

    return figure.update_layout(coloraxis_showscale=False)


 
if __name__ == '__main__':
    app.run_server(debug=True)