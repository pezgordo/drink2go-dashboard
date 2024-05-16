import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Bar(
  x = [['First', 'First', 'Second', 'Second'],
       ["A", "B", "A", "B"]],
  y = [2, 3, 1, 5],
  name = "Adults",
))

fig.add_trace(go.Bar(
  x = [['First', 'First', 'Second', 'Second'],
       ["A", "B", "A", "B"]],
  y = [8, 3, 6, 5],
  name = "Children",
))

fig.update_layout(title_text="Multi-category axis", barmode="stack")

fig.show()