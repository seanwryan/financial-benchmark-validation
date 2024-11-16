import pandas as pd
import random
import os

# Load the original data
file_path = "data/raw/sp500_data.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found. Make sure you fetched the data.")

data = pd.read_csv(file_path)

# Introduce missing values
num_missing = len(data) // 10  # 10% of rows
for _ in range(num_missing):
    row_idx = random.randint(0, len(data) - 1)
    col_idx = random.randint(1, len(data.columns) - 1)  # Avoid the 'Date' column
    data.iloc[row_idx, col_idx] = None

# Introduce conflicting values
num_conflicts = len(data) // 20  # 5% of rows
for _ in range(num_conflicts):
    row_idx = random.randint(0, len(data) - 1)
    col_idx = random.randint(1, len(data.columns) - 1)  # Avoid the 'Date' column
    data.iloc[row_idx, col_idx] = data.iloc[row_idx, col_idx] * random.uniform(0.9, 1.1)  # Small variance

# Save the modified data
modified_file_path = "data/simulated/sp500_modified_data.csv"
os.makedirs("data/simulated", exist_ok=True)
data.to_csv(modified_file_path, index=False)
print(f"Modified data saved to {modified_file_path}")