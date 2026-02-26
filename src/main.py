import numpy as np
from diffprivlib.mechanisms import Gaussian

# 1. Τα πραγματικά ευαίσθητα δεδομένα μας (π.χ. μισθοί υπαλλήλων)
secret_salaries = [2500, 2800, 3100, 4500, 2200]
actual_mean = np.mean(secret_salaries)

# Προσθήκη της παραμέτρου delta (απαραίτητη για τον Gaussian μηχανισμό)
dp_mechanism = Gaussian(epsilon=1.0, delta=0.00001, sensitivity=2000)

# 3. Προσθήκη θορύβου στον μέσο όρο
private_mean = dp_mechanism.randomise(actual_mean)

print(f"Πραγματικός Μέσος Όρος: {actual_mean}€")
print(f"Προστατευμένος Μέσος Όρος (με θόρυβο): {private_mean:.2f}€")
print("Η ιδιωτικότητα των δεδομένων διασφαλίστηκε!")