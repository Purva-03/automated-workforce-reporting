# 📊 Automated Workforce Headcount Reporting

A data analytics and reporting automation project that uses Python, Pandas, Excel, and Power BI to clean workforce data, calculate monthly headcount metrics, validate data quality, and visualize workforce trends.

## 📌 Project Overview

Workforce reporting helps organizations understand employee movements, monitor headcount, and make informed workforce planning decisions.

This project automates the reporting process by transforming raw HR data into structured reports and an interactive Power BI dashboard.

## 🎯 Project Objectives

- Automate workforce data cleaning and preparation.
- Calculate monthly opening and closing headcount.
- Analyze employee hires and exits.
- Monitor workforce attrition.
- Identify missing values and data quality issues.
- Generate Excel reports for workforce analysis.
- Build interactive Power BI dashboards for decision-making.

## 🛠️ Tools and Technologies

- **Python** — Data processing and automation
- **Pandas** — Data cleaning, transformation, and analysis
- **Excel** — Structured workforce reporting
- **Power BI** — Interactive dashboards and visualization
- **DAX** — Measures and workforce KPIs
- **Git and GitHub** — Version control and project documentation

## 📈 Power BI Dashboard

The Power BI report contains three pages designed to analyze workforce performance and data quality.

### 1. Workforce Overview

Provides a high-level view of workforce size and monthly headcount trends.

**Key metrics:**
- Latest closing headcount
- Total employee hires
- Total employee exits
- Monthly closing headcount trend

![Workforce Overview Dashboard]
<img width="1158" height="657" alt="Screenshot 2026-10-29 160514" src="https://github.com/user-attachments/assets/02cf3028-2149-4b5e-be87-a687f73bafa2" />


*Add your Workforce Overview Power BI screenshot to the `screenshots` folder and name it `workforce-overview.png`.*

### 2. Hires and Attrition Analysis

Examines employee movements and workforce attrition over time.

**Key metrics and visualizations:**
- Total hires and exits
- Average monthly attrition rate
- Monthly hires versus exits
- Employee exits by department
- Monthly attrition trends

![Hires and Attrition Dashboard]
<img width="1165" height="650" alt="Screenshot 2026-10-29 160531" src="https://github.com/user-attachments/assets/1902c350-8d9c-43ba-bbed-c0cb0868fd2c" />


*Add your Hires & Attrition Power BI screenshot to the `screenshots` folder and name it `hires-attrition.png`.*

### 3. Data Quality Dashboard

Highlights data completeness and validation results to support reliable reporting.

**Key metrics and visualizations:**
- Total employee records
- Duplicate employee ID checks
- Missing manager IDs
- Data validation summary
- Missing values by column

![Data Quality Dashboard]
<img width="1163" height="657" alt="Screenshot 2026-10-29 160547" src="https://github.com/user-attachments/assets/7ee6977c-d664-4570-908c-5ad4c06b70c0" />


*Add your Data Quality Power BI screenshot to the `screenshots` folder and name it `data-quality.png`.*

## ⚙️ Python Automation Workflow

The project follows a structured data processing workflow:

1. **Load data:** Import the source HR dataset.
2. **Clean data:** Handle missing values, standardize fields, and prepare employee records.
3. **Validate data:** Check duplicate employee IDs, termination dates, and other data quality conditions.
4. **Calculate metrics:** Generate monthly opening headcount, hires, exits, and closing headcount.
5. **Summarize results:** Prepare monthly and department-level workforce summaries.
6. **Export reports:** Generate Excel reports and CSV outputs for analysis.
7. **Visualize insights:** Use Power BI to explore workforce trends and data quality.

## 📁 Project Structure

```text
automated-workforce-reporting/
│
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── calculate_metrics.py
│   ├── export_reports.py
│   └── generate_missing_values.py
│
├── screenshots/
│   ├── workforce-overview.png
│   ├── hires-attrition.png
│   └── data-quality.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

*The screenshots folder and `requirements.txt` should be added to the repository. Update the structure if your actual filenames differ.*

## 🔍 Data Quality Checks

The project includes validation checks to help identify inconsistencies before reporting.

| Validation Check | Result |
|---|---:|
| Total employee records | 311 |
| Duplicate employee ID rows | 0 |
| Missing manager IDs | 8 |
| Active employees with termination dates | 0 |
| Terminated employees without termination dates | 0 |
| Termination dates before hire dates | 0 |

Missing manager IDs and missing termination dates for active employees are assessed according to the expected business context. Missing values are not automatically treated as errors.

## 📊 Workforce Reporting Outputs

The automation generates structured outputs for workforce analysis, including:

- Monthly headcount summaries
- Department-level workforce summaries
- Data quality summaries
- Missing-value reports
- Excel workforce reporting workbook

Generated reports and employee-level data are excluded from this public repository to protect privacy.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible Python version
- pip
- Power BI Desktop (for viewing or modifying the dashboard)

### 1. Clone the repository

```bash
git clone https://github.com/Purva-03/automated-workforce-reporting.git
cd automated-workforce-reporting
```



### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the input dataset

Place an authorized, appropriately anonymized HR dataset in the location expected by the Python scripts.

Do not upload confidential employee information or personal data to a public repository.

### 5. Run the scripts

Run the Python scripts from the project root in the appropriate workflow order:

```bash
python src/load_data.py
python src/clean_data.py
python src/calculate_metrics.py
python src/export_reports.py
python src/generate_missing_values.py
```

Ensure the input file is available and that the scripts' expected paths and output directories are configured correctly.

## 💡 Key Learnings

- Data cleaning and transformation using Pandas
- Designing data quality validation checks
- Calculating monthly workforce metrics
- Automating Excel report generation
- Creating Power BI dashboards using DAX
- Building a reproducible data analytics workflow
- Organizing projects with Git and GitHub

## 🔒 Data Privacy

This repository is intended to demonstrate the reporting workflow and dashboard design.

The original dataset may contain sensitive employee information. Raw employee data, generated reports, and Power BI files containing identifiable records should not be published without appropriate authorization and sanitization.

## 👩‍💻 Author

**Purva Thakur**

B.E. — Artificial Intelligence and Data Science

[LinkedIn](https://www.linkedin.com/in/purva-thakur315/) | [GitHub](https://github.com/Purva-03)

---

⭐ If you find this project useful, feel free to explore the code and dashboard screenshots.
