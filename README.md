# DataLens

A Python-based student performance analytics and risk detection system that analyzes academic performance, attendance, study habits, and previous GPA to identify students who may be academically at risk.

## Overview

DataLens is designed to demonstrate how structured student data can be validated, analyzed, and transformed into actionable academic risk insights.

The project currently uses a synthetic dataset of 500 student records and provides:

- Dataset generation
- Data validation
- Academic risk detection
- Risk-rate calculation
- At-risk student filtering
- Automated unit testing

## Features

### 1. Synthetic Dataset Generation

Generates a reproducible student dataset containing academic and behavioral indicators such as:

- Attendance percentage
- Study hours per day
- Assignment average
- Midterm score
- Previous GPA
- Absences
- At-risk label

### 2. Data Validation

Validates the dataset structure and ensures that important fields contain valid values and ranges.

### 3. Risk Analytics

DataLens calculates:

- Overall student risk rate
- Number of at-risk students
- Filtered list of at-risk students

### 4. Automated Testing

The project includes automated tests using `pytest` to verify dataset validation and analytics functionality.

**Current test result: 10 tests passed.**

## Tech Stack

- Python
- Pandas
- Pytest
- Git & GitHub

## Project Structure

```text
datalens/
│
├── data/
│   └── students.csv
│
├── docs/
│
├── notebooks/
│
├── screenshots/
│
├── src/
│   ├── __init__.py
│   ├── generate_data.py
│   ├── validate_data.py
│   └── analytics.py
│
├── tests/
│   └── test_validate_data.py
│
├── .gitignore
├── LICENSE
└── README.md