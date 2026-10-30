
from pathlib import Path
import pandas as pd

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "processed" / "employees_clean.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "missing_values_by_column.csv"

# Load cleaned employee data
df = pd.read_csv(INPUT_FILE)

# Calculate missing values by column
missing_report = pd.DataFrame({
    "Column": df.columns,
    "MissingCount": df.isna().sum().values,
    "MissingPercentage": (
        df.isna().mean().values * 100
    ).round(2)
})

# Keep only columns with missing values
missing_report = missing_report[
    missing_report["MissingCount"] > 0
].sort_values("MissingCount", ascending=False)

# Save the report
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
missing_report.to_csv(OUTPUT_FILE, index=False)

print("\n--- MISSING VALUES BY COLUMN ---")
print(missing_report.to_string(index=False))
print(f"\nReport saved to: {OUTPUT_FILE}")

