import pandas as pd
import numpy as np

def apply_laplace_mechanism(df, column, epsilon, sensitivity, min_val=None, max_val=None):
    """
    Modular υλοποίηση του Laplace Mechanism για Differential Privacy.
    """
    # Δημιουργία αντιγράφου για να μην επηρεαστεί το αρχικό DataFrame (Data Integrity)
    df_result = df.copy()
    
    # Υπολογισμός της παραμέτρου beta για τον θόρυβο
    beta = sensitivity / epsilon
    
    # Παραγωγή του Laplace Noise με βάση το μέγεθος του dataset
    noise = np.random.laplace(0, beta, size=len(df_result))
    
    # Δημιουργία του νέου column με το πρόθεμα DP_
    new_col_name = f'DP_{column}'
    df_result[new_col_name] = df_result[column] + noise
    
    # Clipping & Rounding (Απαιτήσεις του Privacy by Design)
    # Διασφαλίζει ότι τα δεδομένα παραμένουν εντός λογικών ορίων και είναι χρηστικά
    if min_val is not None and max_val is not None:
        # Εφαρμογή Clipping για περιορισμό των τιμών στο εύρος [min, max]
        df_result[new_col_name] = np.clip(df_result[new_col_name], min_val, max_val)
        
        # Εφαρμογή Rounding για μετατροπή σε ακέραιες τιμές (Business Logic)
        df_result[new_col_name] = np.round(df_result[new_col_name])
        
    return df_result