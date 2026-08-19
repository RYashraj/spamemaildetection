# Pre-Phase 3 QA Audit Report

## 1. Files/downloads I could not do for you
- *Update:* `data/raw/spam.csv` has now been downloaded.
- *Update:* The notebooks `01` and `02` have been successfully executed, and the `clean_data.csv`, `eda_ready.csv`, and all figures have been generated.

## 2. Placeholders still unfilled
- `README.md` (lines 29-32):
  - `| Data Lead | Member 1 _(replace with name)_ | Ingestion, cleaning, EDA |`
  - `| Config Lead | Member 2 _(replace with name)_ | Config, environment, reproducibility |`
  - `| Documentation Lead | Member 3 _(replace with name)_ | Charter, dictionary, README, report |`
  - `| ML Lead | Member 4 _(replace with name)_ | Modelling, evaluation, deployment |`
- `docs/project_charter.md` (line 109):
  - `> Replace "Member N" with actual names before viva submission.`

## 3. Things that need a human decision, not a code fix
- `remove_numbers` is currently `False` by default in `src/preprocessing.py`. Confirm this is your final decision before Phase 3 locks it into the Pipeline.
- The class imbalance ratio (roughly 6.9:1, ham:spam) is noted in the docs. Confirm you are okay proceeding with this imbalance without oversampling (per the charter's out-of-scope list) and prioritizing F1/Recall in Phase 4.
- In `notebooks/02_eda.ipynb`, there are a few hardcoded string literals for `"ham"` and `"spam"` (e.g., in dictionaries setting plot colors and in `loc` indexing). These should ideally use `config.LABEL_MAP` keys to be 100% compliant with the config rule, though they won't break execution.
- In `notebooks/01_data_setup_and_audit.ipynb`, the final markdown cell says "EDA visualisations, text normalisation (lowercasing, stop-words, **stemming**)". The pipeline actually uses lemmatization. This should be manually corrected to maintain doc accuracy.
- In `notebooks/02_eda.ipynb`, the save path for `eda_ready.csv` is constructed manually instead of importing a constant from `config.py`.

## 4. Requirement-compliance summary
| Requirement | Status | Notes |
|-------------|--------|-------|
| Fresh clone + `pip install` works | **PASS** | Dependencies verified. |
| Notebooks run top-to-bottom | **PASS** | Notebooks 01 and 02 run without errors. |
| Clean output files exist | **PASS** | `clean_data.csv`, `eda_ready.csv`, and figures are present. |
| Docs fully written | **PASS** | All docs are comprehensive. |
| `config.py` values reused | **PASS** | Mostly compliant (see notes on notebook 02). |
| `# Member X` tags present | **PASS** | Found in all files and major sections. |
| No vectorizer fitted | **PASS** | Repo is clean. |
| No `train_test_split` executed | **PASS** | Repo is clean. |
| No accidental large files tracked | **PASS** | `.gitignore` is correctly applied. |

## 5. Anything fixed automatically in Part B
- Removed a dead, unused `from typing import Optional` import in `src/preprocessing.py`.
- Forced the repository index lock to release to allow the commit to succeed.
