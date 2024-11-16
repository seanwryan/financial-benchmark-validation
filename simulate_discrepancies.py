import pandas as pd
import random
import os

# Load the original data
file_path = "data/raw/sp500_data.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found. Make sure you fetched the data.")

# Read the original data
data = pd.read_csv(file_path)

# Create a second dataset by introducing intentional discrepancies
data_vendor_b = data.copy()

# Modify vendor B data: shift prices slightly, add missing values
for col in ["Open", "High", "Low", "Close"]:
    data_vendor_b[col] = data_vendor_b[col].apply(
        lambda x: x * random.uniform(0.98, 1.02) if random.random() > 0.1 else None
    )

# Add missing rows to vendor B data
if len(data_vendor_b) > 10:
    data_vendor_b = data_vendor_b.drop(data_vendor_b.sample(n=10).index)

# Save the second dataset
output_path = "data/simulated/vendor_b_data.csv"
os.makedirs("data/simulated", exist_ok=True)
data_vendor_b.to_csv(output_path, index=False)
print(f"Simulated Vendor B data saved to {output_path}")