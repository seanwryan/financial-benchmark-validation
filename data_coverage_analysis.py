import pandas as pd
import os
import matplotlib.pyplot as plt

# Load reconciled data
reconciled_path = "data/outputs/reconciled_data.csv"
if not os.path.exists(reconciled_path):
    raise FileNotFoundError(f"{reconciled_path} not found.")

data = pd.read_csv(reconciled_path)

# Define client requirements
required_columns = ["Date", "Close", "Volume"]
completeness_threshold = 0.95  # 95%

# Check for missing values in required fields
missing_data = data[required_columns].isnull().sum()
total_rows = len(data)

# Calculate data coverage
coverage = 1 - (missing_data / total_rows)
coverage_report = coverage.to_frame(name="Coverage")
coverage_report["Meets Requirement"] = coverage_report["Coverage"] >= completeness_threshold

# Save the coverage report
report_path = "data/outputs/coverage_report.csv"
os.makedirs("data/outputs", exist_ok=True)
coverage_report.to_csv(report_path, index=True)
print(f"Data coverage analysis saved to {report_path}")

# Print a summary to the console
print("\nCoverage Analysis:")
print(coverage_report)

# Create a bar chart for coverage
plt.figure(figsize=(8, 5))
coverage_report["Coverage"].plot(kind="bar", color=["green" if val else "red" for val in coverage_report["Meets Requirement"]])
plt.title("Data Coverage Analysis")
plt.ylabel("Coverage Percentage")
plt.ylim(0, 1.1)
plt.axhline(y=completeness_threshold, color="blue", linestyle="--", label="Threshold")
plt.legend()
plt.savefig("data/outputs/data_coverage_chart.png")
plt.show()
