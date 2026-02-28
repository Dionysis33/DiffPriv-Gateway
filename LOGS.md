# Project Progress Logs - DiffPriv-Gateway

Αυτό το αρχείο καταγράφει την καθημερινή πρόοδο και τις αποφάσεις της ομάδας.

## Φεβρουάριος 2026

### 26/02/2026 - Project Initialization (Tech Lead)
* **Tasks Accomplished**: 
    * Δημιουργία του GitHub Repository με άδεια GPLv3.
    * Στήσιμο του τοπικού περιβάλλοντος (VS Code & GitHub Desktop).
    * Δημιουργία Virtual Environment (venv) και εγκατάσταση βιβλιοθηκών (diffprivlib, pandas, matplotlib).
    * Υλοποίηση του πρώτου core script (`main.py`) για Differential Privacy.
    * Σύνταξη των υποχρεωτικών αρχείων `README.md` και `CONTRIBUTING.md`.
* **Challenges**: Επίλυση σφάλματος TypeError στον Gaussian μηχανισμό (προσθήκη παραμέτρου delta).
* **Next Steps**: Ανάθεση έρευνας βιβλιογραφίας στο Μέλος 2 και σχεδιασμός παρουσίασης στο Μέλος 3.

---

### 28/02/2026 - Infrastructure & Team Synchronization (Tech Lead)
* **Tasks Accomplished**:
    * **Security Framework**: Δημιουργία και ενσωμάτωση επίσημης πολιτικής ασφαλείας (`SECURITY.md`) μέσω Pull Request #3.
    * **CI/CD Automation**: Ενεργοποίηση αυτοματοποιημένου workflow (GitHub Actions) για τον έλεγχο και το testing της Python εφαρμογής σε κάθε push.
    * **Kanban Workflow**: Πλήρης παραμετροποίηση του πίνακα "DiffPriv Development" και απόδοση δικαιωμάτων "Write" σε όλα τα μέλη.
    * **Collaboration**: Η Αθηνά (Member 2) ξεκίνησε την τεκμηρίωση με την υποβολή των πρώτων ερευνητικών πηγών στο `literature_review.md`.
* **Challenges**: Επίλυση ζητημάτων πρόσβασης (permissions) στον πίνακα Kanban για την ομαλή μετακίνηση των tasks.
* **Next Steps**: Υλοποίηση του Laplacian μηχανισμού στο `main.py` και έναρξη σχεδιασμού της παρουσίασης για το Portfolio A από το Μέλος 3.


---


###  28/02/2026 | Algorithm Implementation & Utility Analysis (Tech Lead)

####  Tasks Accomplished
* **Laplace Mechanism Integration**: Υλοποίηση του αλγορίθμου προσθήκης θορύβου Laplace στο `literature_management_lm.ipynb`. Χρήση παραμέτρων $\epsilon = 1.0$ και $\Delta f = 3$ βάσει της έρευνας της @Athina34.
* **Utility & Precision Validation**: Διενέργεια στατιστικού ελέγχου (Mean Difference Analysis). Το αποτέλεσμα έδειξε απόκλιση μόλις **0.0095**, διασφαλίζοντας ότι τα δεδομένα παραμένουν χρήσιμα για ανάλυση παρά την προστασία.
* **Data Visualization**: Δημιουργία συγκριτικών ιστογραμμάτων (Original vs Privacy-Protected) για την οπτικοποίηση της κατανομής του θορύβου.
* **Git Workflow Mastery**: 
    * Δημιουργία feature branch `feat/laplace-mechanism`.
    * Ολοκλήρωση του **Pull Request #5** με επιτυχή συγχώνευση (merge) στην `main`.
* **Project Governance**: 
    * Κλείσιμο του Issue #1 (Literature Review).
    * Άνοιγμα του **Issue #6** (Athina - Privacy Mapping) και του **Issue #7** (Dionysis - Modular Refactoring).

####  Challenges & Solutions
* **Noise Calibration**: Η αρχική προσθήκη θορύβου παρήγαγε κάποιες αρνητικές τιμές. Αποφασίστηκε η υλοποίηση "Clipping Logic" στο επόμενο sprint για να διατηρηθούν οι τιμές στο εύρος 0-3.
* **Coordination**: Συγχρονισμός της εκτενούς βιβλιογραφίας της Αθηνάς (12 πηγές) με τις τεχνικές απαιτήσεις του κώδικα.

####  Next Steps
1. **Dionysis**: Refactoring του κώδικα σε modular συναρτήσεις για υποστήριξη των `adult.csv`, `loans.csv` και `salary.csv`.
2. **Athina**: Δημιουργία της σελίδας `Research & Bibliography` στο GitHub Wiki.
3. **Vasilis (BILLKNITOU)**: Έναρξη νομικής τεκμηρίωσης GDPR και προετοιμασία slide παρουσίασης με τα utility metrics (0.0095).

---