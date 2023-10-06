import dash
from dash import html, dcc, callback, Input, Output, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, title="Dashboard", name='Our Analytics Dashboard')
df = pd.read_csv("../games.csv")

columns = df.columns
layout = html.Div([
    html.Hr(),
    html.H3("Test"),
    dash_table.DataTable(style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    }, data=df.to_dict('records'), page_size=6),
    html.H3("X values"),
    dcc.Dropdown(options=columns, id='x_values', value="white_rating"),
    html.H3("Y values"),
    dcc.Dropdown(options=columns, id='y_values', value="white_rating"),
    html.Hr(),
    html.Div([
        dcc.Graph(figure={}, id='controls-and-graph')
    ]),
    # Input for specifying the number of samples to display.
    html.Label("Number of Samples Per Species:"),
    dcc.Input(
        id="sample-limit",
        type="number",
        placeholder="Enter number of samples (up to 19000)",
        value=10,
        min=1,
        max=19113,
    ),
    html.Div([
        dcc.Graph(figure={}, id='controls')
    ])
])


@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='x_values', component_property='value'),
    Input(component_id='y_values', component_property='value')
)
def update_bar_graph(col_chosen, row_chosen):
    fig = px.histogram(df, x=row_chosen, y=col_chosen, histfunc='avg')
    return fig


@callback(
    Output(component_id='controls', component_property='figure'),
    Input(component_id='x_values', component_property='value'),
    Input(component_id='y_values', component_property='value'),
    Input(component_id="sample-limit", component_property="value"),
)
def update_scatter_graph(col_chosen, row_chosen, values):
    fig = px.scatter(df[:values], x=col_chosen, y=row_chosen, size_max=55, color="winner")
    return fig
