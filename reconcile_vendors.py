import pandas as pd
import os

# Load Vendor A and Vendor B data
vendor_a_path = "data/simulated/sp500_modified_data.csv"
vendor_b_path = "data/simulated/vendor_b_data.csv"

if not os.path.exists(vendor_a_path) or not os.path.exists(vendor_b_path):
    raise FileNotFoundError("Vendor A or Vendor B data not found. Simulate discrepancies first.")

vendor_a = pd.read_csv(vendor_a_path)
vendor_b = pd.read_csv(vendor_b_path)

# Merge the two datasets on Date
reconciled_data = pd.merge(vendor_a, vendor_b, on="Date", suffixes=("_vendor_a", "_vendor_b"), how="outer")

# Reconcile discrepancies (example: average values from both vendors)
for col in ["Open", "High", "Low", "Close", "Volume"]:
    reconciled_data[col] = reconciled_data[[f"{col}_vendor_a", f"{col}_vendor_b"]].mean(axis=1)

# Drop redundant columns
reconciled_data = reconciled_data[["Date", "Open", "High", "Low", "Close", "Volume"]]

# Save reconciled data
output_path = "data/outputs/reconciled_data.csv"
os.makedirs("data/outputs", exist_ok=True)
reconciled_data.to_csv(output_path, index=False)
print(f"Reconciled data saved to {output_path}")