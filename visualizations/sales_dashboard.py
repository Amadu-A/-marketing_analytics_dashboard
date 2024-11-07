import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

from scripts.dashboard import load_data, preprocess_data, aggregate_data

# from scripts.dashboard import load_data, preprocess_data, aggregate_data

# Загружаем и обрабатываем данные
web_data = load_data('data/raw_data/web_sales.csv')
mobile_data = load_data('data/raw_data/mobile_sales.csv')
offline_data = load_data('data/raw_data/offline_sales.csv')

# Объединяем данные из всех каналов
all_data = pd.concat([web_data, mobile_data, offline_data])
all_data = preprocess_data(all_data)
aggregated_data = aggregate_data(all_data)

# Создаем дашборд с использованием Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Маркетинговая аналитика продаж"),
    dcc.Dropdown(
        id="channel-dropdown",
        options=[
            {"label": "Web", "value": "web"},
            {"label": "Mobile", "value": "mobile"},
            {"label": "Offline", "value": "offline"}
        ],
        value="web"
    ),
    dcc.Graph(id="revenue-chart"),
])

@app.callback(
    Output("revenue-chart", "figure"),
    Input("channel-dropdown", "value")
)
def update_chart(channel):
    filtered_data = aggregated_data[aggregated_data["channel"] == channel]
    fig = px.line(filtered_data, x="date", y="total_revenue", title=f"Выручка по каналу: {channel}")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
