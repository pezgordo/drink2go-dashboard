import plotly.express as px
import pandas as pd

# Create a DataFrame with the provided data
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

# Sorting the DataFrame by Año and Categoria
df_combined_sorted = df_combined.sort_values(by=['Pais', 'Categoria'])


# Define the color sequence
color_sequence = px.colors.qualitative.Plotly

# Plotting using Plotly Express
fig = px.bar(df_combined, 
                   x='Categoria',
                   y='Valor', 
                   color='Año', 
                   facet_col='Pais',
                   #barmode='group',
                   category_orders={"Categoria": ["Tienda_Tradicional_2027", "Tienda_Tradicional_2028", "Gran_Superficie_2027", "Gran_Superficie_2028", "Hosteleria_2027", "Hosteleria_2028"]},
                   #category_orders={"Categoria": ["Tienda_Tradicional_2027", "Gran_Superficie_2027", "Hosteleria_2027", "Tienda_Tradicional_2028", "Gran_Superficie_2028", "Hosteleria_2028"]},

                   labels={'Valor': 'Valor', 'Categoria': '', 'Año': 'Año'},
                   title='Promocion punto de venta por Canal. Drink2Go'
                  )
fig.show()



