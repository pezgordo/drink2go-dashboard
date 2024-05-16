import plotly.graph_objects as go
import pandas as pd

# Load the Excel file
df = pd.read_excel('datos2.xlsx', header=None)

# Extracting data
pais = df.iloc[42:63, 0].to_list
categorias = df.iloc[42:63, 1].tolist()
#years = [2023, 2024, 2025, 2026, 2027, 2028] * 6,
years = df.iloc[41, 2:].tolist()
a_2023 = df.iloc[42:63, 7].tolist()
a_2024 = df.iloc[42:63, 6].tolist()
a_2025 = df.iloc[42:63, 5].tolist()
a_2026 = df.iloc[42:63, 4].tolist()
a_2027 = df.iloc[42:63, 3].tolist()
a_2028 = df.iloc[42:63, 2].tolist()

years += [None] * (21 - len(years))

# Check the lengths and truncate if needed
#min_length = min(len(years), len(a_2023), len(a_2024), len(a_2025), len(a_2026), len(a_2027), len(a_2028))
#years = years[:min_length]
#categorias = categorias[:min_length]
#pais = pais[:min_length]
#a_2023 = a_2023[:min_length]
#a_2024 = a_2024[:min_length]
#a_2025 = a_2025[:min_length]
#a_2026 = a_2026[:min_length]
#a_2027 = a_2027[:min_length]
#a_2028 = a_2028[:min_length]

# Dictionary to hold data for each category and pais
data = {
    'Pais': pais,
    'Categorias': categorias,
    'years': years,
    'a_2023': a_2023,
    'a_2024': a_2024,
    'a_2025': a_2025,
    'a_2026': a_2026,
    'a_2027': a_2027,
    'a_2028': a_2028
}
#for categoria in categorias:
#    data[categoria] = df[df[1] == categoria].iloc[:, 2:].values.T.tolist()

result_df = pd.DataFrame(data)

fig = go.Figure()

fig.update_layout(
    template="simple_white",
    xaxis=dict(title_text="Año"),
    yaxis=dict(title_text="Precio"),
    barmode="stack",
)

colors = ["#2A66DE", "#FFC32B", "#334455"]  # Choose colors for the bars

#pais_list = pais.tolist()  # Convert pais to a list

for categoria, color in zip(result_df.Categorias.unique(), colors):
    plot_df = result_df[result_df.Categorias == categoria]
    fig.add_trace(
        go.Bar(
            x=[plot_df.years, plot_df.Pais],
            y=plot_df.a_2023,
            name=categoria,
            marker_color=color),
    )

fig.show()
