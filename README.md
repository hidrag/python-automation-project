# Python Automation System – CSV Data Processing & Reporting

## Overview

This project is a Python-based automation tool that processes structured CSV data.
It validates records, applies business rules, categorizes users, normalizes fields,
and generates clean output files along with logs and summary reports.

The project demonstrates real-world backend automation concepts such as file handling,
data validation, normalization, logging, CLI arguments, and modular code design.

---

## Features (v1.1)

-   CSV input via command-line arguments
-   Multi-field data validation:
    -   Name
    -   Age
    -   Email
    -   Country
    -   Active status
    -   Phone number
-   User categorization:
    -   Child
    -   Teen
    -   Working Age
    -   Senior
-   Phone number normalization:
    -   India (+91)
    -   USA (+1)
-   Cross-field validation:
    -   Country vs phone format mismatch detection
-   Soft validation using remarks instead of hard failure
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
    -   re

No external dependencies required.

---

## Project Structure

```
python-automation-project/
├── data/
│   ├── input_users_v1_1_50_records.csv   # Sample input CSV (v1.1)
│   └── output_users.csv                  # Auto-generated output
├── logs/
│   └── app.log                           # Auto-generated log file
├── main.py                               # Entry point (CLI execution)
├── validator.py                          # Field-level validation logic
├── processor.py                          # Business rules & normalization
├── reporter.py                           # Summary report generation
├── config.py                             # Configurable paths
├── requirements.txt                     # Dependencies (none external)
└── README.md                             # Project documentation
```

---

## Input CSV Format (v1.1)

```csv
name,age,email,country,is_active,phone
Abhi,40,abhi@email.com,India,true,9876543210
John,15,john@email.com,USA,true,4155552671
```

### Validation Rules

-   Name must be present and at least 3 characters
-   Age must be a non-negative number
-   Email must contain '@'
-   Country must not be empty
-   is_active must be one of: true, false, yes, no, 1, 0
-   Phone must be exactly 10 digits

Invalid records are skipped and logged.

---

## How to Run

### Run with default input/output

```bash
python main.py
```

### Run with custom CSV files

```bash
python main.py --input data/input_users_v1_1_50_records.csv --output data/output_users.csv
```

---

## Output

-   Cleaned and normalized CSV output
-   Additional fields:
    -   category
    -   remark
-   Log file generated at `logs/app.log`
-   Summary printed to console

Example:

```text
Processing completed successfully.
Summary: {
  'total_users': 25,
  'active_users': 18,
  'inactive_users': 7,
  'child': 6,
  'teen': 3
  'working_age': 11,
  'seniors': 5,
  'phone_mismatches': 9
}
```

---

## Versions

-   **v1.0** – Basic CSV validation and categorization
-   **v1.1** – Phone validation, normalization, and cross-field checks

---

## Purpose

This project was built to demonstrate Python automation, backend data processing,
incremental feature development, and clean modular design suitable for real-world workflows.
