
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = (
    PROJECT_DIR / "data" / "processed" / "employees_clean.csv"
)
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned employee data
df = pd.read_csv(INPUT_FILE)

# Convert dates after reading the CSV
df["DateofHire"] = pd.to_datetime(
    df["DateofHire"], errors="coerce"
)
df["DateofTermination"] = pd.to_datetime(
    df["DateofTermination"], errors="coerce"
)

# Validate required columns
required = [
    "EmpID",
    "DateofHire",
    "DateofTermination",
    "Department",
]

missing_columns = [c for c in required if c not in df.columns]

if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

if df["DateofHire"].isna().any():
    raise ValueError("Some hire dates are missing or invalid.")

if df["EmpID"].duplicated().any():
    raise ValueError("Duplicate employee IDs must be reviewed.")

# Build a monthly reporting calendar.
# The dataset contains hire and termination dates through 2018.
first_month = df["DateofHire"].min().to_period("M")
last_date = max(
    df["DateofHire"].max(),
    df["DateofTermination"].max()
)
last_month = last_date.to_period("M")

months = pd.period_range(
    start=first_month,
    end=last_month,
    freq="M"
)

# Calculate company-wide metrics for every month
monthly_rows = []

for month in months:
    month_start = month.start_time.normalize()
    month_end = month.end_time.normalize()

    # Employee is active at month-end if hired by then
    # and not terminated on or before that date.
    active_at_end = (
        (df["DateofHire"] <= month_end)
        & (
            df["DateofTermination"].isna()
            | (df["DateofTermination"] > month_end)
        )
    )

    # Active at the start of this month
    active_at_start = (
    (df["DateofHire"] < month_start)
    & (
        df["DateofTermination"].isna()
        | (df["DateofTermination"] >= month_start)
    )
)

    hires = (
        (df["DateofHire"] >= month_start)
        & (df["DateofHire"] <= month_end)
    ).sum()

    exits = (
        (df["DateofTermination"] >= month_start)
        & (df["DateofTermination"] <= month_end)
    ).sum()

    opening = int(active_at_start.sum())
    closing = int(active_at_end.sum())

    average_headcount = (opening + closing) / 2

    attrition_rate = (
        exits / average_headcount
        if average_headcount > 0
        else None
    )

    monthly_rows.append({
        "Month": str(month),
        "OpeningHeadcount": opening,
        "Hires": int(hires),
        "Exits": int(exits),
        "ClosingHeadcount": closing,
        "NetChange": int(hires - exits),
        "AttritionRate": attrition_rate,
    })

monthly = pd.DataFrame(monthly_rows)

# Validate monthly headcount calculations
monthly["ExpectedClosing"] = (
    monthly["OpeningHeadcount"]
    + monthly["Hires"]
    - monthly["Exits"]
)

monthly["ReconciliationPassed"] = (
    monthly["ExpectedClosing"]
    == monthly["ClosingHeadcount"]
)

# Verify each month's opening headcount matches
# the previous month's closing headcount.
monthly["OpeningMatchesPreviousMonth"] = True

if len(monthly) > 1:
    monthly.loc[
        monthly.index[1:],
        "OpeningMatchesPreviousMonth"
    ] = (
        monthly["OpeningHeadcount"].iloc[1:].to_numpy()
        == monthly["ClosingHeadcount"].iloc[:-1].to_numpy()
    )

print("\n--- VALIDATION RESULTS ---")
print(
    "Months reconciled:",
    int(monthly["ReconciliationPassed"].sum()),
    "out of",
    len(monthly)
)

print(
    "Opening balances matched:",
    int(monthly["OpeningMatchesPreviousMonth"].sum()),
    "out of",
    len(monthly)
)

if not monthly["ReconciliationPassed"].all():
    print("\nMonths with reconciliation errors:")
    print(
        monthly.loc[
            ~monthly["ReconciliationPassed"],
            ["Month", "OpeningHeadcount", "Hires",
             "Exits", "ClosingHeadcount", "ExpectedClosing"]
        ].to_string(index=False)
    )

if not monthly["OpeningMatchesPreviousMonth"].all():
    print("\nMonths with opening balance errors:")
    print(
        monthly.loc[
            ~monthly["OpeningMatchesPreviousMonth"],
            ["Month", "OpeningHeadcount", "ClosingHeadcount"]
        ].to_string(index=False)
    )

if (
    monthly["ReconciliationPassed"].all()
    and monthly["OpeningMatchesPreviousMonth"].all()
):
    print("SUCCESS: All monthly headcount checks passed.")


# Save monthly summary
monthly.to_csv(
    OUTPUT_DIR / "monthly_headcount.csv",
    index=False
)

print("\n--- MONTHLY HEADCOUNT ---")
print(monthly.head(12).to_string(index=False))

print("\n--- LATEST MONTH ---")
print(monthly.tail(1).to_string(index=False))

print("\nMonthly headcount file saved successfully.")
print("\n--- FINAL THREE MONTHS ---")
print(monthly.tail(3).to_string(index=False))

print("\n--- OVERALL TOTALS ---")
print("Total hires:", monthly["Hires"].sum())
print("Total exits:", monthly["Exits"].sum())
print("Final closing headcount:", monthly.iloc[-1]["ClosingHeadcount"])