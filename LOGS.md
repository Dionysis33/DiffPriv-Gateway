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