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


# Graph 1 Valor de la compania GRAFICO 
def valor_de_la_compania_graph(df):

    nombres_empresas = df.iloc[3:9, 0].tolist()
    ano_t = df.iloc[3:9, 1].tolist()
    ano_t_1 = df.iloc[3:9, 2].tolist()
    diferencia = df.iloc[3:9, 3].tolist()
    porcentaje = df.iloc[3:9, 4].tolist()

    # Create DataFrame
    data = {
        'Empresa': nombres_empresas,
        'Año T': ano_t,
        'Año T-1': ano_t_1,
        'Diferencia': diferencia,
        'Porcentaje': porcentaje
    }

    result_df = pd.DataFrame(data)

    # Create the bar chart using Plotly Express
    fig = px.bar(
        result_df,
        x='Empresa', 
        y=['Año T', 'Año T-1'], 
        barmode='group', 
        labels={'x': 'Empresa', 'y': 'Valorrr'}, 
        #title='Valor de la Compañia'
        )
    fig.update_layout(
            legend=dict(
                title_text='',
                orientation="h",
                entrywidth=50, 
                yanchor="bottom", 
                y=1.00, 
                xanchor="right", 
                x=1.0,
                font=dict(
                    size=9
                )
            ),
            margin=dict(
                b=0,
                l=0,
                r=0,
                t=0,
            ),
            hovermode='x'
        )
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Valor')

    # Create the graph outside the app layout
    graph = dcc.Graph(
        id='example-graph',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '300px'},  # Set graph width and height
    )

    return graph

# Table 1 Valor de la compania TABLA
def valor_de_la_compania_table(df):

    nombres_empresas = df.iloc[3:9, 0].tolist()
    ano_t = df.iloc[3:9, 1].tolist()
    ano_t_1 = df.iloc[3:9, 2].tolist()
    diferencia = df.iloc[3:9, 3].tolist()
    porcentaje = df.iloc[3:9, 4].tolist()

    # Create DataFrame
    data = {
        'Empresa': nombres_empresas,
        'Año T': ano_t,
        'Año T-1': ano_t_1,
        'Diferencia': diferencia,
        'Porcentaje': porcentaje
    }

    result_df = pd.DataFrame(data)
    data_table = dt.DataTable(
                    id='datatable',
                    columns=[{'name': col, 'id': col} for col in result_df.columns],
                    data=result_df.to_dict('records'),
                    style_table={'overflowX': 'auto'},
                    style_cell={'fontSize': 10, 
                                'font-family': 'Arial', 
                                'text-align': 'center'
                                },
                    style_header={'backgroundColor': 'lightgrey', 
                                  'fontWeight': 'bold'
                                }
                )
    return data_table


# Graph 2 Comparativa de Valor de companias
def comparativa_valor_compania_graph(df):

    nombres_empresas = df.iloc[12:17, 0].tolist()
    a_2023 = df.iloc[12:17, 6].tolist()
    a_2024 = df.iloc[12:17, 5].tolist()
    a_2025 = df.iloc[12:17, 4].tolist()
    a_2026 = df.iloc[12:17, 3].tolist()
    a_2027 = df.iloc[12:17, 2].tolist()
    a_2028 = df.iloc[12:17, 1].tolist()
    
    # Create DataFrame
    data = {
        'Empresa': nombres_empresas,
        '2023': a_2023,
        '2024': a_2024,
        '2025': a_2025,
        '2026': a_2026,
        '2027': a_2027,
        '2028': a_2028,
    }

    result_df = pd.DataFrame(data)

    # Create the bar chart using Plotly Express
    fig = px.line(
        result_df.melt(id_vars='Empresa', var_name='Año', value_name='Valor'),
        x='Año',
        y='Valor',
        
        color='Empresa', 
        #x=['2023', '2024', '2025', '2026', '2027', '2028'],
        #y=result_df.iloc[:, 1:].values.T,
        #x=['2023', '2024','2025', '2026', '2027', '2028'],
        #y=['2023', '2024','2025', '2026', '2027', '2028'],  
        labels={'x': 'Empresa', 'y': 'Valorrr'},
        markers=True,
        )
    fig.update_layout(
            legend=dict(
                title_text='',
                orientation="h",
                entrywidth=50, 
                yanchor="bottom", 
                y=1.00, 
                xanchor="right", 
                x=1.0,
                font=dict(
                    size=9
                )
            ),
            margin=dict(
                b=0,
                l=0,
                r=0,
                t=0,
            ),
            hovermode='x'
        )
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Valor')

    # Create the graph outside the app layout
    graph = dcc.Graph(
        id='example-graph2',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '300px'},  # Set graph width and height
    )

    return graph


# NOT USED Table - KPIs

def kpi_unidades_vendidas_graph(df):

    titulo = df.iloc[21, 0]
    ano_0 = df.iloc[21, 1]
    ano_1 = df.iloc[21, 2]
    diferencia = df.iloc[21, 3]
    variacion = df.iloc[21, 4]

        # Create DataFrame
    data = {
        'Titulo': [titulo],
        'Año 0': [ano_0],
        'Año -1': [ano_1],
        'Diferencia': [diferencia],
        'Variacion': [variacion],
    }

    result_df = pd.DataFrame(data)

     # Create the bar chart using Plotly Express
    fig = px.bar(
        result_df,
        x='Titulo', 
        y=['Año 0', 'Año -1'], 
        barmode='group', 
        labels={'x': 'Empresa', 'y': 'Valorrr'}, 
        #title='Valor de la Compañia'
        )
    
        # Create the graph outside the app layout
    graph = dcc.Graph(
        id='kpis-graph',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '300px'},  # Set graph width and height
    )

    return graph

#KPIs Data Table
def kpis_table(df):

    kpis = df.iloc[21:37, 0].tolist()
    ano_t = df.iloc[21:37, 1].tolist()
    ano_t_1 = df.iloc[21:37, 2].tolist()
    diferencia = df.iloc[21:37, 3].tolist()
    porcentaje = df.iloc[21:37, 4].tolist()

    # Create DataFrame
    data = {
        'KPI': kpis,
        'Año T': ano_t,
        'Año T-1': ano_t_1,
        'Diferencia': diferencia,
        'Variacion': porcentaje
    }

    result_df = pd.DataFrame(data)

    # Define row indices you want to represent as percentages
    percentage_rows_indices = [1, 4, 6, 7, 8, 10, 11, 15]

    # Multiply the values in the specified rows by 100
    result_df.loc[percentage_rows_indices, 'Año T'] *= 100

    # Convert specified columns to float
    columns_to_convert = ['Año T', 'Año T-1', 'Diferencia', 'Variacion']
    result_df[columns_to_convert] = result_df[columns_to_convert].astype(float)

    # Format only the values in the specified rows as percentages
    result_df.loc[percentage_rows_indices, 'Año T'] = result_df.loc[percentage_rows_indices, 'Año T'].apply(lambda x: "{:.2f}%".format(x))

    # Format only the values in the specified rows as percentages
    result_df.loc[percentage_rows_indices, 'Año T-1'] = result_df.loc[percentage_rows_indices, 'Año T-1'].apply(lambda x: "{:.2f}%".format(x))

    # Format as column as percentage
    result_df['Variacion'] = result_df['Variacion'].apply(lambda x: "{:.2f}%".format(x * 100))  


    # Add a new column 'Arrow' with arrow icons based on 'Diferencia' values
    def create_arrow(row):
        if row['Diferencia'] > 0:
            return '&#9650;'  # Green arrow pointing up
        elif row['Diferencia'] < 0:
            return '&#9660;'  # Red arrow pointing down
        else:
            return ''

    result_df['Arrow'] = result_df.apply(create_arrow, axis=1)

    data_table = dt.DataTable(
                    id='kpis_datatable',
                    columns=[
                        {'name': col, 'id': col} if col != 'Arrow' else {'name': '', 'id': col, 'type': 'text', 'presentation': 'markdown'}
                        for col in result_df.columns
                    ],
                    data=result_df.to_dict('records'),
                    style_table={'overflowX': 'auto'},
                    style_cell={
                        'textAlign': 'right',
                        'fontSize': 10,
                        'font-family': 'Arial',
                    }, 
                        style_cell_conditional=[
                            {'if': {'column_id': result_df.columns[0]}, 'textAlign': 'left'}
                        ],

                    style_header={'backgroundColor': 'lightgrey', 
                                  'fontWeight': 'bold'
                                },
                            style_data_conditional=[
                                {
                                    'if': {
                                        'column_id': 'Diferencia',
                                        'filter_query': '{Año T} < {Año T-1}'
                                    },
                                    'backgroundColor': 'red',
                                    'color': 'white'
                                },
                                {
                                    'if': {
                                        'column_id': 'Diferencia',
                                        'filter_query': '{Año T} > {Año T-1}'
                                    },
                                    'backgroundColor': 'green',
                                    'color': 'white'
                                },
                                {
                                    'if': {'column_id': 'Arrow', 'filter_query': '{Diferencia} > 0'},
                                    'color': 'green',
                                },
                                {
                                    'if': {'column_id': 'Arrow', 'filter_query': '{Diferencia} < 0'},
                                    'color': 'red',
                                }
                            ]
                    )
    return data_table


# Graph Promocion Punto de venta por canal
def promo_punto_de_venta_graph():

    data = {
        "Pais": ["España", "Portugal", "Francia", "Italia", "Centro Europa", "Poland", "Mexico"],
        "Tienda_Tradicional_2027": [192394, 234543, 165367, 108526, 196534, 132540, 187654],
        "Gran_Superficie_2027": [157894, 176788, 192937, 165375, 154345, 164600, 164600],
        "Hosteleria_2027": [143234, 232345, 150550, 123498, 178943, 154567, 156765],
        "Tienda_Tradicional_2028": [104186, 38524, 83927, 108526, 95, 132540, 120150],
        "Gran_Superficie_2028": [157894, 81997, 192937, 165375, 90520, 164600, 164600],
        "Hosteleria_2028": [43410, 17363, 150550, 123498, 85730, 122340, 132234]
    }

    df = pd.DataFrame(data)

    # Splitting into separate DataFrames for each year
    df_2027 = df[['Pais', 'Tienda_Tradicional_2027', 'Gran_Superficie_2027', 'Hosteleria_2027']].copy()
    df_2028 = df[['Pais', 'Tienda_Tradicional_2028', 'Gran_Superficie_2028', 'Hosteleria_2028']].copy()

    # Melt the DataFrames to long format for Plotly Express
    df_melted_2027 = df_2027.melt(id_vars=["Pais"], var_name="Categoria", value_name="Valor")
    df_melted_2027['Año'] = '2027'

    df_melted_2028 = df_2028.melt(id_vars=["Pais"], var_name="Categoria", value_name="Valor")
    df_melted_2028['Año'] = '2028'

    # Concatenate the two melted DataFrames
    df_combined = pd.concat([df_melted_2027, df_melted_2028])

    # Update Categoria column for better labels
    #df_combined['Categoria'] = df_combined['Categoria'].str.replace('_', ' ').str.replace('Tienda Tradicional', 'Tienda Tradicional').str.replace('Gran Superficie', 'Gran Superficie').str.replace('Hosteleria', 'Hostelería')
    #df_combined['Categoria'] = df_combined['Categoria'].str.replace('2027', ' 2027').str.replace('2028', ' 2028')



    # Plotting using Plotly Express
    fig = px.bar(df_combined, 
                    x='Categoria',
                    y='Valor', 
                    color='Año', 
                    facet_col='Pais',
                    #barmode='group',
                    category_orders={"Categoria": ["Tienda_Tradicional_2027", "Tienda_Tradicional_2028", "Gran_Superficie_2027", "Gran_Superficie_2028", "Hosteleria_2027", "Hosteleria_2028"]},
                    #category_orders={"Categoria": ["Tienda Tradicional 2027", "Tienda Tradicional 2028", "Gran Superficie 2027", "Gran Superficie 2028", "Hostelería 2027", "Hostelería 2028"]},

                    #category_orders={"Categoria": ["Tienda_Tradicional_2027", "Gran_Superficie_2027", "Hosteleria_2027", "Tienda_Tradicional_2028", "Gran_Superficie_2028", "Hosteleria_2028"]},

                    labels={'Valor': '', 'Categoria': '', 'Año': 'Año'},
                    title='Promocion punto de venta por Canal. Drink2Go'
                    )

    # Update annotations if necessary
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    graph = dcc.Graph(
        id='punto_de_venta_graph',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height':'100%'},
    )
    return graph


# 3 Graphs for Incentivo de ventas por producto Drink2Go
def plot_incentivos(tipo_grafico):
    # Datos
    data = {
        "Producto": ["Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos"],
        "Año": [2028]*3 + [2027]*3,
        "Ingresos": [12402359, 5176663, 3938970, 10519803, 5061799, 4247517],
        "% Incentivos": [105, 100, 109, 93, 84, 78],
        "Volumen Incentivos": [1302248, 517666, 429348, 978342, 425191, 331306]
    }
    
    # Crear DataFrame con los datos
    df = pd.DataFrame(data)

    # Verificar el tipo de gráficos
    if tipo_grafico == 'porcentaje':
        # Gráfico de barras para % de incentivos
        fig = px.bar(df, x="Año", y="% Incentivos", color="Producto",
                      title="Porcentaje de incentivos por producto",
                      labels={"% Incentivos": "Porcentaje de incentivos (%)"},
                      barmode="group")
    elif tipo_grafico == 'volumen':
        # Gráfico de barras para volumen de incentivos
        fig = px.bar(df, x="Año", y="Volumen Incentivos", color="Producto",
                      title="Volumen de incentivos por producto",
                      #labels={"Volumen Incentivos": "Volumen de incentivos"},
                      barmode="group")
    elif tipo_grafico== 'ingresos':
        # Grafico de barras apiladas
        fig = px.bar(df, x="Año", y="Ingresos", color="Producto",
                    title="Incentivo de ventas por producto",
                    #labels={"Ingresos": "Ingresos ($)"},
                    barmode="group")

    else:
        print("Tipo de gráfico no válido. Debe ser 'porcentaje' o 'volumen'.")
        return None

    # Add showlegend=False to hide legend
    #fig.update_traces(showlegend=False)
    fig.update_layout(xaxis=dict(showticklabels=True, title=''), yaxis=dict(showticklabels=True, title=''))

    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))

    graph = dcc.Graph(
        id='incentivo_de_ventas_3_graphs',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height':'200px'},
    )
    return graph
    

# Impacto de celebridades por mercado
def impacto_celebridades():
    # Data
    data = {
        "Celebridad": ["Mensi", "Polinsky", "Romano", "Reno", "Shykira"],
        "España": [220, 130, 210, 160, 190],
        "Portugal": [160, 120, 230, 110, 200],
        "Francia": [140, 170, 160, 230, 260],
        "Italia": [190, 160, 180, 90, 150],
        "Centro Europa": [150, 170, 120, 110, 120],
        "Polonia": [120, 220, 100, 120, 110],
        "México": [220, 110, 180, 160, 170]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Melt DataFrame to long format
    df_long = pd.melt(df, id_vars=['Celebridad'], var_name='Mercado', value_name='Impacto')

    # Plot
    fig = px.bar(
        df_long, 
        x='Celebridad', 
        y='Impacto', 
        color='Mercado',
        #title='Impacto de las celebridades por mercado',
        labels={'Impacto': 'Puntos adicionales en Valor de Marca', 'Celebridad': 'Celebridad'},
        barmode='group')
    
    fig.update_layout(
        xaxis_title=None, 
        yaxis_title=None,
        legend=dict(
                title_text='',
                orientation="h",
                entrywidth=40, 
                yanchor="bottom", 
                y=1.00, 
                xanchor="right", 
                x=1.0,
                font=dict(
                    size=9
                )
            ),
            margin=dict(
                b=0,
                l=0,
                r=0,
                t=0,
            ),
            #hovermode='x'
        )
    
    graph = dcc.Graph(
        id='impacto_celebridades',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height':'300px'},
    )
    return graph

# Precios de bebidas por Pais
def plot_Bebida_Precio(Bebida_type):

    data = {
        "Pais": ["España", "España", "España", "Portugal", "Portugal", "Portugal", "Francia", "Francia", "Francia", "Italia", "Italia", "Italia", "Centro Europa", "Centro Europa", "Centro Europa", "Polonia", "Polonia", "Polonia", "Mexico", "Mexico", "Mexico"],
        "Bebida": ["Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos"],
        "2023": [12, 18, 22, 11, 17, 23, 13, 19, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "2024": [16, 24, 3, 16, 23, 31, 18, 26, 34, 16, 24, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "2025": [2, 28, 35, 2, 28, 36, 25, 3, 38, 24, 36, 45, 0, 0, 0, 0, 0, 0, 24, 36, 45],
        "2026": [2, 28, 35, 2, 28, 36, 25, 3, 38, 3, 4, 56, 0, 0, 0, 24, 28, 35, 3, 4, 5],
        "2027": [2, 28, 3, 2, 28, 3, 23, 28, 32, 24, 3, 34, 28, 34, 35, 26, 32, 38, 3, 29, 5],
        "2028": [25, 28, 29, 24, 28, 29, 27, 28, 3, 28, 31, 34, 28, 32, 32, 27, 32, 35, 32, 33, 38],
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)

    # Melt the DataFrame
    df_melted = df.melt(id_vars=["Pais", "Bebida"], var_name="Año", value_name="Precio")

    # Filter DataFrame for the specified Bebida type
    df_filtered = df_melted[df_melted['Bebida'] == Bebida_type]

    # Create the Line Chart
    fig = px.line(df_filtered, x="Año", y="Precio", color="Pais", markers=True,
                  title=f"Precio de bebidas por Pais - {Bebida_type}",
                  labels={"Año": "Año", "Precio": "Precio Level", "Pais": "Pais"})


    fig.update_layout(
        xaxis_title=None, 
        yaxis_title=None,
        legend=dict(
                title_text='',
                orientation="h",
                entrywidth=40, 
                yanchor="bottom", 
                y=1.00, 
                xanchor="right", 
                x=1.0,
                font=dict(
                    size=9
                )
            ),
            margin=dict(
                b=0,
                l=0,
                r=0,
                t=100,
            ),
            #hovermode='x'
        )


    graph = dcc.Graph(
        id='Precio de bebidas por Pais',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height':'300px'},
    )
    return graph

# Example usage:
plot_Bebida_Precio("Refrescos")

### INICIO APP

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
        #Column 1 - Row 1
        html.Div([
            # Titulo
            html.Div("Valor de la Compañia", className="h6 text-center mt-4"),
            # Grafico
            html.Div([
                valor_de_la_compania_graph(df),

            ]),
            html.Div([
                #html.Div('Valor de la Compañia', className="h6 mt-4"),
                #valor_de_la_compania_table(df),
            ])
        # Fin Column 1 - Row 1
        ], className="col"),

        # Column 2 - Row 1
        html.Div([
            # Titulo
            html.Div("Comparativa de Valor", className="h6 text-center mt-4"),
            # Grafico
            html.Div([
                comparativa_valor_compania_graph(df),

            ]),
            html.Div([
                #html.Div('Valor de la Compañia', className="h6 mt-4"),
                #valor_de_la_compania_table(df),
            ])
        # Fin Column 2 - Row 1
        ], className="col"),


        # Column 3
         html.Div([
            # Titulo
            html.Div("Impacto de las Celebredades por mercado", className="h6 text-center mt-4"),
            # Grafico
            html.Div([
                impacto_celebridades(),

            ]),
            html.Div([
                #html.Div('Valor de la Compañia', className="h6 mt-4"),
                #kpis_table(df),
            ])
                    # Fin Column 2
        ], className="col"),

        # Column 4
        
    # Fin Row 1    
    ], className="row row-cols-1 row-cols-sm-2 row-cols-md-3"),

    # INICIO ROW 2
    html.Div([
        #Column 1 - Row 2
        html.Div([
            # Titulo
            #html.Div("KPIs de Drink2Go", className="h6 text-center mt-4"),
            # Grafico
            html.Div([
                kpis_table(df),
            ], className="h-100"),
            html.Div([
                #html.Div('Valor de la Compañia', className="h6 mt-4"),
                #valor_de_la_compania_table(df),
            ])
        # Fin Column 1 - Row 2
        ], className="col-md-8"),

        # Column 2 - Row 2
        html.Div([
            # Titulo
            #html.Div("Promocion Punto de Venta por Canal. Drink2Go", className="h6 text-center mt-4"),
            # Grafico
            html.Div([
                html.Div([
                    
                    plot_incentivos(tipo_grafico='porcentaje'),  # Mostrar gráfico de porcentaje de incentivos
                    
                ], className="row"),
                html.Div([
                    #html.Div('Valor de la Compañia', className="h6 mt-4"),
                    #valor_de_la_compania_table(df),
                    plot_incentivos(tipo_grafico='volumen')  
                ], className='row'),
                html.Div([
                    #html.Div('Valor de la Compañia', className="h6 mt-4"),
                    #valor_de_la_compania_table(df),
                    plot_incentivos(tipo_grafico='ingresos')  
                ], className='row'),

        ],className="h-100"),
        # Fin Column 1 - Row 2
        ], className="col-md-4"),

         # Fin Row 2    
    ], className="row row-cols-1 row-cols-sm-2 row-cols-md-2"),


    # INICIO ROW 3
    html.Div([
        # Column 2 - Row 2
        html.Div([
            # Titulo
            #html.Div("Promocion Punto de Venta por Canal. Drink2Go", className="h6 text-center mt-4"),
            # Grafico
            html.Div([
                promo_punto_de_venta_graph(),
            ]),
            html.Div([
                #html.Div('Valor de la Compañia', className="h6 mt-4"),
                #valor_de_la_compania_table(df),
            ])
        # Fin Column 1 - Row 2
        ], className="col"),

    # Fin Row 3    
    #], className="row row-cols-1 row-cols-sm-2 row-cols-md-2")
    ], className="row"),

    # INICIO ROW 4
    html.Div([
        # Column 1 - Row 4
        html.Div([
            # Grafico
            html.Div([
                plot_Bebida_Precio("Refrescos"),
            ]),       
        ], className="col"),

        # Column 2 - Row 4
        html.Div([
            # Grafico
            html.Div([
                plot_Bebida_Precio("Isotonicas"),
            ]),       
        ], className="col"),

        # Column 3 - Row 4
        html.Div([
            # Grafico
            html.Div([
                plot_Bebida_Precio("Zumos"),
            ]),       
        ], className="col"),


    # Fin Row 3    
    ], className="row row-cols-1 row-cols-sm-2 row-cols-md-3")
   



# Fin de div principal
], className="container mt-4")


#INICIO DE APP

if __name__ == '__main__':
    app.run_server(debug=True)


