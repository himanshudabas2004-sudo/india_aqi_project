[README (1).md](https://github.com/user-attachments/files/30113377/README.1.md)

# India Air Quality (AQI) Analysis Dashboard

## Project Overview

The **India Air Quality (AQI) Analysis Dashboard** is a data analysis project focused on studying air pollution patterns across major Indian cities. The project uses daily AQI and pollutant-level data to explore how air quality changes over time, compare cities, and identify periods of higher pollution.

This project was built as a student-friendly data analytics portfolio project to demonstrate skills in **data cleaning, exploratory data analysis, visualization, and interactive dashboard creation**.

## Objective

The main goal of this project is to analyze air quality trends in India and present the findings in a clear and interactive way. The dashboard helps answer questions such as:

- Which cities have the highest average AQI?
- How does AQI change over time in a selected city?
- How often do cities fall into unhealthy pollution categories?
- What is the distribution of major pollutants like PM2.5, PM10, NO2, SO2, and CO?

## Dataset

This project uses a daily AQI dataset containing information for major Indian cities. The dataset includes:

- `date`
- `city`
- `state`
- `aqi`
- `pm25`
- `pm10`
- `no2`
- `so2`
- `co`
- `category`

The AQI values are grouped into standard pollution categories such as:

- **Good**
- **Satisfactory**
- **Moderate**
- **Poor**
- **Very Poor**

## Tools and Technologies Used

This project was developed using:

- **Python**
- **Pandas**
- **Plotly**
- **Dash**

## Dashboards

### 1. Overview Dashboard

This dashboard gives a high-level summary of air quality conditions across major Indian cities. It includes average AQI by city, number of high pollution days, AQI category distribution, and quick comparison across selected years. This view is useful for getting a broad understanding of overall pollution patterns.

### 2. City Trend Dashboard

This dashboard focuses on one selected city and shows how AQI changes over time. It includes a daily AQI line chart, monthly or yearly trend view, pollutant behavior for the selected city, and AQI category breakdown for the city. This helps users study seasonal changes and pollution spikes in a specific location.

### 3. Pollutant Analysis Dashboard

This dashboard is designed to compare key pollutants such as PM2.5, PM10, NO2, SO2, and CO. It helps identify which pollutants contribute most to poor air quality and how pollutant levels vary across cities.

### 4. City Comparison Dashboard

This dashboard compares multiple cities side by side. It includes average AQI ranking, pollution category comparison, city-wise pollutant summaries, and best and worst performing cities. This is useful for identifying cities with cleaner or more polluted air.

### 5. Seasonal Trends Dashboard

This dashboard highlights how AQI changes across months and seasons. It includes monthly AQI trends, seasonal pollution spikes, yearly AQI variation, and recurring pollution patterns. This helps show how weather and seasonality may affect air quality.

## Features

The dashboard includes the following features:

- Daily AQI trend visualization for a selected city
- AQI category breakdown using a pie chart
- City-wise AQI comparison for a selected year
- Pollutant indicators for PM2.5, PM10, NO2, SO2, and CO
- Interactive filters for city, year, and metric selection
- Multiple dashboard views for different types of analysis

## Project Structure

```bash
india_aqi_project/
├── data/
│   └── india_aqi_daily.csv
├── dashboard/
│   └── app.py
├── assets/
├── README.md
└── requirements.txt
```

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/india-aqi-analysis-dashboard.git
cd india-aqi-analysis-dashboard
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the dashboard
```bash
python dashboard/app.py
```

### 4. Open the dashboard
After starting the app, open your browser and go to:

```bash
http://127.0.0.1:8050
```

## Key Insights

The dashboard can help users identify cities with consistently high AQI, seasonal pollution patterns, cities with more frequent unhealthy air quality levels, and differences in pollutant concentration across locations.

## Learning Outcomes

This project demonstrates data analysis with **Pandas**, data visualization with **Plotly**, interactive dashboard development with **Dash**, and organization of a complete end-to-end analytics project.

## Future Improvements

This project can be expanded in the future by using real government AQI data, adding map-based visualizations, including weather data for deeper analysis, adding prediction models for future AQI trends, and deploying the dashboard online using Render, Streamlit Cloud, or similar platforms.

## Conclusion

The **India Air Quality (AQI) Analysis Dashboard** is a simple but effective project for understanding environmental data in India. It combines analysis and visualization to turn raw AQI values into useful insights that can support awareness, research, and decision-making.


## Dashboard Images

### Overview View
![Average AQI by City](assets/aqi_by_city.png)

### Category Breakdown
![Delhi AQI Category Distribution](assets/delhi_category_distribution.png)

### Trend View
![Delhi Daily AQI Trend 2025](assets/delhi_aqi_trend_2025.png)
