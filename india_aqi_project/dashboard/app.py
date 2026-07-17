import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

DF = pd.read_csv('data/india_aqi_daily.csv', parse_dates=['date'])
DF['month_dt'] = DF['date'].dt.to_period('M').dt.to_timestamp()

app = Dash(__name__)
app.title = 'India AQI Analysis Dashboard'

cities = sorted(DF['city'].unique())
years = sorted(DF['year'].unique())

app.layout = html.Div([
    html.H1('India Air Quality (AQI) Analysis Dashboard'),
    html.Div('Interactive dashboard for city trends, pollution categories, and pollutant patterns across India.'),
    html.Div([
        html.Div([html.Label('City'), dcc.Dropdown(cities, cities[0], id='city')], style={'width':'30%', 'display':'inline-block', 'padding':'10px'}),
        html.Div([html.Label('Year'), dcc.Dropdown(years, years[-1], id='year')], style={'width':'20%', 'display':'inline-block', 'padding':'10px'}),
        html.Div([html.Label('Metric'), dcc.Dropdown(['aqi', 'pm25', 'pm10', 'no2', 'so2', 'co'], 'aqi', id='metric')], style={'width':'20%', 'display':'inline-block', 'padding':'10px'})
    ]),
    html.Div(id='kpis', style={'display':'flex', 'gap':'20px', 'padding':'10px 0'}),
    dcc.Graph(id='trend'),
    dcc.Graph(id='category'),
    dcc.Graph(id='top_cities')
], style={'fontFamily':'Arial', 'maxWidth':'1200px', 'margin':'0 auto'})

@app.callback(
    Output('kpis', 'children'),
    Output('trend', 'figure'),
    Output('category', 'figure'),
    Output('top_cities', 'figure'),
    Input('city', 'value'),
    Input('year', 'value'),
    Input('metric', 'value')
)
def update(city, year, metric):
    filtered = DF[(DF['city'] == city) & (DF['year'] == year)].copy()
    yearly = DF[DF['year'] == year]
    kpi_data = [
        ('Avg AQI', round(filtered['aqi'].mean(), 1)),
        ('High AQI Days', int((filtered['aqi'] > 200).sum())),
        ('Best City Avg AQI', round(yearly.groupby('city')['aqi'].mean().min(), 1))
    ]
    kpis = [html.Div([html.H3(label), html.H2(str(value))], style={'background':'#f7f7f7', 'padding':'15px', 'borderRadius':'10px', 'flex':'1'}) for label, value in kpi_data]

    trend_fig = px.line(filtered.sort_values('date'), x='date', y='aqi', title=f'{city} Daily AQI in {year}')
    category_fig = px.pie(filtered, names='category', title=f'{city} AQI Category Share in {year}')
    top = yearly.groupby('city', as_index=False)['aqi'].mean().sort_values('aqi', ascending=False)
    top_fig = px.bar(top, x='city', y='aqi', title=f'Average AQI by City in {year}')
    return kpis, trend_fig, category_fig, top_fig

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
