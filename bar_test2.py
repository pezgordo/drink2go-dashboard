
import plotly.graph_objects as go

import pandas as pd

# Load the Excel file
df = pd.read_excel('datos2.xlsx', header=None)

pais = df.iloc[42:63, 0].tolist()
categoria = df.iloc[42:63, 1].unique()
a_2023 = df.iloc[42:63, 7].tolist()
a_2024 = df.iloc[42:63, 6].tolist()
a_2025 = df.iloc[42:63, 5].tolist()
a_2026 = df.iloc[42:63, 4].tolist()
a_2027 = df.iloc[42:63, 3].tolist()
a_2028 = df.iloc[42:63, 2].tolist()

data = {
    'Pais': pais,
    'Categoria': categoria,
    '2023': a_2023,
    '2024': a_2024,
    '2025': a_2025,
    '2026': a_2026,
    '2027': a_2027,
    '2028': a_2028
}


result_df = pd.DataFrame(data)



fig = go.Figure()

fig.update_layout(
    template="simple_white",
    xaxis=dict(title_text="Año"),
    yaxis=dict(title_text="Precio"),
    barmode="stack",
)

colors = ["#2A66DE", "#FFC32B", "#334455"]

# Create stacked bar chart
for i in range(len(categoria)):
    fig.add_trace(go.Bar(
        x=result_df.columns[2:],  # Years as x-axis
        y=result_df[result_df['Categoria'] == categoria[i]].iloc[0, 2:],  # Values for each year
        name=categoria[i],  # Category as name
        marker_color=colors[i % len(colors)],  # Use modulo to repeat colors
        text=categoria[i],  # Display category name on hover
        hoverinfo='text+y',
    ))

fig.show()
