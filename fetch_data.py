import yfinance as yf
import os

# Create directories if they don't exist
if not os.path.exists("data/raw"):
    os.makedirs("data/raw")

# Fetch S&P 500 data
ticker = "^GSPC"  # S&P 500 index
sp500 = yf.Ticker(ticker)

# Download historical data for the last 6 months
data = sp500.history(period="6mo")

# Save the data to a CSV file
file_path = "data/raw/sp500_data.csv"
data.to_csv(file_path)
print(f"Data saved to {file_path}")