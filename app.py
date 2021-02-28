import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import plotly.express as px

from dash.dependencies import Input, Output

import plotly.graph_objects as go

#external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

app = dash.Dash(__name__) #external_stylesheets=external_stylesheets)
server = app.server

data = pd.read_csv('data/data.csv', index_col = 0)
paises = data['Country'].unique()
data['value'] = data['value'].astype(float)

print(data['Series Name'].unique())

app.layout = html.Div([
    html.H1('DEMO', style={
            'textAlign': 'center', 'margin': '48px 0', 'fontFamily': 'system-ui'}),
    

    dcc.Tabs(id="tabs", children = [

        dcc.Tab(label='Elige paises en el mapa', children = [
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
            ], justify="center", align="center", className="h-50")]),
        dcc.Tab(label='Nutricion',children = [
            html.H2('Prevalencia de desnutrición (% de la población)', style={
            'textAlign': 'center', 'margin': '48px 0', 'fontFamily': 'system-ui'}),
            html.P('América del Sur alberga la mayoría (55%) de las personas subalimentadas de la región, y el aumento observado en los últimos años se debe sobre todo al deterioro de la seguridad alimentaria en la República Bolivariana de Venezuela, donde la prevalencia de la subalimentación aumentó casi cuatro veces, de 6,4% en 2012-2014 a 21,2% en 2016-2018.',style={
            'textAlign': 'center','margin': '48px 0'}),
            dbc.Row([
                dbc.Col([
                                    dcc.Graph(
                                            id='map2'),
                                    dcc.Slider(
                                            id='slider1',
                                            min=2011,
                                            max=2018,
                                            step=1,
                                            value=2011,
                                            marks = {x:str(x) for x in range(2011,2019)})], width = 4),
                dbc.Col(
                    dcc.Graph(
                            id='scatter1'
                                ), 
                    width = 4),
            ], justify="center", align="center", className="h-50")
            ]
            )
        ]
        )
    ]
    )


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

@app.callback([Output('map2','figure'), Output('scatter1','figure')], [Input('radiopais','value'), Input('slider1','value')])

def update_tab2(radiopais, slider1):

    if radiopais == None:
        radiopais = []
    

    formap = data[(data['Country'].isin(radiopais))&(data['year'] == slider1)&(data['vars']=='nutr')]


    figure1 = go.Figure()
    figure1 = px.choropleth(formap, locations="ISO",
    color="value",
    color_continuous_scale=px.colors.sequential.Bluered,
    fitbounds = 'locations')

    figure2 = go.Figure()
    
    for pais in radiopais:
        forscatter = data[(data['Country'] == pais)&(data['vars']=='nutr')]
        figure2.add_trace(
            go.Scatter(x = forscatter['year'], y = forscatter['value'], name = pais))

    figure2.update_xaxes(
    range=(2010, 2019),
    constrain='domain')


    return figure1, figure2


if __name__ == '__main__':
	app.run_server(debug=True)