import numpy as np
import pandas as pd
import pytest

from src.privacy_engine import (
    apply_gaussian_mechanism,
    apply_laplace_mechanism,
)


# Fixture με δείγμα δεδομένων τύπου "fire incidents"
# Χρησιμοποιείται σε tests όπου η κλίμακα τιμών είναι 0-3.
@pytest.fixture
def fire_df():
    return pd.DataFrame(
        {
            "Incident ID": range(1, 11),
            "Final Priority": [0, 1, 2, 3, 1, 2, 0, 3, 1, 2],
        }
    )


# Fixture με αριθμητικά δεδομένα μισθών.
# Χρησιμοποιείται για να συγκρίνουμε την επίδραση διαφορετικών
# τιμών epsilon πάνω στον θόρυβο.
@pytest.fixture
def salary_df():
    return pd.DataFrame(
        {
            "Salary": [1000.0, 1100.0, 1200.0, 1300.0, 1250.0, 1150.0],
        }
    )


# Ελέγχει ότι μετά την εφαρμογή του Laplace mechanism
# οι τιμές παραμένουν μέσα στα όρια [0, 3] λόγω clipping.
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


# Ελέγχει ότι:
# - δεν αλλάζει το αρχικό DataFrame
# - διατηρείται η δομή
# - προστίθεται σωστά το DP column
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


# Ελέγχει την "χρησιμότητα" του αποτελέσματος.
# Με μεγάλο epsilon ο θόρυβος πρέπει να είναι μικρός.
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


# Ελέγχει ότι το epsilon επηρεάζει σωστά το μέγεθος του θορύβου.
# Μικρό epsilon => περισσότερος θόρυβος
# Μεγάλο epsilon => λιγότερος θόρυβος
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


# Ελέγχει τη συμπεριφορά του συστήματος όταν δοθούν λανθασμένες
# παράμετροι ή invalid configuration.
def test_robustness_invalid_configuration_raises_expected_exceptions(
    fire_df,
):
    with pytest.raises(KeyError):
        apply_laplace_mechanism(
            fire_df,
            column="Wrong Column",
            epsilon=1.0,
            sensitivity=3.0,
            min_val=0,
            max_val=3,
        )

    with pytest.raises(ValueError):
        apply_laplace_mechanism(
            fire_df,
            column="Final Priority",
            epsilon=None,
            sensitivity=3.0,
            min_val=0,
            max_val=3,
        )

    with pytest.raises(ValueError):
        apply_laplace_mechanism(
            fire_df,
            column="Final Priority",
            epsilon=0,
            sensitivity=3.0,
            min_val=0,
            max_val=3,
        )


# Ελέγχει ότι το Gaussian mechanism δημιουργεί νέο DP column
# χωρίς να αλλοιώνει το αρχικό DataFrame.
def test_gaussian_creates_dp_column_and_preserves_original(fire_df):
    original_df = fire_df.copy(deep=True)

    protected_df = apply_gaussian_mechanism(
        fire_df,
        column="Final Priority",
        epsilon=1.0,
        delta=1e-5,
        sensitivity=3.0,
        min_val=0,
        max_val=3,
        random_state=42,
    )

    assert "DP_Final Priority" in protected_df.columns
    assert "DP_Final Priority" not in original_df.columns
    assert len(protected_df) == len(original_df)
    assert protected_df["Incident ID"].equals(original_df["Incident ID"])


# Ελέγχει ότι το Gaussian mechanism, όταν δοθούν όρια,
# κρατά τις τιμές μέσα στο επιτρεπτό range.
def test_gaussian_clipping_bounds(fire_df):
    protected_df = apply_gaussian_mechanism(
        fire_df,
        column="Final Priority",
        epsilon=1.0,
        delta=1e-5,
        sensitivity=3.0,
        min_val=0,
        max_val=3,
        random_state=42,
    )

    assert protected_df["DP_Final Priority"].between(0, 3).all()


# Ελέγχει ότι με σταθερό random_state το Gaussian mechanism
# είναι reproducible και παράγει το ίδιο αποτέλεσμα.
def test_gaussian_is_reproducible_with_fixed_random_state(fire_df):
    protected_df_1 = apply_gaussian_mechanism(
        fire_df,
        column="Final Priority",
        epsilon=1.0,
        delta=1e-5,
        sensitivity=3.0,
        min_val=0,
        max_val=3,
        random_state=42,
    )

    protected_df_2 = apply_gaussian_mechanism(
        fire_df,
        column="Final Priority",
        epsilon=1.0,
        delta=1e-5,
        sensitivity=3.0,
        min_val=0,
        max_val=3,
        random_state=42,
    )

    assert protected_df_1["DP_Final Priority"].equals(
        protected_df_2["DP_Final Priority"]
    )


# Ελέγχει invalid παραμέτρους για το Gaussian mechanism.
def test_gaussian_invalid_configuration_raises_expected_exceptions(fire_df):
    with pytest.raises(KeyError):
        apply_gaussian_mechanism(
            fire_df,
            column="Wrong Column",
            epsilon=1.0,
            delta=1e-5,
            sensitivity=3.0,
            min_val=0,
            max_val=3,
            random_state=42,
        )

    with pytest.raises(ValueError):
        apply_gaussian_mechanism(
            fire_df,
            column="Final Priority",
            epsilon=0,
            delta=1e-5,
            sensitivity=3.0,
            min_val=0,
            max_val=3,
            random_state=42,
        )

    with pytest.raises(ValueError):
        apply_gaussian_mechanism(
            fire_df,
            column="Final Priority",
            epsilon=1.0,
            delta=0,
            sensitivity=3.0,
            min_val=0,
            max_val=3,
            random_state=42,
        )

    with pytest.raises(ValueError):
        apply_gaussian_mechanism(
            fire_df,
            column="Final Priority",
            epsilon=1.0,
            delta=1.5,
            sensitivity=3.0,
            min_val=0,
            max_val=3,
            random_state=42,
        )
