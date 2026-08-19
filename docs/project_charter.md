# Project Charter — Spam Email Detection

> **Course**: Python for Data Science (PDS)  
> **Phase**: 1 — Project Setup & Dataset Audit  
> Member 3 (Documentation Lead): Authored and maintains this charter

---

## 1. Problem Statement

Spam messages — unsolicited, often deceptive or malicious text — are a
persistent nuisance and security threat. Manual filtering is neither scalable
nor reliable. This project builds a **binary text classifier** that
automatically distinguishes between legitimate messages ("ham") and spam using
classical machine learning techniques applied to the UCI SMS Spam Collection
dataset.

Although titled "Spam Email Detection" for assignment purposes, the dataset
contains SMS text messages. The classification methodology (bag-of-words
features + probabilistic / linear classifiers) directly transfers to email
body text, making this a valid pedagogical proxy. See `docs/data_dictionary.md`
for the full scope note.

---

## 2. Objectives

1. **Build a reproducible ML pipeline** from raw data to evaluated model,
   following a five-phase structure (Setup → EDA → Modelling → Evaluation → Deployment).
2. **Achieve high recall on spam class** — missing a spam message (false negative)
   is more costly than a false alarm (false positive) in most use-cases.
3. **Compare two classifiers** (Multinomial Naive Bayes vs. Logistic Regression)
   on accuracy, precision, recall, F1, and ROC-AUC.
4. **Produce interpretable results** — feature importance / coefficient plots,
   confusion matrices, and plain-language write-ups accessible to a non-technical audience.
5. **Document every decision** so the project is reproducible end-to-end by
   a fresh team member from a single `README.md`.

---

## 3. Scope

### In Scope

| Item | Notes |
|------|-------|
| Binary classification (ham / spam) | Primary deliverable |
| SMS text pre-processing (Phase 2) | Tokenisation, stop-word removal, stemming |
| TF-IDF vectorisation (Phase 3) | Sparse matrix representation |
| Multinomial Naive Bayes model | Primary model |
| Logistic Regression model | Baseline / comparison model |
| Model evaluation & comparison (Phase 4) | Confusion matrix, classification report, ROC curve |
| Optional Streamlit demo (Phase 5) | Lightweight interactive interface if time permits |
| Exploratory Data Analysis (Phase 2) | Word clouds, length distributions, class balance plots |

### Out of Scope

| Item | Reason excluded |
|------|----------------|
| **Deep learning** (LSTM, BERT, Transformers) | Beyond course scope; compute-intensive |
| **Live email inbox access** (IMAP/Gmail API) | Security, authentication complexity |
| **Attachment scanning** | Raw email structure absent from dataset |
| **Multilingual support** | Dataset is English-only; multilingual NLP requires separate corpora |
| **SVM / SVC as a third model** | May be added only if Phases 1–4 complete ahead of schedule |
| **Hyperparameter tuning (Grid/RandomSearchCV)** | Optional stretch goal — not in primary plan |
| **Production deployment** | Streamlit demo is a prototype, not production-grade |

---

## 4. Shortlisted Algorithms

### 4.1 Multinomial Naive Bayes (Primary Model)

> Member 4 (ML Lead): Rationale and implementation ownership

Multinomial Naive Bayes (MNB) is the canonical algorithm for text
classification with bag-of-words / TF-IDF features. Its probabilistic
foundation — modelling word-count distributions per class — maps directly onto
the spam-detection problem: spam messages tend to use a distinct, high-frequency
vocabulary ("free", "win", "prize", "claim") that MNB can capture with very
few training examples. It is computationally lightweight, interpretable (class
log-probabilities are easily inspected), and robust on short texts like SMS,
making it the natural primary choice for this project.

### 4.2 Logistic Regression (Baseline / Comparison Model)

> Member 4 (ML Lead): Rationale and implementation ownership

Logistic Regression (LR) is a strong linear baseline for high-dimensional
sparse text feature spaces. Unlike MNB, LR optimises a discriminative
objective and can assign negative weights to "ham-indicating" words, providing
a richer decision boundary. Its coefficients are directly interpretable as
log-odds contributions per feature, making it excellent for post-hoc
explanation. Running LR alongside MNB lets us isolate whether generative
(MNB) or discriminative (LR) assumptions yield better spam recall on this
dataset — a standard diagnostic comparison in academic NLP work.

---

## 5. Team & Roles

| Member | Role | Primary Responsibility |
|--------|------|----------------------|
| Member 1 | Data Lead | Dataset ingestion, QC, cleaning (Phase 1–2) |
| Member 2 | Config Lead | Config, environment, reproducibility (Phase 1, 3) |
| Member 3 | Documentation Lead | Charter, dictionary, README, report (all phases) |
| Member 4 | ML Lead | Modelling, evaluation, visualisation (Phase 3–4) |

> Replace "Member N" with actual names before viva submission.

---

## 6. Phase Plan

| Phase | Title | Owner | Status |
|-------|-------|-------|--------|
| 1 | Project Setup & Dataset Audit | All | ✅ In Progress |
| 2 | EDA & Text Pre-processing | Member 1, Member 3 | ⏳ Pending |
| 3 | Feature Engineering & Modelling | Member 2, Member 4 | ⏳ Pending |
| 4 | Evaluation & Comparison | Member 4 | ⏳ Pending |
| 5 | Deployment (Streamlit demo) | Member 3, Member 4 | ⏳ Pending |

---

## 7. Constraints & Assumptions

- The dataset is assumed to be the standard UCI SMS Spam Collection (5,572 rows).
- `RANDOM_STATE = 42` is fixed project-wide via `config.py`.
- All notebooks must run top-to-bottom without manual intervention after
  placing `spam.csv` in `data/raw/`.
- No modelling artefacts (`.pkl`, `.joblib`) are committed to git; they are
  generated locally and optionally stored via DVC or shared separately.
