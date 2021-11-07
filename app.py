import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
from dash import dash_table
from dash import html
from dash import dcc
from dash import dash_table
import dash_auth
from services.predict import predict_svm
import pandas as pd
from services.secret_service import secret_service
from components.parse_contents import parse_contents

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


auth = dash_auth.BasicAuth(
    app,
    secret_service())


app.layout = html.Div([
        html.H1(
        children='Basic Sentiment Analysis'
    ),
    html.H3("Type a comment"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='Example Review', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload')
])



@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    if input_value == 'Example Review':
        return f'Here you will see the sentiment of your comment'

    sentiment = predict_svm(input_value)

    return f'The sentiment of your comment is: {sentiment}'


@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


if __name__ == '__main__':
    app.run_server(debug=True)