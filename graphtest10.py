import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

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
    "Refrescos": "blue",
    "Isotonicas": "green",
    "Zumos": "orange"
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
fig.update_layout(title_text="Ingresos totales por mercado y producto", barmode="group")

# Show the plot
fig.show()
