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

### 06/03/2026 | Phase 2: Scalability & Multi-Dataset Audit (Tech Lead)

####  Tasks Accomplished
* **Master Pipeline Development**: Δημιουργία του `SME_Data_Privacy_Scalability.ipynb` για την αυτοματοποιημένη επεξεργασία πολλαπλών datasets.
* **Modular Refactoring (Issue #7)**: Υλοποίηση κεντρικού συστήματος ρυθμίσεων (`datasets_config`) που επιτρέπει την προσθήκη νέων πηγών δεδομένων χωρίς αλλαγή του κώδικα.
* **Production-Ready Logic**: Ενσωμάτωση μηχανισμών "Clipping" και "Rounding" στη συνάρτηση Laplace, διασφαλίζοντας ότι τα προστατευμένα δεδομένα παραμένουν εντός επιχειρηματικών ορίων (π.χ. 0-3 για το Priority).
* **Team Integration & Merge**: 
    * Επιτυχής συγχώνευση του **Pull Request #8** (@BILLKNITOU) με τη νομική ανάλυση GDPR και το προσχέδιο παρουσίασης.
    * Ενημέρωση του **Project Wiki** με εξειδικευμένες σελίδες για την Τεχνική Αρχιτεκτονική και τη Βιβλιογραφία.
* **Performance Validation**: Επιβεβαίωση Utility Score στο `fire.csv` με απόκλιση μόλις **0.0033** μετά το refactoring.

####  Challenges & Solutions
* **Path & Scope Issues**: Επίλυση σφαλμάτων `KeyError` και `NameError` στο Jupyter περιβάλλον μέσω σωστής αρχικοποίησης μεταβλητών και χρήσης σχετικών διαδρομών (`../data/`).
* **Non-Fast-Forward Push**: Διαχείριση Git conflicts μέσω `git pull` για το συγχρονισμό των τοπικών αλλαγών με τις νομικές προσθήκες του Βασίλη στο remote.

####  Next Steps
1. **Athina (Member 2)**: Εκτέλεση Data Profiling στα `adult.csv`, `loans.csv` και `salary.csv` για τον προσδιορισμό του Sensitivity ($\Delta f$).
2. **Dionysis (Tech Lead)**: Ενημέρωση των παραμέτρων στο Master Pipeline μόλις ολοκληρωθεί το profiling.
3. **Vasilis (Member 3)**: Ενσωμάτωση των νέων Utility Metrics (από όλα τα datasets) στα τελικά slides της παρουσίασης.

---

### 16/03/2026 | Phase 2: Testing Infrastructure & Production Handover (Tech Lead)

####  Tasks Accomplished
* **Production-Ready Restructuring (Issue #10)**: 
    * Πλήρης αναδιοργάνωση του repository σε modular μορφή (μεταφορά της λογικής στο `src/privacy_engine.py`).
    * Δημιουργία `src/__init__.py` για σωστό package resolution.
* **Unit Testing Integration (Issue #9 & PR #11)**:
    * Επιτυχής συγχώνευση (merge) της σουίτας δοκιμών του @BILLKNITOU. 
    * Επαλήθευση 5 κρίσιμων σεναρίων: Clipping Bounds, Data Integrity, Utility Thresholds, Epsilon Impact και Robustness.
* **CI/CD Validation**: Επιβεβαίωση ότι το αυτοματοποιημένο workflow (GitHub Actions) εκτελείται επιτυχώς και "πρασινίζει" το build μετά την προσθήκη των tests.
* **Wiki Documentation Rewrite**:
    * Πλήρης σύνταξη της σελίδας **Technical Architecture** με την περιγραφή της modular δομής.
    * Επικαιροποίηση της σελίδας **Technical Implementation** με τη μαθηματική τεκμηρίωση του Laplace Mechanism.
    * Προσθήκη **Custom Footer** για την ομοιομορφία του documentation.

####  Challenges & Solutions
* **Import Errors in Testing**: Αντιμετωπίστηκαν προβλήματα στα paths του `pytest` μέσω της προσθήκης του `sys.path.append` και της χρήσης του `__init__.py`.
* **Collaborative Sync**: Συντονισμός του handover μέσω δομημένων GitHub Comments, διασφαλίζοντας ότι τα μέλη της ομάδας έχουν σαφείς οδηγίες για το documentation.

####  Next Steps
1. **Athina (@Athina34)**: Οριστικοποίηση του **Privacy Map** (Sensitivity Δf) για τα datasets Adult, Loans και Salary στο Wiki (Issue #6).
2. **Vasilis (@BILLKNITOU)**: Σύνδεση των test results με την ενότητα **GDPR Accountability** στο Wiki.
3. **Dionysis (Tech Lead)**: Προετοιμασία του script της Φάσης 3 για την παραγωγή συγκριτικών γραφημάτων (Visualizations).


---


### 18/03/2026 | Phase 3: Team Integration & Final Repository Alignment (Team)

#### Tasks Accomplished
* Ολοκληρώθηκε και στην πράξη επιβεβαιώθηκε το agreed team workflow:
  * issue clarification
  * ξεχωριστό branch ανά task
  * local validation
  * draft PR review
  * merge μετά από team confirmation

* Έγινε merge το implementation του **Gaussian mechanism** (Issue #12 / PR #15).
* Έγινε merge το **README / terminology alignment** (Issue #13 / PR #16).
* Έγινε merge το **final sensitivity mapping / SME research update** (Issue #6 / PR #17).

#### Team Contribution Summary
* **Dionysis**: Gaussian implementation, validation, review coordination.
* **BILLKNITOU**: README cleanup, terminology alignment, documentation consistency.
* **Athina34**: final sensitivity mapping, research notebook update, bibliography support.

#### Outcome
* Το project υποστηρίζει πλέον καθαρά **Laplace** και **Gaussian** mechanisms.
* Το `README.md` είναι ευθυγραμμισμένο με το actual implemented state.
* Οι sensitivity τιμές για τα βασικά SME datasets έχουν οριστικοποιηθεί.
* Το board και το repository history παρέμειναν καθαρά και οργανωμένα.

#### Next Steps
1. Τελική προετοιμασία παρουσίασης και submission materials.
2. Έλεγχος συνοχής ανάμεσα σε code, documentation, research και GDPR analysis.


---


### 18/03/2026 | Phase 3: Final Issue Triage & Closeout Planning (Tech Lead)

#### Tasks Accomplished
* Άνοιξε το **Discussion #18** με θέμα τα **Known Limitations** και το **deferred work after current MVP alignment**, ώστε να καταγραφούν με καθαρό τρόπο τα άμεσα shortcomings και τα post-MVP items.
* Έγινε πρώτο triage των τελικών ενεργειών του project με σαφή διάκριση ανάμεσα σε:
  * current MVP closeout tasks,
  * documentation / setup cleanup,
  * και future backlog items.
* Δημιουργήθηκε το private project board **Final issues** για την οργάνωση των τελευταίων tasks της φάσης.
* Άνοιξε το **Issue #19**:
  * `[DOCS] Add Known Limitations and Utility Score explanation to Wiki`
* Άνοιξε το **Issue #20**:
  * `[TECH] Normalize requirements files and verify clean installation setup`
* Καταγράφηκε ως **draft / backlog** το μελλοντικό data-oriented item:
  * `[DATA] Explore automated sensitivity discovery for future Privacy Engine iterations`

#### Team Coordination
* Η **Athina34** επιβεβαίωσε στο discussion #18 ότι:
  * το **documentation alignment** είναι first-priority,
  * το **packaging / setup cleanup** είναι immediate issue,
  * και το **automated sensitivity discovery** ανήκει στο post-MVP scope.
* Με βάση αυτό, ορίστηκε καθαρό split ανάμεσα σε active issues και backlog.

#### Challenges & Solutions
* **Scope Clarity**: Υπήρχε ανάγκη να ξεχωρίσουμε με ακρίβεια τι ανήκει στο current MVP closeout και τι αποτελεί μελλοντική κατεύθυνση.
  * **Solution**: Δημιουργήθηκε dedicated discussion και ξεχωριστό final board, ώστε να μη μπερδευτούν implementation tasks με meta / planning items.
* **Project Closure Organization**: Χρειαζόταν πιο καθαρή παρακολούθηση για τα τελευταία tasks χωρίς να χαθεί η συνοχή με το υπάρχον workflow.
  * **Solution**: Τα active items μεταφέρθηκαν σε issue-driven μορφή και τα μεγαλύτερα future ideas έμειναν ως backlog / draft items.

#### Next Steps
1. **Athina34**: Ανάληψη και υλοποίηση του Wiki cleanup για `Known Limitations` και utility explanation (Issue #19).
2. **Dionysis (Tech Lead)**: Cleanup των `requirements.txt` / `requirements-dev.txt` και verification του installation flow (Issue #20).
3. Παρακολούθηση του `Final issues` board μέχρι το τελικό closeout της φάσης.
4. Μεταγενέστερη αξιολόγηση του draft item για automated sensitivity discovery σε επόμενο development cycle.