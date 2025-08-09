import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("Saldo Total"), xs=12, md=6),  # xs=12 (celular), md=6 (desktop)
        dbc.Col(html.Div("Deuda Total"), xs=12, md=6)
    ])
], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)
