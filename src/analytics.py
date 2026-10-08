from pathlib import Path

import pandas as pd


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "students.csv"


def load_dataset(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the student dataset from CSV."""
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_csv(path)


def get_summary(data: pd.DataFrame) -> dict:
    """Return high-level summary statistics."""
    return {
        "total_students": len(data),
        "average_attendance": round(data["attendance_pct"].mean(), 2),
        "average_study_hours": round(data["study_hours_per_day"].mean(), 2),
        "average_assignment_score": round(data["assignment_avg"].mean(), 2),
        "average_midterm_score": round(data["midterm_score"].mean(), 2),
        "average_previous_gpa": round(data["previous_gpa"].mean(), 2),
        "at_risk_students": int(data["at_risk"].sum()),
    }


def get_risk_rate(data: pd.DataFrame) -> float:
    """Calculate the percentage of students identified as at risk."""
    if len(data) == 0:
        return 0.0

    return round(data["at_risk"].mean() * 100, 2)


def get_at_risk_students(data: pd.DataFrame) -> pd.DataFrame:
    """Return only students identified as at risk."""
    return data[data["at_risk"] == 1].copy()


def main() -> None:
    """Run a basic DataLens analytics report."""
    data = load_dataset()
    summary = get_summary(data)
    risk_rate = get_risk_rate(data)

    print("DataLens Analytics Report")
    print("=" * 30)

    for key, value in summary.items():
        print(f"{key}: {value}")

    print(f"risk_rate: {risk_rate}%")


if __name__ == "__main__":
    main()