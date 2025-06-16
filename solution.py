from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

ordered_items = pd.read_csv("notebook-2/chipotle.csv")
ordered_items["item_price"] = ordered_items["item_price"].apply(lambda price: float(price.strip("$")))
item_revenue = ordered_items.groupby("item_name")["item_price"].sum()
top_5 = item_revenue.nlargest(5)
print(top_5)

pie_figure = px.pie(
  top_5,
  values="item_price",
  names=top_5.index,
)

bar_figure = px.bar(
  top_5,
  x=top_5.index,
  y="item_price",
)

bar_h_figure = px.bar(
  top_5,
  x="item_price",
  y=top_5.index,
  orientation="h",
)

scatter_figure = px.scatter(
  top_5,
  x=top_5.index,
  y="item_price",
  color="item_price",
  size="item_price",
)

app = Dash(external_stylesheets=[dbc.themes.COSMO])
app.layout = dbc.Container([
  dbc.Row([
    dbc.Col(dcc.Graph(figure=pie_figure), xl=6),
    dbc.Col(dcc.Graph(figure=bar_figure), xl=6),
  ]),

  dbc.Row([
    dbc.Col(dcc.Graph(figure=bar_h_figure), xl=6),
    dbc.Col(dcc.Graph(figure=scatter_figure), xl=6),
  ]),
])

app.run(debug=True)