from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/students.csv")

EXPECTED_COLUMNS = [
    "student_id",
    "attendance_pct",
    "study_hours_per_day",
    "assignment_avg",
    "midterm_score",
    "previous_gpa",
    "absences",
    "at_risk",
]


def validate_dataset(data: pd.DataFrame) -> None:
    """Validate the structure and basic quality of the student dataset."""

    # Schema validation
    missing_columns = [
        column for column in EXPECTED_COLUMNS
        if column not in data.columns
    ]

    unexpected_columns = [
        column for column in data.columns
        if column not in EXPECTED_COLUMNS
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    if unexpected_columns:
        raise ValueError(
            f"Unexpected columns found: {unexpected_columns}"
        )

    # Missing-value validation
    if data.isnull().any().any():
        raise ValueError("Dataset contains missing values.")

    # Duplicate validation
    if data.duplicated().any():
        raise ValueError("Dataset contains duplicate rows.")

    if data["student_id"].duplicated().any():
        raise ValueError("Dataset contains duplicate student IDs.")

    # Range validation
    if not data["attendance_pct"].between(0, 100).all():
        raise ValueError("Attendance values must be between 0 and 100.")

    if not data["assignment_avg"].between(0, 100).all():
        raise ValueError("Assignment scores must be between 0 and 100.")

    if not data["midterm_score"].between(0, 100).all():
        raise ValueError("Midterm scores must be between 0 and 100.")

    if not data["previous_gpa"].between(0, 10).all():
        raise ValueError("GPA values must be between 0 and 10.")

    if (data["study_hours_per_day"] < 0).any():
        raise ValueError("Study hours cannot be negative.")

    if (data["absences"] < 0).any():
        raise ValueError("Absences cannot be negative.")

    if not data["at_risk"].isin([0, 1]).all():
        raise ValueError("at_risk must contain only 0 or 1.")

    print("Dataset validation passed.")
    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")
    print("Missing values: 0")
    print("Duplicate rows: 0")
    print("Duplicate student IDs: 0")


def main() -> None:
    """Load and validate the student dataset."""

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        )

    data = pd.read_csv(DATA_PATH)
    validate_dataset(data)


if __name__ == "__main__":
    main()