
from pathlib import Path
import pandas as pd

# Locate the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Locate the HR dataset
DATA_FILE = PROJECT_DIR / "data" / "raw" / "HRDataset_v14.csv"

# Check whether the file exists
if not DATA_FILE.exists():
    raise FileNotFoundError(
        f"Dataset not found at: {DATA_FILE}\n"
        "Please place HRDataset_v14.csv inside data/raw/"
    )

# Load the CSV file
df = pd.read_csv(DATA_FILE)

# Display basic information
print("\n--- DATASET OVERVIEW ---")
print(f"Total employee records: {len(df)}")
print(f"Total columns: {len(df.columns)}")

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- FIRST FIVE RECORDS ---")
print(df.head().to_string())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum().sort_values(ascending=False).head(10))

print("\n--- DATA TYPES ---")
print(df.dtypes)
