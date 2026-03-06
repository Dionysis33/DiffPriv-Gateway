<p align="center">
  <img src="assets/logo.png" width="400" alt="DiffPriv-Gateway Logo">
</p>

# DiffPriv-Gateway 🛡️

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Dionysis33/DiffPriv-Gateway/graphs/commit-activity)
[![Python application](https://github.com/Dionysis33/DiffPriv-Gateway/actions/workflows/python-app.yml/badge.svg)](https://github.com/Dionysis33/DiffPriv-Gateway/actions/workflows/python-app.yml)

Το **DiffPriv-Gateway** είναι μια λύση ανοικτού κώδικα (Open-Source) που βοηθά τις Μικρομεσαίες Επιχειρήσεις να συμμορφωθούν με τον **GDPR**, εφαρμόζοντας **Διαφορική Ιδιωτικότητα** (Differential Privacy).


---

## 📋 Πίνακας Περιεχομένων
- [Το Επιχειρηματικό Πρόβλημα](#το-επιχειρηματικό-πρόβλημα)
- [Η Λύση μας](#η-λύση-μας)
- [Βασικά Χαρακτηριστικά](#βασικά-χαρακτηριστικά)
- [Τεχνολογίες & Εργαλεία](#τεχνολογίες--εργαλεία)
- [Οδηγίες Εγκατάστασης](#οδηγίες-εγκατάστασης)
- [Συνεισφορά](#οδηγός-συνεισφοράς)
- [Άδεια Χρήσης](#άδεια-χρήσης)

---

## Το Επιχειρηματικό Πρόβλημα
Οι ΜΜΕ συχνά δεν έχουν τους πόρους για σύνθετες τεχνολογίες προστασίας. Η απλή αφαίρεση ονομάτων (anonymization) δεν αρκεί, καθώς οι ταυτότητες μπορούν να αποκαλυφθούν μέσω συνδυασμού δεδομένων (linkage attacks).

---

## Γιατί η Προστασία Δεδομένων είναι Κρίσιμη για τις SMEs

Οι μικρομεσαίες επιχειρήσεις (SMEs) βασίζονται όλο και περισσότερο στα δεδομένα για να βελτιώσουν τις λειτουργίες τους, να κατανοήσουν καλύτερα τη συμπεριφορά πελατών και να υποστηρίξουν τη λήψη αποφάσεων. Ωστόσο, τα datasets τους συχνά περιλαμβάνουν προσωπικά ή ευαίσθητα δεδομένα, όπως πληροφορίες εργαζομένων, οικονομικά στοιχεία και δεδομένα πελατών. Χωρίς κατάλληλους μηχανισμούς προστασίας, τέτοιες αναλύσεις μπορούν να οδηγήσουν σε privacy breaches, κίνδυνο re-identification και κανονιστική έκθεση ως προς τον GDPR.

Το DiffPriv-Gateway αντιμετωπίζει αυτή την ανάγκη ενσωματώνοντας μηχανισμούς **Differential Privacy** στη ροή ανάλυσης δεδομένων. Αντί να εκθέτει raw data, επιτρέπει την παραγωγή χρήσιμων statistical outputs με μειωμένο disclosure risk και με ισχυρότερη ευθυγράμμιση προς τις αρχές του GDPR. Έτσι, οι SMEs αποκτούν μια πρακτική και τεχνικά εφαρμόσιμη προσέγγιση για ασφαλή data analytics.

---

## Η Λύση μας
Αυτό το εργαλείο λειτουργεί ως μια "έξυπνη πύλη" που επεξεργάζεται στατιστικά ερωτήματα. Χρησιμοποιεί τον **Gaussian μηχανισμό** για την προσθήκη ελεγχόμενου θορύβου, διασφαλίζοντας ότι το αποτέλεσμα δεν αποκαλύπτει πληροφορίες για μεμονωμένα άτομα.

---

## Βασικά Χαρακτηριστικά
* **Low-Code Implementation**: Εύκολη ενσωμάτωση σε υπάρχουσες βάσεις δεδομένων.
* **Gaussian & Laplacian Mechanisms**: Υποστήριξη των κορυφαίων αλγορίθμων ιδιωτικότητας.
* **GDPR Ready**: Σχεδιασμένο με βάση την αρχή "Privacy by Design".

---

## Τεχνολογίες & Εργαλεία
* **Γλώσσα**: Python 3.12
* **Βιβλιοθήκες**: `diffprivlib` (IBM), `pandas`, `numpy`
* **Version Control**: Git & GitHub Desktop
* **IDE**: VS Code

---

## Οδηγίες Εγκατάστασης
1. Κλωνοποίηση του αποθετηρίου:
   ```bash
   git clone [https://github.com/Dionysis33/DiffPriv-Gateway.git](https://github.com/Dionysis33/DiffPriv-Gateway.git)