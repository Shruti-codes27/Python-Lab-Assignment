# Name: Shruti
# Roll no: 2501730066
# Date: 3 Dec 2025

import pandas as pd

df = pd.read_csv("weather_data.csv")

print("---- HEAD ----")
print(df.head())

print("\n---- INFO ----")
print(df.info())

print("\n---- DESCRIBE ----")
print(df.describe())

import pandas as pd

df = pd.read_csv("weather_data.csv")

print(df.isnull().sum())

import pandas as pd

df = pd.read_csv("weather_data.csv")

month_cols = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

df_melt = df.melt(
    id_vars='YEAR',
    value_vars=month_cols,
    var_name='MONTH',
    value_name='TEMP'
)

df_melt['MONTH_NUM'] = pd.to_datetime(df_melt['MONTH'], format='%b').dt.month

df_melt['DATE'] = pd.to_datetime(
    df_melt['YEAR'].astype(str) + '-' + df_melt['MONTH_NUM'].astype(str) + '-01'
)

df_cleaned = df_melt[['DATE', 'YEAR', 'MONTH', 'TEMP']]

print(df_cleaned.head())
print(df_cleaned.info())

import pandas as pd
import numpy as np

df = pd.read_csv("weather_data.csv")

monthly_stats = df.iloc[:, 1:].agg(['mean', 'min', 'max', 'std'])  # months only

yearly_stats = pd.DataFrame({
    'YEAR': df['YEAR'],
    'Mean': df.iloc[:, 1:].mean(axis=1),
    'Min': df.iloc[:, 1:].min(axis=1),
    'Max': df.iloc[:, 1:].max(axis=1),
    'Std Dev': df.iloc[:, 1:].std(axis=1)
})

print("\n===== MONTHLY STATISTICS =====")
print(monthly_stats)

print("\n===== YEARLY STATISTICS =====")
print(yearly_stats)


import matplotlib.pyplot as plt

# Prepare the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [15, 17, 20, 25, 28, 32, 35, 34, 30, 25, 20, 16]  # example in °C
rainfall = [50, 40, 60, 70, 80, 90, 100, 85, 70, 60, 55, 50]  # example in mm

# Line chart for temperature
plt.figure(figsize=(12,6))
plt.plot(months, temperature, marker='o', color='r', label='Temperature (°C)')
plt.title('Monthly Temperature Trends')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()
plt.savefig('temperature_trends.png')
plt.show() 
plt.close()

# Bar chart for rainfall
plt.figure(figsize=(12,6))
plt.bar(months, rainfall, color='b', label='Rainfall (mm)')
plt.title('Monthly Rainfall Totals')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.savefig('rainfall_totals.png')
plt.show()
plt.close()

# Combine both plots in a single figure
fig, ax1 = plt.subplots(figsize=(12,6))

# Line plot for temperature
ax1.plot(months, temperature, color='r', marker='o', label='Temperature (°C)')
ax1.set_xlabel('Months')
ax1.set_ylabel('Temperature (°C)', color='r')
ax1.tick_params(axis='y', labelcolor='r')

# Bar plot for rainfall on same figure but different y-axis
ax2 = ax1.twinx()
ax2.bar(months, rainfall, color='b', alpha=0.3, label='Rainfall (mm)')
ax2.set_ylabel('Rainfall (mm)', color='b')
ax2.tick_params(axis='y', labelcolor='b')

plt.title('Monthly Temperature and Rainfall')
fig.tight_layout()
plt.savefig('combined_plot.png')
plt.show()
plt.close()

print("All plots saved as PNG images.")

import pandas as pd

# Sample daily data for a year
data = {
    'Date': pd.date_range(start='2025-01-01', end='2025-12-31', freq='D'),
    'Temperature': [15 + (i%365)*0.05 for i in range(365)],  # example daily temperature
    'Rainfall': [50 + (i%30) for i in range(365)]            # example daily rainfall
}

df = pd.DataFrame(data)
df['Month'] = df['Date'].dt.month
df['Season'] = df['Month']%12 // 3 + 1  # Simple 4-season mapping

# Group by Month
monthly_stats = df.groupby('Month').agg({
    'Temperature': ['mean', 'min', 'max'],
    'Rainfall': ['mean', 'sum']
})
print("Monthly Statistics:")
print(monthly_stats)

# Group by Season
season_stats = df.groupby('Season').agg({
    'Temperature': ['mean', 'min', 'max'],
    'Rainfall': ['mean', 'sum']
})
print("\nSeasonal Statistics:")
print(season_stats)

# Using resample (time-based)
df.set_index('Date', inplace=True)  # set Date as index for resampling

monthly_resample = df.resample('M').agg({
    'Temperature': ['mean', 'min', 'max'],
    'Rainfall': ['mean', 'sum']
})
print("\nMonthly Statistics Using Resample:")
print(monthly_resample)

# Assume 'df' is your cleaned DataFrame from Task 5
df.to_csv('cleaned_weather_data.csv', index=True)  # saves Date as index
print("Cleaned data exported to 'cleaned_weather_data.csv'")


# Write Markdown report
report = """
# Weather Data Analysis Report

## Overview
This report analyzes daily temperature and rainfall data for the year 2025.

## Insights
- Temperature increases from Jan to Jul, then decreases.
- Rainfall is highest in monsoon months.

## Plots
- temperature_trends.png
- rainfall_totals.png
- combined_plot.png
"""

# Save report
with open('weather_analysis_report.md', 'w') as f:
    f.write(report)
print("Report saved as weather_analysis_report.md")







