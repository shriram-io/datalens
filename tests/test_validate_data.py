import pandas as pd
import pytest

from src.validate_data import validate_dataset


def valid_dataset() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "student_id": ["STU0001", "STU0002"],
            "attendance_pct": [85.0, 72.0],
            "study_hours_per_day": [4.0, 2.5],
            "assignment_avg": [78.0, 61.0],
            "midterm_score": [82.0, 55.0],
            "previous_gpa": [8.2, 6.1],
            "absences": [3, 7],
            "at_risk": [0, 1],
        }
    )


def test_valid_dataset_passes():
    data = valid_dataset()

    validate_dataset(data)


def test_missing_values_are_rejected():
    data = valid_dataset()
    data.loc[0, "attendance_pct"] = None

    with pytest.raises(ValueError, match="missing values"):
        validate_dataset(data)


def test_duplicate_student_ids_are_rejected():
    data = valid_dataset()
    data.loc[1, "student_id"] = "STU0001"

    with pytest.raises(ValueError, match="duplicate student IDs"):
        validate_dataset(data)


def test_invalid_attendance_is_rejected():
    data = valid_dataset()
    data.loc[0, "attendance_pct"] = 120

    with pytest.raises(ValueError, match="Attendance"):
        validate_dataset(data)


def test_invalid_gpa_is_rejected():
    data = valid_dataset()
    data.loc[0, "previous_gpa"] = 12

    with pytest.raises(ValueError, match="GPA"):
        validate_dataset(data)


def test_invalid_risk_label_is_rejected():
    data = valid_dataset()
    data.loc[0, "at_risk"] = 2

    with pytest.raises(ValueError, match="at_risk"):
        validate_dataset(data)