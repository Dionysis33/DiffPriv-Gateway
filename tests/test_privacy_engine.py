import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.privacy_engine import apply_laplace_mechanism


@pytest.fixture
def fire_df():
    return pd.DataFrame(
        {
            "Incident ID": range(1, 11),
            "Final Priority": [0, 1, 2, 3, 1, 2, 0, 3, 1, 2],
        }
    )


@pytest.fixture
def salary_df():
    return pd.DataFrame(
        {
            "Salary": [1000.0, 1100.0, 1200.0, 1300.0, 1250.0, 1150.0]
        }
    )


def test_laplace_clipping_bounds(fire_df):
    np.random.seed(42)

    protected_df = apply_laplace_mechanism(
        fire_df,
        column="Final Priority",
        epsilon=1.0,
        sensitivity=3.0,
        min_val=0,
        max_val=3,
    )

    assert "DP_Final Priority" in protected_df.columns
    assert protected_df["DP_Final Priority"].between(0, 3).all()


def test_data_integrity_structure_and_dp_column(fire_df):
    np.random.seed(42)
    original_df = fire_df.copy(deep=True)

    protected_df = apply_laplace_mechanism(
        fire_df,
        column="Final Priority",
        epsilon=1.0,
        sensitivity=3.0,
        min_val=0,
        max_val=3,
    )

    assert len(protected_df) == len(original_df)
    assert list(original_df.columns) == ["Incident ID", "Final Priority"]
    assert list(protected_df.columns) == [
        "Incident ID",
        "Final Priority",
        "DP_Final Priority",
    ]
    assert protected_df["Incident ID"].equals(original_df["Incident ID"])
    assert "DP_Final Priority" not in original_df.columns


def test_utility_score_threshold(fire_df):
    np.random.seed(42)

    protected_df = apply_laplace_mechanism(
        fire_df,
        column="Final Priority",
        epsilon=100.0,
        sensitivity=3.0,
        min_val=0,
        max_val=3,
    )

    mean_difference = abs(
        fire_df["Final Priority"].mean()
        - protected_df["DP_Final Priority"].mean()
    )

    assert mean_difference < 0.1


def test_epsilon_impact_on_noise_variance(salary_df):
    np.random.seed(42)
    protected_low_epsilon = apply_laplace_mechanism(
        salary_df,
        column="Salary",
        epsilon=0.1,
        sensitivity=1.0,
    )

    np.random.seed(42)
    protected_high_epsilon = apply_laplace_mechanism(
        salary_df,
        column="Salary",
        epsilon=10.0,
        sensitivity=1.0,
    )

    low_epsilon_error = (
        protected_low_epsilon["DP_Salary"] - salary_df["Salary"]
    ).abs().mean()

    high_epsilon_error = (
        protected_high_epsilon["DP_Salary"] - salary_df["Salary"]
    ).abs().mean()

    assert low_epsilon_error > high_epsilon_error


def test_robustness_invalid_configuration_raises_expected_exceptions(fire_df):
    with pytest.raises(KeyError):
        apply_laplace_mechanism(
            fire_df,
            column="Wrong Column",
            epsilon=1.0,
            sensitivity=3.0,
            min_val=0,
            max_val=3,
        )

    with pytest.raises(TypeError):
        apply_laplace_mechanism(
            fire_df,
            column="Final Priority",
            epsilon=None,
            sensitivity=3.0,
            min_val=0,
            max_val=3,
        )