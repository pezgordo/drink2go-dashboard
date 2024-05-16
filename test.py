#importar librerias
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_table as dt
import glob
import os
import plotly.express as px

from dash.exceptions import PreventUpdate

import dash_bootstrap_components as dbc



# Load the Excel file
df = pd.read_excel('datos2.xlsx', header=None)


column_name = df.iloc[0, 0]


nombres_empresas = df.iloc[4:9, 0].tolist()
ano_t = df.iloc[4:9, 1].tolist()
ano_t_1 = df.iloc[4:9, 2].tolist()
diferencia = df.iloc[4:9, 3].tolist()
porcentaje = df.iloc[4:9, 4].tolist()

#print(nombres_empresas)
#print(ano_t)

# Create DataFrame
data = {
    'Empresa': nombres_empresas,
    'Año T': ano_t,
    'Año T-1': ano_t_1,
    'Diferencia': diferencia,
    'Porcentaje': porcentaje
}

result_df = pd.DataFrame(data)
# Rename the headers


print(result_df)

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
bootstrap = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css'
external_stylesheets = [meta_tags, font_awesome, bootstrap]




app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server = app.server

#EMPIEZA LA APLICACION DASH
app.layout = html.Div([

    # INICIO DIV 1
    html.Div([

        #1.1 DIV SUPERIOR LOGO
        html.Div([
            html.Img(src = app.get_asset_url('logo.png'),
                        style = {'height': '150px'},
                        className = 'title_image'
                        ),
                


        ], className='one-third column', id = 'title11'),

        #1.2 TITULO
        html.Div([
            html.H6('Cuadro de control - Drink2Go',
                        style = {'color': '#00622b'},
                        className = 'title'
                        
                        ),

        ], className='one-third column', id = 'title111')

    # FIN DE DIV 1  
        ], className = 'flex_container2'), 



    # Inicio DIV 2 - ROW 1
    html.Div([
        #Column 1
        html.Div([
            # Titulo
            html.H1("Data from Excel", className="mt-4"),
            # Grafico
            html.Div([
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': result_df['Empresa'], 'y': result_df['Año T'], 'type': 'bar', 'name': 'Año T'},
                            {'x': result_df['Empresa'], 'y': result_df['Año T-1'], 'type': 'bar', 'name': 'Año T-1'}
                        ],
                        'layout': {
                            'title': 'Año_t and Año_t-1 by Empresa',
                            'legend': {'orientation': 'h', 'x': 1, 'y': 1.0, 'xanchor': 'top', 'yanchor': 'right'},
                            #'legend': {'orientation': 'h'},
                        },
                    },
                    style={
                        'width':'100%',
                        'height':'300px',
                        
                    },
                    
                )
            ]),
            html.Div([
                html.Div('Valor de la Compañia', className="h6 mt-4"),
                dt.DataTable(
                    id='datatable',
                    columns=[{'name': col, 'id': col} for col in result_df.columns],
                    data=result_df.to_dict('records'),
                    style_table={'overflowX': 'auto'},
                    style_cell={'fontSize': 10, 
                                'font-family': 'Arial', 
                                'text-align': 'left'
                                },
                    style_header={'backgroundColor': 'lightgrey', 
                                  'fontWeight': 'bold'
                                }
                )
            ])
        # Fin Column 1
        ], className="col"),

        # Column 2
        


        # Column 3
       


        # Column 4
        



        
    # Fin Row 1    
    ], className="row row-cols-1 row-cols-sm-2 row-cols-md-4")


# Fin de div principal
], className="container mt-4")


#INICIO DE APP

if __name__ == '__main__':
    app.run_server(debug=True)