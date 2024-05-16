import plotly.graph_objects as go
import pandas as pd

# Data
"""
data = {
    'Country': ['Spain','Portugal', 'France', 'Italy', 'Central Europe', 'Poland','Mexico'] * 3,
    'Category': ['Sodas', 'Isotonics', 'Juices'] * 7,
    '2028': [25, 28, 29, 24, 28, 29, 27, 28, 3, 28, 31, 34, 28, 32, 32, 27, 32, 35, 32, 33, 38],
    '2027': [2, 28, 3, 2, 28, 3, 23, 28, 32, 24, 3, 34, 28, 34, 35, 26, 32, 38, 3, 29, 5],
    '2026': [2, 28, 35, 2, 28, 36, 25, 3, 38, 3, 4, 56, 0, 0, 0, 24, 28, 35, 3, 4, 5],
    '2025': [2, 28, 35, 2, 28, 36, 25, 3, 38, 24, 36, 45, 0, 0, 0, 0, 0, 0, 24, 36, 45],
    '2024': [16, 24, 3, 16, 23, 31, 18, 26, 34, 16, 24, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    '2023': [12, 18, 22, 11, 17, 23, 13, 19, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
"""
df2 = pd.DataFrame(
    dict(
        Country=['Spain','Portugal', 'France', 'Italy', 'Central Europe', 'Poland','Mexico'] * 6,
        Category=['Sodas', 'Isotonics', 'Juices'] * 14,
    )
)



Country2=['Spain', 'Spain', 'Spain', 'Portugal', 'Portugal', 'Portugal'] * 7,

df = pd.DataFrame(
    dict(
        Country=['Spain','Portugal', 'France', 'Italy', 'Central Europe', 'Poland','Mexico'] * 3,
        #Country=['Spain','Portugal', 'France'] * 7,
        #Country=['Spain', 'Spain', 'Spain', 'Portugal', 'Portugal', 'Portugal'] * 7,
        #Country_2=['Italy', 'Central Europe', 'Poland'] * 7,
        #Country=['Spain', 'Spain', 'Spain', 'Portugal', 'Portugal', 'Portugal', 'France', 'France', 'France', 'Italy', 'Italy', 'Italy', 'Central Europe', 'Central Europe', 'Central Europe', 'Poland', 'Poland', 'Poland', 'Mexico', 'Mexico', 'Mexico'],
        #Category=['Sodas', 'Sodas', 'Sodas', 'Sodas', 'Sodas', 'Sodas', 'Sodas', 'Isotonics', 'Isotonics', 'Isotonics', 'Isotonics', 'Isotonics', 'Isotonics', 'Isotonics', 'Juices', 'Juices', 'Juices', 'Juices', 'Juices', 'Juices', 'Juices'],
        Category=['Sodas', 'Isotonics', 'Juices'] * 7,
        a2028=[25, 28, 29, 24, 28, 29, 27, 28, 3, 28, 31, 34, 28, 32, 32, 27, 32, 35, 32, 33, 38],
        a2027=[2, 28, 3, 2, 28, 3, 23, 28, 32, 24, 3, 34, 28, 34, 35, 26, 32, 38, 3, 29, 5],
        a2026=[2, 28, 35, 2, 28, 36, 25, 3, 38, 3, 4, 56, 0, 0, 0, 24, 28, 35, 3, 4, 5],
        a2025=[2, 28, 35, 2, 28, 36, 25, 3, 38, 24, 36, 45, 0, 0, 0, 0, 0, 0, 24, 36, 45],
        a2024=[16, 24, 3, 16, 23, 31, 18, 26, 34, 16, 24, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        a2023=[12, 18, 22, 11, 17, 23, 13, 19, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )
)
# Create DataFrame
#df = pd.DataFrame(data)

# Plotly
fig = go.Figure()

fig.update_layout(
    template="simple_white",
    xaxis=dict(title_text="Ano"),
    yaxis=dict(title_text="Valor"),
    barmode="stack",
)

#colors = ["#2A66DE","#2A66DE","#2A66DE", "#2A66DE","#2A66DE","#2A66DE","#2A66DE", "#FFC32B", "#FFC32B", "#FFC32B", "#FFC32B", "#FFC32B", "#FFC32B", "#FFC32B", "#FF3344","#FF3344","#FF3344", "#FF3344","#FF3344","#FF3344", "#FF3344"]
#colors = ["#2A66DE", "#FFC32B", "#FF3344"]
colors = ["#2A66DE", "#FFC32B", "#FF3344", "#5A676E", "#89C123", "#F65444", "#9365DE"]
#colors = ["#2A66DE", "#FFC32B", "#FF3344", "#2A66DE", "#FFC32B", "#FF3344", "#2A66DE", "#FFC32B", "#FF3344", "#2A66DE", "#FFC32B", "#FF3344", "#2A66DE", "#FFC32B", "#FF3344"]
#colors = ["#2A66DE", "#FFC32B", "#FF3344", "#2A777E", "#FF1212", "#FF7654", "#FF3111", "#F76542", "#456654", "#235411"]
"""
for categoria, color in zip(df.Categorias.unique(), colors):
    #temp_df = df[(df['Categoria'] == categoria) & (df['Pais'] == pais)]
    #temp_df = df[(df['Categorias'] == categoria)]
    temp_df = df[(df['Categorias'] == categoria) & (df['Pais'] == pais)]

    plot_df = df[df.Categorias == categoria]
    fig.add_trace(
        go.Bar(
            #x=[plot_df.Years, plot_df.Pais],
            #y=temp_df.columns[2:],
            x=temp_df.columns[2:],
            y=temp_df.iloc[0, 2:],
            name=categoria,
            marker_color=color),
    )
"""

"""
for category in df['Category'].unique():
    for color in colors:
        for country in df['Country'].unique():
            temp_df = df[(df['Category'] == category) & (df['Country'] == country)]
            fig.add_trace(go.Bar(
                x=[temp_df.columns[2:], df.Country],
                y=temp_df.iloc[0, 2:],
                name=f"{country} - {category}"
            ))
"""

"""
for country, color in zip(df.Country, colors):
    plot_df = df[df.Country == country]
    fig.add_trace(
        go.Bar(
        #x=[plot_df.columns[2:], plot_df.Country],
        x=[plot_df.columns[2:], plot_df.Category],
        y=plot_df.iloc[0, 2:],
        name=country,
        marker_color=color,
    ))
    """
"""
for  country, category, color in zip(df.Country, df.Category, colors):
    plot_df = df[df.Category == category]
    fig.add_trace(
        go.Bar(
        x=[plot_df.columns[2:], plot_df.Country],
        #x=[plot_df.columns[2:], plot_df.Country, plot_df.Category],
        y=plot_df.iloc[0, 2:],
        name=category,
        marker_color=color,
    ))

"""
""""
for  country, color, category in zip(df.Country.unique(), colors, df.Category):
    for category in (df.Category):
        plot_df = df[df.Category == category]
        fig.add_trace(
            go.Bar(
            x=[plot_df.columns[2:], plot_df.Country],
            #x=[plot_df.columns[2:], plot_df.Country, plot_df.Category],
            y=plot_df.iloc[0, 2:],
            name=category,
            marker_color=color,
    ))
"""
for  country , color in zip(df2.Country, colors):
#for color in colors:
#for category in zip(df.Category.unique()):
        
            plot_df = df[df.Country == country]
            fig.add_trace(
                go.Bar(
                x=[plot_df.columns[2:], plot_df.Country],
                #x=[plot_df.columns[2:], plot_df.Country, plot_df.Category],
                y=plot_df.iloc[0, 2:],
                name=country,
                #marker_color=color,
    
    ))
            print(plot_df.iloc[0, 2:])
            print([plot_df.columns[2:], plot_df.Country])

"""
fig.update_layout(
    template="simple_white",
    xaxis=dict(title_text="Year"),
    yaxis=dict(title_text="Price"),
    barmode="stack",
    #legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
"""

fig.show()