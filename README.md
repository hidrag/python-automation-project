# Python Automation System – CSV Data Processing & Reporting

## Overview

This project is a Python-based automation tool that processes structured CSV data.
It validates records, applies basic business rules, categorizes users, and generates
clean output files along with logs and summary reports.

The project demonstrates real-world backend automation concepts such as file handling,
validation, logging, CLI arguments, and modular code design.

---

## Features (v1.0)

-   CSV input via command-line arguments
-   Data validation and cleaning
-   User categorization:
    -   Child
    -   Teen
    -   Working Age
    -   Senior
-   Automated output CSV generation
-   Error and process logging
-   Console-based summary reporting

---

## Tech Stack

-   Python 3
-   Standard Library:
    -   csv
    -   argparse
    -   logging
    -   os
    -   sys

No external dependencies required.

---

## Project Structure

```
python-automation-project/
├── data/
│   └── input_users.csv        # Sample input CSV
├── logs/
│   └── app.log                # Auto-generated log file
├── main.py                    # Entry point (CLI execution)
├── validator.py               # Data validation logic
├── processor.py               # Business rules & categorization
├── reporter.py                # Summary report generation
├── config.py                  # Configurable paths
├── requirements.txt           # Dependencies (none external)
└── README.md                  # Project documentation
```

---

## Input CSV Format

The input CSV file should contain the following columns:

```csv
name,age
Abhi,40
John,15
Alice,10
```

Invalid records (missing name or invalid age) are skipped and logged.

---

## How to Run

### Run with default input/output

```bash
python main.py
```

Uses:

-   Input: `data/input_users.csv`
-   Output: `data/output_users.csv`

---

### Run with custom CSV files

```bash
python main.py --input path/to/input.csv --output path/to/output.csv
```

---

## Output

-   Cleaned and categorized CSV output
-   Log file generated at `logs/app.log`
-   Summary printed to console

Example:

```text
Processing completed successfully.
Summary: {'total_users': 5, 'minors': 2, 'working_age': 2, 'seniors': 1}
```

---

## Versions

-   **v1.0** – CSV validation, categorization, and reporting
-   **v1.1 (planned)** – Phone validation and country-based normalization

---

## Purpose

This project was built to demonstrate Python automation, backend data processing,
and clean modular design suitable for real-world workflows.
