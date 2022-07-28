import dash_mantine_components as dmc
from dash import Dash, html

from layout.appshell import create_appshell

app = Dash(__name__)

app.layout = create_appshell()

if __name__ == "__main__":
    app.run_server()
