import plotly.graph_objects as go
import pandas as pd

# Load the Excel file
df = pd.read_excel('datos2.xlsx', header=None)

# Extracting data
pais = df.iloc[42:63, 0].to_list()
categorias = df.iloc[42:63, 1].tolist()
years = df.iloc[41, 2:].tolist()
a_2023 = df.iloc[42:63, 7].tolist()
a_2024 = df.iloc[42:63, 6].tolist()
a_2025 = df.iloc[42:63, 5].tolist()
a_2026 = df.iloc[42:63, 4].tolist()
a_2027 = df.iloc[42:63, 3].tolist()
a_2028 = df.iloc[42:63, 2].tolist()
years += [None] * (21 - len(years))

df2 = pd.DataFrame({
    'Pais': pais,
    'Categorias': categorias,
    'Years': years,
    'a_2023': a_2023,
    '2024': a_2024,
    '2025': a_2025,
    '2026': a_2026,
    '2027': a_2027,
    '2028': a_2028,
})







fig = go.Figure()

fig.update_layout(
    template="simple_white",
    xaxis=dict(title_text="Año"),
    yaxis=dict(title_text="Precio"),
    barmode="stack",
)

colors = ["#2A66DE", "#FFC32B", "#334455"]  # Choose colors for the bars


for categoria, color in zip(df2.Categorias.unique(), colors):
    plot_df = df2[df2.Categorias == categoria]
    fig.add_trace(
        go.Bar(
            x=[plot_df.Years, plot_df.Pais],
            y=plot_df.a_2023,
            name=categoria,
            marker_color=color),
    )

fig.show()