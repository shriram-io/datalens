import numpy as np
import pandas as pd


def generate_student_data(
    n_students: int = 500,
    random_seed: int = 42,
) -> pd.DataFrame:
    """Generate a reproducible synthetic student performance dataset."""

    rng = np.random.default_rng(random_seed)

    attendance = np.clip(
        rng.normal(78, 12, n_students),
        35,
        100,
    )

    study_hours = np.clip(
        rng.normal(3.5, 1.5, n_students),
        0.5,
        10,
    )

    assignment_avg = np.clip(
        rng.normal(68, 15, n_students),
        20,
        100,
    )

    midterm_score = np.clip(
        rng.normal(65, 16, n_students),
        15,
        100,
    )

    previous_gpa = np.clip(
        rng.normal(6.8, 1.2, n_students),
        3.0,
        10.0,
    )

    absences = np.maximum(
        np.rint((100 - attendance) / 4 + rng.normal(0, 1.5, n_students)),
        0,
    ).astype(int)

    # Latent performance score used only to generate the target.
    performance_score = (
        0.30 * attendance
        + 0.20 * assignment_avg
        + 0.20 * midterm_score
        + 0.15 * previous_gpa * 10
        + 0.15 * study_hours * 10
        + rng.normal(0, 7, n_students)
    )

    at_risk = (
        (performance_score < 58)
        | ((attendance < 60) & (midterm_score < 55))
    ).astype(int)

    return pd.DataFrame(
        {
            "student_id": [
                f"STU{number:04d}"
                for number in range(1, n_students + 1)
            ],
            "attendance_pct": np.round(attendance, 2),
            "study_hours_per_day": np.round(study_hours, 2),
            "assignment_avg": np.round(assignment_avg, 2),
            "midterm_score": np.round(midterm_score, 2),
            "previous_gpa": np.round(previous_gpa, 2),
            "absences": absences,
            "at_risk": at_risk,
        }
    )


def main() -> None:
    """Generate and save the synthetic dataset."""

    data = generate_student_data()

    output_path = "data/students.csv"
    data.to_csv(output_path, index=False)

    print(f"Generated {len(data)} student records.")
    print(f"Saved dataset to: {output_path}")
    print("\nRisk distribution:")
    print(data["at_risk"].value_counts().sort_index())


if __name__ == "__main__":
    main()