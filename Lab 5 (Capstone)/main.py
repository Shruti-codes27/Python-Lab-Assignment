import pandas as pd
from pathlib import Path

# Path to your data folder
data_folder = Path("data/")
csv_files = list(data_folder.glob("*.csv"))

df_list = []
log_errors = []

for file in csv_files:
    try:
        # Read CSV, skip corrupted lines
        df = pd.read_csv(file, on_bad_lines='skip')

        # Extract file name (without .csv) as dataset type
        data_type = file.stem   # e.g. building_consumption

        # Add metadata column
        df["source_file"] = data_type

        # If month not present, add placeholder
        if "month" not in df.columns:
            df["month"] = "Unknown"

        df_list.append(df)

    except FileNotFoundError:
        log_errors.append(f"File not found: {file}")
    except pd.errors.EmptyDataError:
        log_errors.append(f"Empty or corrupt file skipped: {file}")
    except Exception as e:
        log_errors.append(f"Error in {file}: {e}")

# Combine everything
df_combined = pd.concat(df_list, ignore_index=True)

print("\n===== MERGED DATAFRAME (df_combined) =====")
print(df_combined.head())

print("\n===== ERROR LOG =====")
for err in log_errors:
    print(err if log_errors else "No errors found.")


import pandas as pd

# --------------------------------------------
# Detect the datetime column automatically
# --------------------------------------------
def ensure_datetime(df):
    possible_cols = ["timestamp", "date", "date_time", "datetime"]
    for col in possible_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            df = df.set_index(col)
            return df
    raise ValueError("No datetime column found in the dataset.")


# --------------------------------------------
# Task 2 — DAILY TOTALS
# --------------------------------------------
def calculate_daily_totals(df):
    df = ensure_datetime(df)
    daily = df.resample("D").sum(numeric_only=True)
    return daily


# --------------------------------------------
# Task 2 — WEEKLY TOTALS
# --------------------------------------------
def calculate_weekly_aggregates(df):
    df = ensure_datetime(df)
    weekly = df.resample("W").sum(numeric_only=True)
    return weekly


# --------------------------------------------
# Task 2 — BUILDING-WISE SUMMARY
# --------------------------------------------
def building_wise_summary(df):
    if "building_id" not in df.columns:
        print("⚠️ building_id not found. Using default grouping by source_file.")
        group_col = "source_file"
    else:
        group_col = "building_id"

    summary = df.groupby(group_col).agg({
        "consumption": ["mean", "min", "max", "sum"]
    })
    summary.columns = ["Mean", "Min", "Max", "Total"]
    return summary


# DAILY TOTALS
daily_totals = calculate_daily_totals(df_combined)
print("\n===== DAILY TOTALS =====")
print(daily_totals.head())

# WEEKLY TOTALS
weekly_totals = calculate_weekly_aggregates(df_combined)
print("\n===== WEEKLY TOTALS =====")
print(weekly_totals.head())

# BUILDING SUMMARY
building_summary = building_wise_summary(df_combined)
print("\n===== BUILDING SUMMARY =====")
print(building_summary)

print(df.columns)

import pandas as pd
from pathlib import Path
class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh


class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, reading: MeterReading):
        self.meter_readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        total = self.calculate_total_consumption()
        return {
            "campus": self.name,
            "total_kwh": total,
            "num_readings": len(self.meter_readings)
        }


class BuildingManager:
    def __init__(self):
        self.campus = {}

    def load_from_dataframe(self, df):
        for _, row in df.iterrows():

            b_id = str(row["campus_id"])   # now consistent after renaming

            if b_id not in self.campus:
                self.campus[b_id] = campus(b_id)

            reading = Meter

import matplotlib.pyplot as plt
import pandas as pd

# Make sure timestamp column is datetime
df_combined["timestamp"] = pd.to_datetime(df_combined["timestamp"])

# DAILY consumption (Trend Line)
daily = df_combined.groupby("timestamp")["consumption"].sum()

# WEEKLY average per building
df_combined.set_index("timestamp", inplace=True)
weekly = df_combined.groupby("campus_id").resample("W")["consumption"].mean().reset_index()

# PEAK HOUR (scatter)
df_combined["hour"] = df_combined.index.hour
peak = df_combined[df_combined["hour"] >= 18]   # Example: 6PM onwards as peak hours

# --------------------------- PLOTTING ----------------------------
fig, axes = plt.subplots(3, 1, figsize=(12, 16))

# 1️⃣ TREND LINE – Daily Consumption
axes[0].plot(daily.index, daily.values)
axes[0].set_title("Daily Campus Energy Consumption")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("kWh")
axes[0].grid(True)

# 2️⃣ BAR CHART – Weekly Average by campus
avg_weekly = weekly.groupby("campus_id")["consumption"].mean()
axes[1].bar(avg_weekly.index, avg_weekly.values)
axes[1].set_title("Average Weekly Energy Usage per campus")
axes[1].set_xlabel("campus ID")
axes[1].set_ylabel("Avg Weekly kWh")

# 3️⃣ SCATTER PLOT – Peak Hour Consumption
axes[2].scatter(peak.index, peak["consumption"])
axes[2].set_title("Peak Hour Energy Consumption (Evening)")
axes[2].set_xlabel("Timestamp")
axes[2].set_ylabel("kWh")
axes[2].grid(True)

# Layout + Save
plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()

import os
import pandas as pd

# Create output folder if not exists
os.makedirs("output", exist_ok=True)

# --------------------- 1️⃣ EXPORT CLEANED DATA ---------------------
df_combined.to_csv("output/cleaned_energy_data.csv", index=False)


# --------------------- 2️⃣ SUMMARY STATS PER CAMPUSC ---------------------
campus_summary = df_combined.groupby("campus_id")["consumption"].agg(
    ["mean", "min", "max", "sum"]
).reset_index()

campus_summary.to_csv("output/campus_summary.csv", index=False)


# --------------------- 3️⃣ EXECUTIVE SUMMARY TXT ----------------------

# Total campus energy use
total_consumption = df_combined["consumption"].sum()

# Highest consuming campus
max_campus = campus_summary.loc[
    campus_summary["sum"].idxmax(), "campus_id"
]
max_campus_value = campus_summary["sum"].max()

# Peak load time (when campus uses most energy)
peak_row = df_combined.loc[df_combined["consumption"].idxmax()]
peak_time = peak_row["timestamp"]
peak_value = peak_row["consumption"]

# Weekly trend (simple)
weekly_trend = (
    df_combined.resample("W", on="timestamp")["consumption"].sum()
)

# Daily trend
daily_trend = (
    df_combined.resample("D", on="timestamp")["consumption"].sum()
)

# ------------------- Write to summary.txt -------------------

with open("output/summary.txt", "w") as f:
    f.write("==== Campus Energy Executive Summary ====\n\n")
    f.write(f"Total Campus Consumption: {total_consumption:.2f} kWh\n")
    f.write(f"Highest-Consuming campus: {max_campus} ({max_campus_value:.2f} kWh)\n")
    f.write(f"Peak Load Time: {peak_time} with {peak_value:.2f} kWh\n\n")

    f.write("Weekly Trend (kWh):\n")
    for date, value in weekly_trend.items():
        f.write(f"{date.date()} — {value:.2f}\n")

    f.write("\nDaily Trend (kWh):\n")
    for date, value in daily_trend.items():
        f.write(f"{date.date()} — {value:.2f}\n")

print("✨ Task 5 complete! Files saved in /output/ folder.")

