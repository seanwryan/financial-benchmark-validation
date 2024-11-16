import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure the 'visualizations' directory exists
visualizations_dir = "visualizations"
os.makedirs(visualizations_dir, exist_ok=True)
print(f"Directory '{visualizations_dir}' is ready.")

# Load the reconciled data
file_path = "data/outputs/sp500_reconciled_data.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found. Make sure you reconciled the data.")

data = pd.read_csv(file_path)

# Set Date as Index for time-series visualization
data['Date'] = pd.to_datetime(data['Date'], utc=True)  # Ensure consistent datetime format
data.set_index('Date', inplace=True)

# Visualization 1: Closing Price Over Time
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
plt.title("S&P 500 Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(visualizations_dir, "closing_price_over_time.png"))
plt.show()

# Visualization 2: Volume Traded Over Time
plt.figure(figsize=(10, 6))
plt.bar(data.index, data['Volume'], label='Volume Traded', color='green', alpha=0.7)
plt.title("S&P 500 Volume Traded Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(visualizations_dir, "volume_traded_over_time.png"))
plt.show()

print("\nVisualizations saved to the 'visualizations/' folder.")