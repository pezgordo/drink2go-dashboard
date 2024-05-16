
import pandas as pd
import plotly.graph_objects as go
df = pd.DataFrame(
    dict(
        week=[1, 1, 2, 2, 3, 3] * 2,
        layout=["classic", "classic", "modern", "modern"] * 3,
        response=["conversion", "exit"] * 6,
        cnt=[26, 23, 45, 34, 55, 44, 53, 27, 28, 25, 30, 34],
    )
)




fig = go.Figure()

fig.update_layout(
    template="simple_white",
    xaxis=dict(title_text="Week"),
    yaxis=dict(title_text="Count"),
    barmode="stack",
)

colors = ["#2A66DE", "#FFC32B"]

"""
for r, c in zip(df.response.unique(), colors):
    plot_df = df[df.response == r]
    fig.add_trace(
        go.Bar(
            x=[plot_df.week, plot_df.layout], 
            y=plot_df.cnt, 
            name=r, 
            marker_color=c),
    )
"""


for r in zip(df.response.unique()):
    for c in zip(colors):
        plot_df = df[df.response == r]
        fig.add_trace(
            go.Bar(
                x=[plot_df.week, plot_df.layout], 
                y=plot_df.cnt, 
                name=r, 
                marker_color=c
            ),
        )

fig.show()