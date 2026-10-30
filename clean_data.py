
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_FILE = PROJECT_DIR / "data" / "raw" / "HRDataset_v14.csv"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load original data
df = pd.read_csv(RAW_FILE)

print("Starting data-quality checks...")
print(f"Original records: {len(df)}")

# 1. Check duplicate employee IDs
duplicate_ids = df[df.duplicated(subset=["EmpID"], keep=False)]
print(f"Rows with duplicate EmpID: {len(duplicate_ids)}")

# 2. Convert dates safely
date_columns = [
    "DateofHire",
    "DateofTermination",
    "LastPerformanceReview_Date"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column], errors="coerce"
    )

# 3. Check missing values
print("\nMissing values by column:")
print(df.isna().sum().sort_values(ascending=False).head(15))

# 4. Check employment status against termination date
active_without_termination = df[
    (df["EmploymentStatus"] == "Active")
    & (df["DateofTermination"].notna())
]

terminated_without_date = df[
    (df["EmploymentStatus"].isin([
        "Voluntarily Terminated",
        "Terminated for Cause"
    ]))
    & (df["DateofTermination"].isna())
]

print("\nStatus consistency checks:")
print(
    "Active employees with termination dates:",
    len(active_without_termination)
)
print(
    "Terminated employees without termination dates:",
    len(terminated_without_date)
)

# 5. Check hire dates after termination dates
invalid_dates = df[
    df["DateofTermination"].notna()
    & (df["DateofTermination"] < df["DateofHire"])
]

print("Termination before hire:", len(invalid_dates))

# 6. Check missing manager assignments
missing_managers = df[df["ManagerID"].isna()]
print("Missing ManagerID:", len(missing_managers))

# 7. Save an audit report
quality_summary = pd.DataFrame({
    "Check": [
        "Total employee records",
        "Duplicate EmpID rows",
        "Missing ManagerID",
        "Active with termination date",
        "Terminated without termination date",
        "Termination before hire"
    ],
    "Count": [
        len(df),
        len(duplicate_ids),
        len(missing_managers),
        len(active_without_termination),
        len(terminated_without_date),
        len(invalid_dates)
    ]
})

quality_summary.to_csv(
    PROCESSED_DIR / "data_quality_summary.csv",
    index=False
)

# 8. Save a cleaned copy, preserving all original rows
df.to_csv(
    PROCESSED_DIR / "employees_clean.csv",
    index=False,
    date_format="%Y-%m-%d"
)

print("\nData-quality summary saved.")
print("Cleaned employee data saved.")
print(f"Output folder: {PROCESSED_DIR}")
