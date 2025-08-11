import pandas as pd
import matplotlib.pyplot as plt
from utils.pdf_generator import generate_pdf
import os

# Step 1: Load the data
csv_file = "data/sample_data.csv"
df = pd.read_csv(csv_file)

# Step 2: Process data (mean, max, min for each column)
summary = "Data Summary Report\n\n"
summary += "Column-wise Statistics:\n\n"

stats = df.describe().loc[["mean", "max", "min"]]

for column in stats.columns:
    summary += f"{column}:\n"
    summary += f"  Mean: {stats.at['mean', column]:.2f}\n"
    summary += f"  Max: {stats.at['max', column]:.2f}\n"
    summary += f"  Min: {stats.at['min', column]:.2f}\n\n"


# Step 3: Generate a bar chart for mean values
mean_values = df.mean(numeric_only=True)
plt.figure(figsize=(8, 5))
mean_values.plot(kind="bar", color="skyblue")
plt.title("Mean Values of Columns")
plt.xlabel("Columns")
plt.ylabel("Mean")
plt.tight_layout()

# Create 'reports' folder if not exists
if not os.path.exists("reports"):
    os.makedirs("reports")

chart_path = "reports/mean_chart.png"
plt.savefig(chart_path)
plt.close()

# Step 4: Generate PDF report
generate_pdf(summary, chart_path)

print("PDF report generated successfully at: reports/report.pdf")
