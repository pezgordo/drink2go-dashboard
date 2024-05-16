import plotly.graph_objects as go
import pandas as pd

# Load the Excel file
df = pd.read_excel('datos2.xlsx', header=None)

# Extracting data
pais = df.iloc[42:63, 0].unique()
categorias = df.iloc[42:63, 1].unique()
years = df.iloc[41, 2:].tolist()

# Dictionary to hold data for each category and pais
data = {}
for categoria in categorias:
    data[categoria] = df[df[1] == categoria].iloc[:, 2:].values.T.tolist()

fig = go.Figure()

fig.update_layout(
    template="simple_white",
    xaxis=dict(title_text="Año"),
    yaxis=dict(title_text="Precio"),
    barmode="stack",
)

colors = ["#2A66DE", "#FFC32B", "#334455"]  # Choose colors for the bars

# Create stacked bar chart for each category and pais
for categoria, color in zip(categorias, colors):
    for i, pais_data in enumerate(data[categoria]):
        if i < len(pais):  # Ensure the index is within bounds
            fig.add_trace(go.Bar(
                x=years,
                y=pais_data,
                name=f"{categoria} - {pais[i]}",
                marker_color=color,
                text=f"{categoria} - {pais[i]}",
                hoverinfo='text+y',
            ))

fig.show()