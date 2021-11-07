
import pandas as pd
import base64
import datetime
import io
import dash
from dash.dependencies import Input, Output, State
from dash import dash_table
from dash import html
from dash import dcc
from dash import dash_table
from services.predict import predict_svm

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            df['sentiment']="Neutral"
            for i in range(len(df)):
                try:
                    df.loc[i,'sentiment'] = predict_svm(df.loc[i, "Comment"])
                except:
                    df.loc[i,'sentiment'] = "Something went wrong with the prediction"

            df['new_column'] = 12
            global_df = df
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
            df['new_column'] = 12
            global_df = df
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            export_format="csv"
        ),

        html.Hr(),  # horizontal line

    ])