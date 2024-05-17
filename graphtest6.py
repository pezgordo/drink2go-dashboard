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
    "Refrescos": "blue",
    "Isotonicas": "green",
    "Zumos": "orange"
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
fig.update_layout(title_text="Analisis del Area de Producción- Drink2Go", showlegend=True)

# Show the plot
fig.show()