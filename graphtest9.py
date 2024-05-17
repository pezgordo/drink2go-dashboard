import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

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
    "Refrescos": "blue",
    "Isotonicas": "green",
    "Zumos": "orange"
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
fig.update_layout(title_text="Analysis of Costs - Drink2Go", showlegend=True)

# Show the plot
fig.show()
