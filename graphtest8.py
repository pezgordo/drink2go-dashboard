import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

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
    "Refrescos": "blue",
    "Isotonicas": "green",
    "Zumos": "orange"
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
fig.update_layout(title_text="Analysis of Costs - Drink2Go", showlegend=True)

# Show the plot
fig.show()
