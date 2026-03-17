import numpy as np
from diffprivlib.mechanisms import GaussianAnalytic


def apply_laplace_mechanism(
    df,
    column,
    epsilon,
    sensitivity,
    min_val=None,
    max_val=None,
):
    """
    Υλοποίηση του Laplace mechanism για Differential Privacy.
    Επιστρέφει νέο DataFrame με νέο column της μορφής DP_<column>.
    """
    if column not in df.columns:
        raise KeyError(column)

    if epsilon is None or epsilon <= 0:
        raise ValueError("epsilon must be > 0")

    if sensitivity is None or sensitivity < 0:
        raise ValueError("sensitivity must be >= 0")

    # Δημιουργία αντιγράφου ώστε να μην επηρεάζεται το αρχικό DataFrame
    df_result = df.copy()

    # Παράμετρος κλίμακας για τον Laplace θόρυβο
    beta = sensitivity / epsilon

    # Παραγωγή θορύβου με μέγεθος ίσο με το πλήθος των γραμμών
    noise = np.random.laplace(0, beta, size=len(df_result))

    # Δημιουργία νέου προστατευμένου column
    new_col_name = f"DP_{column}"
    df_result[new_col_name] = df_result[column] + noise

    # Αν υπάρχουν λογικά όρια, εφαρμόζουμε clipping και rounding
    if min_val is not None and max_val is not None:
        df_result[new_col_name] = np.clip(
            df_result[new_col_name],
            min_val,
            max_val,
        )
        df_result[new_col_name] = np.round(df_result[new_col_name])

    return df_result


def apply_gaussian_mechanism(
    df,
    column,
    epsilon,
    delta,
    sensitivity,
    min_val=None,
    max_val=None,
    random_state=None,
):
    """
    Υλοποίηση του Gaussian mechanism για Differential Privacy.
    Επιστρέφει νέο DataFrame με νέο column της μορφής DP_<column>.
    """
    if column not in df.columns:
        raise KeyError(column)

    if epsilon is None or epsilon <= 0:
        raise ValueError("epsilon must be > 0")

    if delta is None or not (0 < delta < 1):
        raise ValueError("delta must be between 0 and 1")

    if sensitivity is None or sensitivity < 0:
        raise ValueError("sensitivity must be >= 0")

    # Δημιουργία αντιγράφου ώστε να μην επηρεάζεται το αρχικό DataFrame
    df_result = df.copy()

    # Δημιουργία Gaussian mechanism από diffprivlib
    mechanism = GaussianAnalytic(
        epsilon=epsilon,
        delta=delta,
        sensitivity=sensitivity,
        random_state=random_state,
    )

    # Δημιουργία νέου προστατευμένου column
    new_col_name = f"DP_{column}"
    df_result[new_col_name] = df_result[column].apply(
        lambda value: mechanism.randomise(value)
    )

    # Αν υπάρχουν λογικά όρια, εφαρμόζουμε clipping και rounding
    if min_val is not None and max_val is not None:
        df_result[new_col_name] = np.clip(
            df_result[new_col_name],
            min_val,
            max_val,
        )
        df_result[new_col_name] = np.round(df_result[new_col_name])

    return df_result
