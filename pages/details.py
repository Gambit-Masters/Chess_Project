import dash
from dash import html, dash_table
import pandas as pd

dash.register_page(__name__, title="Chess Information")
df = pd.read_csv("../games.csv")

layout = html.Div([
    html.H1('This is our Details page'),
    html.Div('This is our Details page content.'),

    dash_table.DataTable(
        style_data={
            'whiteSpace': 'normal',
            'height': 'auto',
        },
        data=df.to_dict('records'),
        page_size=10
    ),
    html.Hr(),
    html.H2("Below is information on the columns")
])
