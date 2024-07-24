import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from pathlib import Path

# Load data
current_dir = Path(__file__).resolve().parent
df = pd.read_csv(
    current_dir.parent / 'data' / 'customer_data_clustered.csv'
)

# Create a Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1('Customer Segmentation Dashboard'),

    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(df, x='TotalSpend', y='Frequency', color='Cluster',
                          title='Customer Segmentation')
    ),

    dcc.Graph(
        id='box-plot',
        figure=px.box(df, x='Cluster', y='TotalSpend', title='Spend Distribution by Cluster')
    ),

    dcc.Graph(
        id='histogram',
        figure=px.histogram(df, x='Recency', color='Cluster',
                            title='Recency Distribution by Cluster')
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
