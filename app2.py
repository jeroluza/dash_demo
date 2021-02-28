import dash
import dash_core_components as dcc
import dash_html_components as html
 
app = dash.Dash()
app.layout = html.Div([
    dcc.Tabs(
        id='tabs-1',
        value='tab-1',
        children=[
            dcc.Tab(
                label='Tab 1',
                value='tab-1',
                children=[
                    html.Div("Content 1"),
                    dcc.Tabs(
                        id='tabs-2',
                        value='tab-1-1',
                        children=[
                            dcc.Tab(label='Tab 1-1', value='tab-1-1', children=["Content 1-1"]),
                            dcc.Tab(label='Tab 1-2', value='tab-1-2', children=["Content 1-2"])
                        ]
                    )
                ]
            ),
            dcc.Tab(
                label='Tab 2',
                value='tab-2',
                children=[
                    html.Div("Content 2"),
                    dcc.Tabs(
                        id='tabs-3',
                        value='tab-2-1',
                        children=[
                            dcc.Tab(label='Tab 2-1', value='tab-2-1', children=["Content 2-1"]),
                            dcc.Tab(label='Tab 2-2', value='tab-2-2', children=["Content 2-2"])
                        ]
                    )
                ]
            ),
            dcc.Tab(label='Tab 3', value='tab-3', children=["Content 3"])
        ]
    )
])
 
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
 
if __name__ == '__main__':
    app.run_server(debug=True)