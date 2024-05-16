import plotly.express as px
import pandas as pd

# Crear el DataFrame con los datos
data = {
    "Producto": ["Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos"],
    "Año": [2028]*3 + [2027]*3,
    "Ingresos": [12402359, 5176663, 3938970, 10519803, 5061799, 4247517],
    "% Incentivos": [105, 100, 109, 93, 84, 78],
    "Volumen Incentivos": [1302248, 517666, 429348, 978342, 425191, 331306]
}

df = pd.DataFrame(data)

# Grafico de barras apiladas
fig = px.bar(df, x="Año", y="Ingresos", color="Producto",
             title="Incentivo de ventas por producto - Drink2Go",
             labels={"Ingresos": "Ingresos ($)"},
             barmode="group")
# Gráfico de barras para % de incentivos
fig1 = px.bar(df, x="Año", y="% Incentivos", color="Producto",
              title="Porcentaje de incentivos por producto - Drink2Go",
              labels={"% Incentivos": "Porcentaje de incentivos (%)"},
              barmode="group")

# Gráfico de barras para volumen de incentivos
fig2 = px.bar(df, x="Año", y="Volumen Incentivos", color="Producto",
              title="Volumen de incentivos por producto - Drink2Go",
              labels={"Volumen Incentivos": "Volumen de incentivos"},
              barmode="group")
fig.show()
fig1.show()
fig2.show()