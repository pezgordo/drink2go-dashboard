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
from plotly.subplots import make_subplots
from dash.exceptions import PreventUpdate

import dash_bootstrap_components as dbc



# Load the Excel file
df2 = pd.read_excel('datos2.xlsx', header=None)

df = pd.read_excel('datos_final.xlsx', header=None)


### GERENCIA GENERAL ###

### 1 ###
# KPIs Data Table
def kpis_table(df):

    kpis = df.iloc[78:94, 1].tolist()
    ano_t = df.iloc[78:94, 2].tolist()
    ano_t_1 = df.iloc[78:94, 3].tolist()
    diferencia = df.iloc[78:94, 4].tolist()
    porcentaje = df.iloc[78:94, 5].tolist()

    # Create DataFrame
    data = {
        'KPI': kpis,
        'Año 0': ano_t,
        'Año -1': ano_t_1,
        'Diferencia': diferencia,
        'Variacion': porcentaje
    }

    result_df = pd.DataFrame(data)

    # Define row indices you want to represent as percentages
    percentage_rows_indices = [1, 4, 6, 7, 8, 10, 11, 15]

    # Multiply the values in the specified rows by 100
    result_df.loc[percentage_rows_indices, 'Año 0'] *= 100
    result_df.loc[percentage_rows_indices, 'Año -1'] *= 100


    # Convert specified columns to float
    columns_to_convert = ['Año 0', 'Año -1', 'Diferencia', 'Variacion']
    result_df[columns_to_convert] = result_df[columns_to_convert].astype(float)

    # Format only the values in the specified rows as percentages
    result_df.loc[percentage_rows_indices, 'Año 0'] = result_df.loc[percentage_rows_indices, 'Año 0'].apply(lambda x: "{:.2f}%".format(x))

    # Format only the values in the specified rows as percentages
    result_df.loc[percentage_rows_indices, 'Año -1'] = result_df.loc[percentage_rows_indices, 'Año -1'].apply(lambda x: "{:.2f}%".format(x))

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
                                        'filter_query': '{Año 0} < {Año -1}'
                                    },
                                    'backgroundColor': 'red',
                                    'color': 'white'
                                },
                                {
                                    'if': {
                                        'column_id': 'Diferencia',
                                        'filter_query': '{Año 0} > {Año -1}'
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

### 2 ###
# Comparativa de Valor de companias
def comparativa_valor_compania_graph(df):

    nombres_empresas = df.iloc[13:19, 0].tolist()
    a_2023 = df.iloc[13:19, 1].tolist()
    a_2024 = df.iloc[13:19, 2].tolist()
    a_2025 = df.iloc[13:19, 3].tolist()
    a_2026 = df.iloc[13:19, 4].tolist()
    a_2027 = df.iloc[13:19, 5].tolist()
    a_2028 = df.iloc[13:19, 6].tolist()
    
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
        title='Comparativa de Valor',
        markers=True,
        )
    fig.update_layout(
            legend=dict(
                #title_text='Comparativa de Valor',
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
                t=130,
            ),
            hovermode='x'
        )
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Valor')

    # Create the graph outside the app layout
    graph = dcc.Graph(
        id='comparativa_valor',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '400px'},  # Set graph width and height
    )

    return graph




### 3 ###
# Graph 2 Valor de la compania GRAFICO 
def valor_de_la_compania_graph(df):

    nombres_empresas = df.iloc[4:10, 1].tolist()
    a_2028 = df.iloc[4:10, 2].tolist()
    a_2027 = df.iloc[4:10, 3].tolist()
    diferencia = df.iloc[4:10, 4].tolist()
    porcentaje = df.iloc[4:10, 5].tolist()

    # Create DataFrame
    data = {
        'Empresa': nombres_empresas,
        '2028': a_2028,
        '2027': a_2027,
        'Diferencia': diferencia,
        'Porcentaje': porcentaje
    }

    result_df = pd.DataFrame(data)

    # Create the bar chart using Plotly Express
    fig = px.bar(
        result_df,
        x='Empresa', 
        y=['2028', '2027'], 
        barmode='group', 
        labels={'x': 'Empresa', 'y': 'Valorrr'}, 
        title='Valor de la Compañia'
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
                t=130,
            ),
            hovermode='x'
        )
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Valor')

    # Create the graph outside the app layout
    graph = dcc.Graph(
        id='valor_compania',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '400px'},  # Set graph width and height
    )

    return graph



### 4 ###
# Analisis valor de la compañia grafico
def analisis_valor_de_la_compania(df):

    parametro = df.iloc[24:30, 0].tolist()
    a_2023 = df.iloc[24:30, 1].tolist()
    a_2024 = df.iloc[24:30, 2].tolist()
    a_2025 = df.iloc[24:30, 3].tolist()
    a_2026 = df.iloc[24:30, 4].tolist()
    a_2027 = df.iloc[24:30, 5].tolist()
    a_2028 = df.iloc[24:30, 6].tolist()


    # Create DataFrame
    data = {
        'Parametro': parametro,
        '2023': a_2023,
        '2024': a_2024,
        '2025': a_2025,
        '2026': a_2026,
        '2027': a_2027,
        '2028': a_2028,
        '2027': a_2027
    }

    result_df = pd.DataFrame(data)

    df_melted = result_df.melt(id_vars=['Parametro'], var_name='Año', value_name='Ponderacion Media')


    # Create the bar chart using Plotly Express
    fig = px.bar(
        df_melted,
        x='Año', 
        y='Ponderacion Media',
        color='Parametro', 
        barmode='group', 
        labels={'Parametro': 'Parámetro', 'Ponderacion Media': 'Ponderación Media'},

        #labels={'x': 'Parametro', 'y': 'Valorrr'}, 
        title='Analisis Valor de la Compañia'
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
                t=130,
            ),
            hovermode='x'
        )
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Valor')

    # Create the graph outside the app layout
    graph = dcc.Graph(
        id='valor_compania',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '400px'},  # Set graph width and height
    )

    return graph


### GERENCIA DE MARKETING


# 5 Nivel y Precios por compañia
def plot_Bebida_Precio_por_empresa(Bebida_type, graph_id_suffix):
    
    # New data based on the image provided (including companies)
    data = {
        "Pais": ["España", "España", "España", "Portugal", "Portugal", "Portugal", "Francia", "Francia", "Francia", 
                 "Italia", "Italia", "Italia", "Centro Europa", "Centro Europa", "Centro Europa", 
                 "Polonia", "Polonia", "Polonia", "Mexico", "Mexico", "Mexico"],
        "Bebida": ["Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", 
                   "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", 
                   "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos"],
        "GlobalBiz": [19, 28, 31, 19, 26, 31, 20, 28, 32, 22, 29, 36, 23, 3, 35, 22, 31, 36, 23, 31, 36],
        "FreshMarket": [17, 26, 3, 17, 25, 3, 20, 29, 35, 17, 26, 3, 17, 26, 3, 18, 27, 33, 17, 26, 30],
        "SparklingCo": [17, 24, 27, 17, 23, 27, 18, 27, 32, 17, 24, 27, 16, 24, 27, 16, 25, 3, 16, 24, 27],
        "QualityMax": [20, 27, 32, 19, 27, 34, 21, 28, 33, 22, 27, 32, 25, 30, 35, 25, 30, 35, 23, 28, 33],
        "Drink2Go": [25, 28, 29, 24, 28, 29, 27, 28, 3, 28, 31, 34, 28, 32, 32, 27, 32, 35, 32, 33, 38],
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)

    # Melt the DataFrame for Plotly
    df_melted = df.melt(id_vars=["Pais", "Bebida"], var_name="Compañía", value_name="Precio")

    # Filter DataFrame for the specified Bebida type
    df_filtered = df_melted[df_melted['Bebida'] == Bebida_type]

    # Create the Line Chart
    fig = px.line(df_filtered, x="Compañía", y="Precio", color="Pais", markers=True,
                  title=f"Precio por Pais y Compañía - {Bebida_type}",
                  labels={"Compañía": "Compañía", "Precio": "Precio Level", "Pais": "Pais"})


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
                t=130,
            ),
            #hovermode='x'
        )


    # Generar el gráfico con un ID único utilizando el sufijo proporcionado
    graph_id = f'Precio_de_bebidas_por_Pais_{graph_id_suffix}'
    graph = dcc.Graph(
        id=graph_id,
        config={'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height':'300px'},
    )
    return graph

# 6 Nivel de Precio drink2go 5 años
def plot_Bebida_Precio(Bebida_type, graph_id_suffix):

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


    # Generar el gráfico con un ID único utilizando el sufijo proporcionado
    graph_id = f'Precio_de_bebidas_por_Pais_{graph_id_suffix}'
    graph = dcc.Graph(
        id=graph_id,
        config={'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height':'300px'},
    )
    return graph


# 8 Graph Promocion Punto de venta por canal
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
    # Update layout
    fig.update_layout(
        title_text="Promocion punto de venta por Canal. Drink2Go", 
        showlegend=True,
        legend=dict(
                title_text='',
                orientation="v",
                entrywidth=40, 
                yanchor="bottom", 
                y=1.00, 
                xanchor="left", 
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


# 9 Unidades Vendidas por tipo de bebida y Año - FALTA

#10 Incentivo ventas 5 años
def plot_Incentivo_de_Ventas():
    
    # Data extracted from the table
    data = {
        "Producto": ["Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos"],
        "Año": [2027, 2027, 2027, 2028, 2028, 2028],
        "Ingresos": [10519803, 5061799, 4247517, 12402359, 5176663, 3938970],
        "% Incentivos": [93, 84, 78, 105, 100, 109],
        "Volumen Incentivos": [978342, 425191, 331306, 1302248, 517666, 429348]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)

    # Define colors for each product
    product_colors = {
        "Refrescos": "#636efb", 
        "Isotonicas": "#f0563b",  
        "Zumos": "#00cc96"       
    }
    
    # Create subplots for the three metrics: Ingresos, % Incentivos, and Volumen Incentivos
    fig = make_subplots(rows=1, cols=3, shared_xaxes=True, vertical_spacing=0.1,
                        subplot_titles=("Ingresos", "% Incentivos", "Volumen Incentivos"))


    # Plot for Ingresos (Bar chart with color depending on Producto)
    fig.add_trace(
        go.Bar(x=df['Producto'] + " " + df['Año'].astype(str), 
               y=df['Ingresos'], 
               name="Ingresos",
               marker_color=[product_colors[prod] for prod in df['Producto']]),  # Apply color based on Producto
        row=1, col=1
    )

    # Plot for % Incentivos (Bar chart with color depending on Producto)
    fig.add_trace(
        go.Bar(x=df['Producto'] + " " + df['Año'].astype(str), 
               y=df['% Incentivos'], 
               name="% Incentivos",
               marker_color=[product_colors[prod] for prod in df['Producto']]),  # Apply color based on Producto
        row=1, col=2
    )

    # Plot for Volumen Incentivos (Bar chart with color depending on Producto)
    fig.add_trace(
        go.Bar(x=df['Producto'] + " " + df['Año'].astype(str), 
               y=df['Volumen Incentivos'], 
               name="Volumen Incentivos",
               marker_color=[product_colors[prod] for prod in df['Producto']]),  # Apply color based on Producto
        row=1, col=3
    )


    # Update layout
    fig.update_layout(
        title_text="Incentivo de Ventas por Producto (Drink2Go)",
        height=400,
        showlegend=False,
        margin=dict(l=50, r=50, b=50, t=100),
        hovermode="x unified"
    )

    # Update axis labels
    fig.update_xaxes(title_text="Producto y Año", row=1, col=1)
    fig.update_yaxes(title_text="Ingresos", row=1, col=1)
    fig.update_yaxes(title_text="% Incentivos", row=1, col=2)
    fig.update_yaxes(title_text="Volumen Incentivos", row=1, col=3)

    # Generate the graph without a unique ID
    graph = dcc.Graph(
        config={'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height':'400px'},
    )
    return graph


# 11.	Nivel de precios 5 años todas las compañías y drink2go

def plot_Nivel_de_Precios():
    
    # Data from the table
    data = {
        "Pais": ["España", "España", "España", "Portugal", "Portugal", "Portugal", "Francia", "Francia", "Francia", 
                 "Italia", "Italia", "Italia", "Centro Europa", "Centro Europa", "Centro Europa", "Polonia", "Polonia", 
                 "Polonia", "Mexico", "Mexico", "Mexico"],
        "Producto": ["Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", 
                     "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", 
                     "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos"],
        "2027_GlobalBiz": [18, 28, 31, 18, 25, 32, 2, 28, 32, 22, 29, 36, 22, 3, 35, 22, 31, 36, 22, 31, 36],
        "2027_FreshMarket": [16, 25, 28, 16, 24, 28, 19, 28, 33, 16, 25, 28, 16, 25, 28, 17, 26, 31, 16, 25, 28],
        "2027_SparklingCo": [17, 24, 27, 17, 23, 27, 17, 25, 3, 17, 24, 27, 15, 24, 23, 16, 25, 3, 15, 24, 27],
        "2027_QualityMax": [2, 27, 32, 19, 27, 34, 21, 28, 33, 22, 27, 32, 25, 3, 35, 25, 3, 35, 23, 28, 33],
        "2027_Drink2Go": [2, 28, 3, 2, 28, 3, 23, 28, 32, 24, 3, 34, 28, 34, 35, 26, 32, 38, 3, 29, 5],
        "2028_GlobalBiz": [19, 28, 31, 19, 26, 31, 2, 28, 32, 22, 29, 36, 23, 3, 35, 22, 31, 36, 23, 31, 36],
        "2028_FreshMarket": [17, 26, 3, 17, 25, 3, 2, 29, 35, 17, 26, 3, 17, 26, 3, 18, 27, 33, 17, 26, 3],
        "2028_SparklingCo": [17, 24, 27, 17, 23, 27, 18, 27, 32, 17, 24, 27, 16, 24, 27, 16, 25, 3, 16, 24, 27],
        "2028_QualityMax": [2, 27, 32, 19, 27, 34, 21, 28, 33, 22, 27, 32, 25, 30, 35, 25, 30, 35, 23, 28, 33],
        "2028_Drink2Go": [25, 28, 29, 24, 28, 29, 27, 28, 3, 28, 31, 34, 28, 32, 32, 27, 32, 35, 32, 33, 38]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Melt the DataFrame to convert it into long format for Plotly Express
    df_melted = df.melt(id_vars=["Pais", "Producto"], var_name="Año_Compania", value_name="Precio")

    # Split 'Año_Compania' into separate columns for Year and Company
    df_melted[['Año', 'Compania']] = df_melted['Año_Compania'].str.split('_', expand=True)
    df_melted.drop(columns=['Año_Compania'], inplace=True)

    # Create the grouped bar chart using Plotly Express
    fig = px.bar(df_melted, x="Producto", y="Precio", color="Compania", barmode="group",
                 facet_col="Año", facet_row="Pais", title="Nivel de Precios por Compañía",
                 labels={"Precio": "Precio", "Producto": "Producto", "Compania": "Compañía"})

    fig.update_layout(
        height=1000,
        margin=dict(l=50, r=50, b=100, t=100),
    )

    # Return the graph as a dcc.Graph component
    graph = dcc.Graph(
        config={'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '700px'},
    )
    
    return graph




### GERENCIA DE PRODUCCION


# 12.	Nro de fabricas todas las compañías todos los años, evoluacion

def plot_numero_de_fabricas():
    # Data from the table (ignoring 'Allin One')
    data = {
        "Pais": ["España"] * 30 + ["Marruecos"] * 30 + ["Mexico"] * 30 + ["China"] * 30,
        "Año": [2023, 2023, 2023, 2023, 2023, 2024, 2024, 2024, 2024, 2024,
                2025, 2025, 2025, 2025, 2025, 2026, 2026, 2026, 2026, 2026,
                2027, 2027, 2027, 2027, 2027, 2028, 2028, 2028, 2028, 2028] * 4,
        "Compañía": ["GlobalBiz", "FreshMarket", "SparklingCo", "QualityMax", "Drink2Go"] * 6 * 4,
        "Numero de Fabricas": [2, 2, 2, 2, 2, 2, 2, 2, 3, 2,
                               2, 2, 2, 3, 2, 2, 2, 2, 3, 2,
                               2, 2, 2, 3, 2, 2, 2, 2, 3, 2,   # España
                               1, 1, 1, 1, 1, 1, 2, 2, 1, 1,
                               2, 2, 2, 1, 2, 2, 2, 2, 1, 2,
                               2, 2, 2, 1, 2, 2, 2, 2, 1, 2,   # Marruecos
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 1, 0, 0, 0, 1, 1, 0, 0, 0,
                               1, 1, 1, 0, 0, 1, 1, 1, 0, 0,   # Mexico
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                               0, 1, 0, 0, 0, 0, 1, 0, 0, 0]   # China
    }

    # Convert data into a DataFrame
    df = pd.DataFrame(data)

    # Create the line chart using Plotly Express
    fig = px.line(df, x="Año", y="Numero de Fabricas", color="Compañía", line_group="Compañía",
                  facet_row="Pais", markers=True, title="Número de Fábricas por Compañía y País")

    fig.update_layout(
        height=800,
        hovermode="x unified",
        margin=dict(l=50, r=50, t=100, b=50)
    )

    # Return the graph component
    return dcc.Graph(
        config={'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '700px'},
    )



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




# 3 Graphs for Incentivo de ventas por producto Drink2Go
def plot_incentivos(tipo_grafico, graph_id_suffix):
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

    graph_id = f'incentivo_de_ventas_{graph_id_suffix}_graph'
    graph = dcc.Graph(
        #id='incentivo_de_ventas_3_graphs',
        id=graph_id,
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
        title='Impacto de celebridades por mercado',
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
                b=40,
                l=0,
                r=0,
                t=130,
            ),
            #hovermode='x'
        )
    
    graph = dcc.Graph(
        id='impacto_celebridades',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height':'400px'},
    )
    return graph



####






#####



# 4 Graph Analisis Area de Produccion
def analisis_produccion():
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import pandas as pd

    # Create a dictionary to hold the data
    data = {
        "Year": [2027, 2028],
        "Refrescos_Total_Capacidad_Produccion": [6440000, 6608000],
        "Isotonicas_Total_Capacidad_Produccion": [2392000, 2454400],
        "Zumos_Total_Capacidad_Produccion": [1679000, 1722800],
        "Refrescos_Decision_Unidades_a_Producir": [7123800, 7251300],
        "Isotonicas_Decision_Unidades_a_Producir": [3920510, 4116535],
        "Zumos_Decision_Unidades_a_Producir": [2670550, 2804078],
        "Refrescos_Total_Unid_Producidas": [6193504, 6494808],
        "Isotonicas_Total_Unid_Producidas": [2392000, 2454400],
        "Zumos_Total_Unid_Producidas": [1679000, 1722800],
        "Refrescos_%_de_Ocupacion_Fabricas": [962, 983],
        "Isotonicas_%_de_Ocupacion_Fabricas": [1000, 1000],
        "Zumos_%_de_Ocupacion_Fabricas": [1000, 1000],
        # Add more data columns similarly
    }

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(data)

    # Define custom colors for each category
    colors = {
        "Refrescos": "#636efb",
        "Isotonicas": "#ef563b",
        "Zumos": "#05cc96"
    }

    # Create subplots
    fig = make_subplots(rows=1, cols=4, subplot_titles=("Total Capacidad Produccion", "Decision Unidades a Producir", "Total Unid. Producidas", "% de Ocupacion Fabricas"))


    # Add traces for each category
    for i, category in enumerate(colors):
        show_legend = i == 0  # Show legend only for the first trace
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Total_Capacidad_Produccion"], name=category, marker_color=colors[category], showlegend=False), row=1, col=1)
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Decision_Unidades_a_Producir"], name=category, marker_color=colors[category], showlegend=True), row=1, col=2)
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Total_Unid_Producidas"], name=category, marker_color=colors[category], showlegend=False), row=1, col=3)
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_%_de_Ocupacion_Fabricas"], name=category, marker_color=colors[category], showlegend=False), row=1, col=4)

    # Update layout
    fig.update_layout(
        title_text="Analisis del Area de Producción- Drink2Go", 
        showlegend=True,
        legend=dict(
                title_text='',
                orientation="v",
                entrywidth=40, 
                yanchor="bottom", 
                y=1.00, 
                xanchor="left", 
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
        )




    # Create the graph outside the app layout
    graph = dcc.Graph(
        id='analisis_produccion',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '300px'},  # Set graph width and height
    )

    return graph


# 3 Graph Analisis de Ventas e Inventario
def analisis_ventas_inventario():


    # Create a dictionary to hold the data
    data = {
        "Year": [2027, 2028],
        "Refrescos_Total_Unidades_Vendidas": [6029955, 6383706],
        "Isotonicas_Total_Unidades_Vendidas": [2393270, 2432002],
        "Zumos_Total_Unidades_Vendidas": [1723857, 1721926],
        "Refrescos_Unidades_Inventario": [830692, 941786],
        "Isotonicas_Unidades_Inventario": [173136, 195526],
        "Zumos_Unidades_Inventario": [124214, 125090],
        "Refrescos_%_de_Inventario_sobre_Ventas": [138, 148],
        "Isotonicas_%_de_Inventario_sobre_Ventas": [72, 80],
        "Zumos_%_de_Inventario_sobre_Ventas": [72, 73],
        # Add more data columns similarly
    }

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(data)

   # Define custom colors for each category
    colors = {
        "Refrescos": "#636efb",
        "Isotonicas": "#ef563b",
        "Zumos": "#05cc96"
    }

    # Create subplots
    fig = make_subplots(rows=1, cols=3, subplot_titles=("Total Unidades Vendidas", "Unidades Inventario", "% de Inventario sobre Ventas"))

    # Add traces for each category
    for i, category in enumerate(colors):
        show_legend = i == 0  # Show legend only for the first trace
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Total_Unidades_Vendidas"], name=category, marker_color=colors[category], showlegend=False), row=1, col=1)
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Unidades_Inventario"], name=category, marker_color=colors[category], showlegend=True), row=1, col=2)
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_%_de_Inventario_sobre_Ventas"], name=category, marker_color=colors[category], showlegend=False), row=1, col=3)

    # Update layout
    fig.update_layout(
        title_text="Analisis de Ventas e Inventario - Drink2Go", 
        showlegend=True,
        legend=dict(
                title_text='',
                orientation="v",
                entrywidth=40, 
                yanchor="bottom", 
                y=1.00, 
                xanchor="left", 
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
        ),

    # Create the graph outside the app layout
    graph = dcc.Graph(
        id='ventas_e_inventario',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '300px'},  # Set graph width and height
    )

    return graph


# 3 Graphs Analisis de Costos
def analisis_costos():

    # Create a dictionary to hold the data
    data = {
        "Year": [2027, 2028],
        "Refrescos_Coste_Unitario_de_Materia_Prima": [8, 8],
        "Isotonicas_Coste_Unitario_de_Materia_Prima": [14, 14],
        "Zumos_Coste_Unitario_de_Materia_Prima": [28, 28],
        "Refrescos_Coste_Unitario_de_Fabricacion": [13, 14],
        "Isotonicas_Coste_Unitario_de_Fabricacion": [28, 28],
        "Zumos_Coste_Unitario_de_Fabricacion": [48, 49],
        "Refrescos_Coste_Total_Fabricacion": [831.04, 815.845],
        "Isotonicas_Coste_Total_Fabricacion": [680.963, 682.014],
        "Zumos_Coste_Total_Fabricacion": [818.085, 844.986],
        # Add more data columns similarly
    }

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(data)

   # Define custom colors for each category
    colors = {
        "Refrescos": "#636efb",
        "Isotonicas": "#ef563b",
        "Zumos": "#05cc96"
    }

    # Create subplots
    fig = make_subplots(rows=1, cols=3, subplot_titles=("Coste Unitario de Materia Prima", "Coste Unitario de Fabricacion", "Coste Total Fabricacion"))

    # Add traces for each category
    for i, category in enumerate(colors):
        show_legend = i == 0  # Show legend only for the first trace
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Coste_Unitario_de_Materia_Prima"], name=category, marker_color=colors[category], showlegend=False), row=1, col=1)
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Coste_Unitario_de_Fabricacion"], name=category, marker_color=colors[category], showlegend=True), row=1, col=2)
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Coste_Total_Fabricacion"], name=category, marker_color=colors[category], showlegend=False), row=1, col=3)



    # Update layout
    fig.update_layout(
        title_text="Analisis de Costos de Produccion - Drink2Go", 
        showlegend=True,
        legend=dict(
                title_text='',
                orientation="v",
                entrywidth=40, 
                yanchor="bottom", 
                y=1.00, 
                xanchor="left", 
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
        ),

    # Create the graph outside the app layout
    graph = dcc.Graph(
        id='costos_produccion',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '300px'},  # Set graph width and height
    )

    return graph


# 4 Graphs Costo Logistica
def analisis_costo_logistica():
    # Create a dictionary to hold the data
    data = {
        "Year": [2027, 2028],
        "Refrescos_Coste_Almacenaje": [123002, 138915],
        "Isotonicas_Coste_Almacenaje": [139039, 141511],
        "Zumos_Coste_Almacenaje": [93953, 80536],
        "Refrescos_Coste_Transporte": [262229, 294954],
        "Isotonicas_Coste_Transporte": [116124, 108744],
        "Zumos_Coste_Transporte": [63222, 73174],
        "Refrescos_Coste_Distribucion": [422097, 446859],
        "Isotonicas_Coste_Distribucion": [119664, 121600],
        "Zumos_Coste_Distribucion": [103431, 103316],
        "Refrescos_Coste_Logistica_Total": [807328, 880728],
        "Isotonicas_Coste_Logistica_Total": [374827, 371855],
        "Zumos_Coste_Logistica_Total": [260606, 257025],
        # Add more data columns similarly
    }

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(data)

   # Define custom colors for each category
    colors = {
        "Refrescos": "#636efb",
        "Isotonicas": "#ef563b",
        "Zumos": "#05cc96"
    }

    # Create subplots
    fig = make_subplots(rows=1, cols=4, subplot_titles=("Coste Almacenaje", "Coste Transporte", "Coste Distribucion", "Coste Logistica Total"))

    # Add traces for each category
    for i, category in enumerate(colors):
        show_legend = i == 0  # Show legend only for the first trace
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Coste_Almacenaje"], name=category, marker_color=colors[category], showlegend=False), row=1, col=1)
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Coste_Transporte"], name=category, marker_color=colors[category], showlegend=True), row=1, col=2)
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Coste_Distribucion"], name=category, marker_color=colors[category], showlegend=False), row=1, col=3)
        fig.add_trace(go.Bar(x=df["Year"], y=df[f"{category}_Coste_Logistica_Total"], name=category, marker_color=colors[category], showlegend=False), row=1, col=4)

    # Update layout
    fig.update_layout(
        title_text="Analisis de Costos de Logistica - Drink2Go", 
        showlegend=True,
        legend=dict(
                title_text='',
                orientation="v",
                entrywidth=40, 
                yanchor="bottom", 
                y=1.00, 
                xanchor="left", 
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
        ),

    # Create the graph outside the app layout
    graph = dcc.Graph(
        id='costos_logistica',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '300px'},  # Set graph width and height
    )

    return graph

# 2 Graphs Ingresos totales por mercado y producto
def ingresos_totales():
    # Create a dictionary to hold the data
    data = {
        "Market": ["Espana", "Portugal", "Francia", "Italia", "Centro Europa", "Polonia", "Mexico", "Total ingresos"],
        "Refrescos_2028": [10580197, 2494104, 8687127, 16906666, 3007553, 7071705, 10359491, 59106840],
        "Isotonicas_2028": [3790728, 412517, 3256484, 11196107, 960933, 3787605, 5654902, 29059274],
        "Zumos_2028": [3557589, 795520, 1696616, 8556443, 531920, 2852573, 6548832, 24539492],
        "Refrescos_2027": [10605481, 2292670, 8231616, 17841302, 2061466, 5742097, 9466816, 56241448],
        "Isotonicas_2027": [3705810, 398376, 3250815, 12605335, 661279, 2774172, 5454364, 28850150],
        "Zumos_2027": [4001631, 859426, 1852396, 10097705, 171167, 1369002, 4874076, 23225402],
        "Variacion_2028": [51, 7, 57, 94, None, None, None, None],  # Variacion is not available for Total ingresos
        "Variacion_2027": [94, 80, 118, None, None, None, None, None]  # Variacion is not available for Total ingresos
    }

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(data)

    # Define custom colors for each product
    colors = {
        "Refrescos": "#636efb",
        "Isotonicas": "#ef563b",
        "Zumos": "#05cc96"
    }

    # Create subplots
    fig = make_subplots(rows=1, cols=2, subplot_titles=("2028", "2027"))

    # Add traces for each product in 2028
    for i, product in enumerate(colors):
        show_legend = i == 0  # Show legend only for the first product
        fig.add_trace(go.Bar(x=df["Market"], y=df[f"{product}_2028"], name=product, marker_color=colors[product], showlegend=False), row=1, col=1)

    # Add traces for each product in 2027
    for i, product in enumerate(colors):
        show_legend = i == 0  # Show legend only for the first product
        fig.add_trace(go.Bar(x=df["Market"], y=df[f"{product}_2027"], name=product, marker_color=colors[product], showlegend=True), row=1, col=2)

    # Update layout
    fig.update_layout(
        title_text="Ingresos Totales por Mercado y por Producto", 
        showlegend=True,
        legend=dict(
                title_text='',
                orientation="v",
                entrywidth=40, 
                yanchor="bottom", 
                y=1.00, 
                xanchor="left", 
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
        ),

    # Create the graph outside the app layout
    graph = dcc.Graph(
        id='ingresos_totales',
        config = {'displayModeBar': False},
        figure=fig,
        style={'width': '100%', 'height': '500px'},  # Set graph width and height
    )

    return graph


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
            html.Img(src = app.get_asset_url('logo_drink.png'),
                        style = {'height': '150px'},
                        className = 'title_image'
                        ),
                


        ], className='one-third column', id = 'title11'),

        #1.2 TITULO
        html.Div([
            html.H6('Cuadro de control - Drink2Go',
                        style = {'color': '#00002b'},
                        className = 'title'
                        
                        ),

        ], className='one-third column', id = 'title111')

    # FIN DE DIV 1  
        ], className = 'flex_container2'), 





    # NEW DIV ESCOGER GERENCIA
    html.Div([
        dcc.Dropdown(
            id='app-dropdown',
            options=[
                {'label': 'Gerencia General', 'value':'gerencia_general'},
                {'label': 'Gerencia Marketing y Ventas', 'value':'gerencia_marketing'},
                {'label': 'Gerencia de Produccion', 'value':'gerencia_produccion'},
                {'label': 'Gerencia Financera', 'value':'gerencia_financiera'}
            ],
            placeholder='Seleccionar Gerencia',
            value='gerencia_marketing'

        ),
        html.Div(id="graph-container"),
    ],
    style={"width": "100%"},
    ),

    html.Div(id='graph-container2', style={"margin-top": "20px"}),




    # Inicio DIV 2 - ROW 1
    html.Hr(className="my-4"),
    html.Div([
        #Column 1 - Row 1
        html.Div([
            # Titulo
            #html.Div("Valor de la Compañia", className="h6 text-center mt-4"),
            # Grafico
            html.Div([
                valor_de_la_compania_graph(df),

            ]),
            #html.Div([
                #html.Div('Valor de la Compañia', className="h6 mt-4"),
                #valor_de_la_compania_table(df),
            #])
        # Fin Column 1 - Row 1
        ], className="col"),

        # Column 2 - Row 1
        #html.Div([
            # Titulo
            #html.Div("Comparativa de Valor", className="h6 text-center mt-4"),
            # Grafico
         #   html.Div([
          #      comparativa_valor_compania_graph(df),

           # ]),
           # html.Div([
                #html.Div('Valor de la Compañia', className="h6 mt-4"),
                #valor_de_la_compania_table(df),
           # ])
        # Fin Column 2 - Row 1
        #], className="col"),


        # Column 3
         html.Div([
            # Titulo
            #html.Div("Impacto de las Celebredades por mercado", className="h6 text-center mt-4"),
            # Grafico
            html.Div([
                impacto_celebridades(),

            ]),
            html.Div([
                #html.Div('Valor de la Compañia', className="h6 mt-4"),
                #kpis_table(df),
                
            ])
        # Fin Column 3
        ], className="col"),
        
    
    # Fin Row 1    
    ], className="row row-cols-1 row-cols-sm-2 row-cols-md-3"),
    

    # INICIO ROW 2
    html.Hr(className="my-4"),
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
                    
                    plot_incentivos('porcentaje', '1'),  # Mostrar gráfico de porcentaje de incentivos
                    
                ], className="row"),
                html.Div([
                    #html.Div('Valor de la Compañia', className="h6 mt-4"),
                    #valor_de_la_compania_table(df),
                    plot_incentivos('volumen', '2')  
                ], className='row'),
                html.Div([
                    #html.Div('Valor de la Compañia', className="h6 mt-4"),
                    #valor_de_la_compania_table(df),
                    plot_incentivos('ingresos','3')  
                ], className='row'),

        ],className="h-100"),
        # Fin Column 1 - Row 2
        ], className="col-md-4"),

         # Fin Row 2    
    ], className="row row-cols-1 row-cols-sm-2 row-cols-md-2"),


    # INICIO ROW 3
    html.Hr(className="my-4"),
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
    html.Hr(className="my-4"),
    html.Div([
        # Column 1 - Row 4
        html.Div([
            # Grafico
            html.Div([
                plot_Bebida_Precio("Refrescos", '1'),
            ]),       
        ], className="col"),

        # Column 2 - Row 4
        html.Div([
            # Grafico
            html.Div([
                plot_Bebida_Precio("Isotonicas", '2'),
            ]),       
        ], className="col"),

        # Column 3 - Row 4
        html.Div([
            # Grafico
            html.Div([
                plot_Bebida_Precio("Zumos", '3'),
            ]),       
        ], className="col"),
    # Fin Row 4    
    ], className="row row-cols-1 row-cols-sm-2 row-cols-md-3"),
   
    # INICIO ROW 5
    html.Hr(className="my-4"),
    html.Div([
        # Column 1 - Row 5
        html.Div([
            # Grafico
            html.Div([
                analisis_produccion(),
            ]),       
        ], className="col"),
    #Fin Row 5
    ], className="row"),

    # INICIO ROW 6
    html.Hr(className="my-4"),
    html.Div([
        # Column 1 - Row 5
        html.Div([
            # Grafico
            html.Div([
                analisis_ventas_inventario(),
            ]),       
        ], className="col"),
    #Fin Row 5
    ], className="row"),

    # INICIO ROW 7
    html.Hr(className="my-4"),
    html.Div([
        # Column 1 - Row 5
        html.Div([
            # Grafico
            html.Div([
                analisis_costos(),
            ]),       
        ], className="col"),
    #Fin Row 6
    ], className="row"),


    # INICIO ROW 8
    html.Hr(className="my-4"),
    html.Div([
        # Column 1 - Row 5
        html.Div([
            # Grafico
            html.Div([
                analisis_costo_logistica(),
            ]),       
        ], className="col"),
    #Fin Row 7
    ], className="row"),

        # INICIO ROW 9
    html.Hr(className="my-4"),
    html.Div([
        # Column 1 - Row 5
        html.Div([
            # Grafico
            html.Div([
                ingresos_totales(),
            ]),       
        ], className="col"),
    #Fin Row 8
    ], className="row")

# Fin de div principal
], className="container mt-4")


##### CALLBACKS
@app.callback(
    Output('graph-container', 'children'),
    [Input('app-dropdown', 'value')]
)



def update_graph(selected_value):
    print(f"Dropdown selected: {selected_value}")  
    if selected_value == 'gerencia_general':
        


        return html.Div([
                    html.Div([
                        html.Div(kpis_table(df), className="col-6"),
                        html.Div(comparativa_valor_compania_graph(df), className="col-6"),
                        
                        ], className="row"),
                    html.Div([
                        html.Div(valor_de_la_compania_graph(df),className="col-6"),
                        html.Div(analisis_valor_de_la_compania(df), className="col-6")
                        ], className="row"),
                ])



   
    
    elif selected_value == 'gerencia_marketing':
        return html.Div([
                    html.Hr(className="my-4"),
                    html.Div([
                        # Column 1 - Row 4
                        html.Div([
                            # Grafico
                            html.Div([
                                plot_Bebida_Precio("Refrescos", '1'),
                            ]),       
                        ], className="col"),

                        # Column 2 - Row 4
                        html.Div([
                            # Grafico
                            html.Div([
                                plot_Bebida_Precio("Isotonicas", '2'),
                            ]),       
                        ], className="col"),

                        # Column 3 - Row 4
                        html.Div([
                            # Grafico
                            html.Div([
                                plot_Bebida_Precio("Zumos", '3'),
                            ]),       
                        ], className="col"),
                    # Fin Row 4    
                    ], className="row row-cols-1 row-cols-sm-2 row-cols-md-3"),
                
                    html.Hr(className="my-4"),
                    html.Div([
                        # Column 1 - Row 4
                        html.Div([
                            # Grafico
                            html.Div([
                                plot_Bebida_Precio_por_empresa("Refrescos", '1'),
                            ]),       
                        ], className="col"),

                        # Column 2 - Row 4
                        html.Div([
                            # Grafico
                            html.Div([
                                plot_Bebida_Precio_por_empresa("Isotonicas", '2'),
                            ]),       
                        ], className="col"),

                        # Column 3 - Row 4
                        html.Div([
                            # Grafico
                            html.Div([
                                plot_Bebida_Precio_por_empresa("Zumos", '3'),
                            ]),       
                        ], className="col"),
                    # Fin Row 4    
                    ], className="row row-cols-1 row-cols-sm-2 row-cols-md-3"),

                    html.Hr(className="my-4"),
                    html.Div([
                        html.Div([
                            promo_punto_de_venta_graph(),
                        ], className="col"),
                    ]),

                    html.Div([
                        html.Div([
                            plot_Incentivo_de_Ventas(),
                        ], className="col"),

                    ]), 

                    html.Div([
                        html.Div([
                            plot_Nivel_de_Precios(),
                        ], className="col"),

                    ]), 
                
                ])


    




    elif selected_value == 'gerencia_produccion':
        return plot_numero_de_fabricas()
    

    elif selected_value == 'gerencia_financiera':
        return promo_punto_de_venta_graph()
    else:
        # If no value is selected, return an empty container
        return html.Div("Seleccione un gráfico del menú desplegable.")



#INICIO DE APP

if __name__ == '__main__':
    app.run_server(debug=True)


