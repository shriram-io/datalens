import pandas as pd

from src.analytics import (
    get_at_risk_students,
    get_risk_rate,
    get_summary,
)


def sample_dataset():
    return pd.DataFrame(
        {
            "student_id": [1, 2, 3, 4],
            "attendance_pct": [90, 80, 70, 60],
            "study_hours_per_day": [3, 2, 1, 1],
            "assignment_avg": [90, 80, 70, 60],
            "midterm_score": [85, 75, 65, 55],
            "previous_gpa": [9.0, 8.0, 7.0, 6.0],
            "absences": [2, 4, 6, 10],
            "at_risk": [0, 0, 1, 1],
        }
    )


def test_summary_returns_correct_student_count():
    data = sample_dataset()

    summary = get_summary(data)

    assert summary["total_students"] == 4
    assert summary["at_risk_students"] == 2


def test_risk_rate_is_correct():
    data = sample_dataset()

    assert get_risk_rate(data) == 50.0


def test_at_risk_students_are_filtered():
    data = sample_dataset()

    result = get_at_risk_students(data)

    assert len(result) == 2
    assert result["at_risk"].eq(1).all()


def test_empty_dataset_has_zero_risk_rate():
    data = sample_dataset().iloc[0:0]

    assert get_risk_rate(data) == 0.0