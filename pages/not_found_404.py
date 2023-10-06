import dash
from dash import html

dash.register_page(__name__, title="Title", name="Intro")

layout = html.H1("This was the 404 content. But now it's the home page :D ")