import pandas as pd
import numpy as np
import os

# Load the simulated data
file_path = "data/simulated/sp500_modified_data.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found. Make sure you simulated discrepancies.")

data = pd.read_csv(file_path)

# Validate: Check for missing values
print("Checking for missing values...")
missing_values = data.isnull().sum()
print(missing_values)

# Handle missing values: Fill with median for numeric columns
for col in data.select_dtypes(include=[np.number]).columns:
    median_value = data[col].median()
    data[col].fillna(median_value, inplace=True)

# Validate: Check for inconsistent values
print("\nDetecting inconsistent values...")
# For simplicity, assume numeric columns should have values within realistic ranges
for col in data.select_dtypes(include=[np.number]).columns:
    lower_bound = data[col].quantile(0.01)  # Lower 1st percentile
    upper_bound = data[col].quantile(0.99)  # Upper 99th percentile
    inconsistent = (data[col] < lower_bound) | (data[col] > upper_bound)
    print(f"{col}: {inconsistent.sum()} inconsistent values detected.")
    # Replace outliers with median
    data.loc[inconsistent, col] = data[col].median()

# Save the reconciled data
reconciled_file_path = "data/outputs/sp500_reconciled_data.csv"
os.makedirs("data/outputs", exist_ok=True)
data.to_csv(reconciled_file_path, index=False)
print(f"\nReconciled data saved to {reconciled_file_path}")