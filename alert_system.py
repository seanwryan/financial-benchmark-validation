import pandas as pd
import numpy as np
import os

# Load reconciled data
reconciled_path = "data/outputs/reconciled_data.csv"
if not os.path.exists(reconciled_path):
    raise FileNotFoundError(f"{reconciled_path} not found. Make sure you reconciled the data.")

data = pd.read_csv(reconciled_path)

# Set thresholds for anomaly detection
outlier_thresholds = {
    "Open": (data["Open"].quantile(0.01), data["Open"].quantile(0.99)),
    "High": (data["High"].quantile(0.01), data["High"].quantile(0.99)),
    "Low": (data["Low"].quantile(0.01), data["Low"].quantile(0.99)),
    "Close": (data["Close"].quantile(0.01), data["Close"].quantile(0.99)),
    "Volume": (data["Volume"].quantile(0.01), data["Volume"].quantile(0.99)),
}

# Create a log for alerts
alert_log_path = "data/outputs/alert_log.txt"
with open(alert_log_path, "w") as log:
    log.write("Data Alerts:\n\n")

    # Check for missing data
    for col in data.columns:
        missing_count = data[col].isnull().sum()
        if missing_count > 0:
            log.write(f"Missing data in column '{col}': {missing_count} rows\n")

    # Check for outliers
    for col, (low, high) in outlier_thresholds.items():
        outliers = data[(data[col] < low) | (data[col] > high)]
        if not outliers.empty:
            log.write(f"Outliers detected in column '{col}': {len(outliers)} rows\n")

print(f"Alert log created at {alert_log_path}")