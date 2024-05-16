import pandas as pd
import plotly.express as px

# Data
data = {
    "Celebridad": ["Mensi", "Polinsky", "Romano", "Reno", "Shykira"],
    "España": [220, 130, 210, 160, 190],
    "Portugal": [160, 120, 230, 110, 200],
    "Francia": [140, 170, 160, 230, 260],
    "Italia": [190, 160, 180, 90, 150],
    "Centro Europa": [150, 170, 120, 110, 120],
    "Polonia": [120, 220, 100, 120, 110],
    "México": [220, 110, 180, 160, 170]
}

# Create DataFrame
df = pd.DataFrame(data)

# Melt DataFrame to long format
df_long = pd.melt(df, id_vars=['Celebridad'], var_name='Mercado', value_name='Impacto')

# Plot
fig = px.bar(df_long, x='Celebridad', y='Impacto', color='Mercado',
             title='Impacto de las celebridades por mercado',
             labels={'Impacto': 'Puntos adicionales en Valor de Marca', 'Celebridad': 'Celebridad'},
             barmode='group')

fig.update_layout(xaxis_title=None, yaxis_title=None)

fig.show()