import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

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
    "Refrescos": "blue",
    "Isotonicas": "green",
    "Zumos": "orange"
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
fig.update_layout(title_text="Analysis of Sales and Inventory - Drink2Go", showlegend=True)

# Show the plot
fig.show()
