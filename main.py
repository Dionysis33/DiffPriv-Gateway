import os

import pandas as pd

from src.privacy_engine import apply_laplace_mechanism


def run_production_demo():
    print("DiffPriv-Gateway | Production Entry Point")
    print("-" * 45)

    file_path = os.path.join("data", "synthetic", "fire.csv")

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        protected_df = apply_laplace_mechanism(
            df,
            column="Final Priority",
            epsilon=1.0,
            sensitivity=3.0,
            min_val=0,
            max_val=3,
        )

        print("\nΤο Pipeline εκτελέστηκε επιτυχώς!")
        print("Προεπισκόπηση δεδομένων (Original vs Protected):")
        print(protected_df[["Final Priority", "DP_Final Priority"]].head())

        print(f"\nΣύνολο γραμμών: {len(protected_df)} (OK)")
    else:
        print(f"Σφάλμα: Το αρχείο {file_path} δεν βρέθηκε.")


if __name__ == "__main__":
    run_production_demo()
