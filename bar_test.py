import numpy as np
import pandas as pd
import plotly.graph_objects as go


# Create dummy data indexed by month and with multi-columns [product, revenue]
index = pd.date_range("2020-01-01", "2020-12-01", freq="MS")
df = pd.concat(
    [
        pd.DataFrame(
            np.random.rand(12, 3) * 1.25 + 0.25,
            index=index,
            columns=["Revenue1", "Revenue2", "Revenue3"]
        ),
        pd.DataFrame(
            np.random.rand(12, 3) + 0.5,
            index=index,
            columns=["Revenue1", "Revenue2", "Revenue3"]
        ),
    ],
    axis=1,
    keys=["Product1", "Product2"]
)

# Create a figure with the right layout
fig = go.Figure(
    layout=go.Layout(
        height=600,
        width=1000,
        barmode="relative",
        yaxis_showticklabels=False,
        yaxis_showgrid=False,
        yaxis_range=[0, df.groupby(axis=1, level=0).sum().max().max() * 1.5],
       # Secondary y-axis overlayed on the primary one and not visible
        yaxis2=go.layout.YAxis(
            visible=False,
            matches="y",
            overlaying="y",
            anchor="x",
        ),
        font=dict(size=24),
        legend_x=0,
        legend_y=1,
        legend_orientation="h",
        hovermode="x",
        margin=dict(b=0,t=10,l=0,r=10)
    )
)

# Define some colors for the product, revenue pairs
colors = {
    "Product1": {
        "Revenue1": "#F28F1D",
        "Revenue2": "#F6C619",
        "Revenue3": "#FADD75",
    },
    "Product2": {
        "Revenue1": "#2B6045",
        "Revenue2": "#5EB88A",
        "Revenue3": "#9ED4B9",
    },
    "Product3": {
        "Revenue1": "#244445",
        "Revenue2": "#66688A",
        "Revenue3": "#988789",
    },
    "Product4": {
        "Revenue1": "#98745",
        "Revenue2": "#765456",
        "Revenue3": "#876577",
    }
}

# Add the traces
for i, t in enumerate(colors):
    for j, col in enumerate(df[t].columns):
        if (df[t][col] == 0).all():
            continue
        fig.add_bar(
            x=df.index,
            y=df[t][col],
            # Set the right yaxis depending on the selected product (from enumerate)
            yaxis=f"y{i + 1}",
            # Offset the bar trace, offset needs to match the width
            # The values here are in milliseconds, 1billion ms is ~1/3 month
            offsetgroup=str(i),
            offset=(i - 1) * 1000000000,
            width=1000000000,
            legendgroup=t,
            legendgrouptitle_text=t,
            name=col,
            marker_color=colors[t][col],
            marker_line=dict(width=2, color="#333"),
            hovertemplate="%{y}<extra></extra>"
        )

fig.show()