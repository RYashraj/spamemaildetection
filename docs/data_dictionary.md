# Data Dictionary — Spam Email Detection Project

> **Dataset**: UCI SMS Spam Collection  
> **Phase**: 1 — Project Setup & Dataset Audit  
> Member 1 (Data Lead): Authored and maintained this dictionary

---

## 1. Source & Citation

| Field | Detail |
|-------|--------|
| **Name** | SMS Spam Collection v.1 |
| **Repository** | [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) |
| **Kaggle Mirror** | <https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset> |
| **Original Authors** | Tiago A. Almeida & José María Gómez Hidalgo |
| **License** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Citation** | Almeida, T.A., Gómez Hidalgo, J.M., Yamakami, A. (2011). *Contributions to the study of SMS spam filtering: new collection and results*. DOCENG'11. |
| **Download date** | (fill in when you download) |

---

## 2. ⚠️ Important Scope Note: SMS Data, Not Email

> **This project is titled "Spam Email Detection" for assignment purposes.**  
> The underlying dataset contains **SMS (Short Message Service) text messages**,
> not raw email content with headers, MIME parts, or attachments.  
>
> Implications:
> - Messages are short (typically < 160 characters), unlike email bodies.
> - There are no email headers (`From:`, `Subject:`, `To:`, `MIME-Version:`, etc.).
> - No attachments, URLs embedded in HTML, or styling artefacts are present.
> - Techniques like header-based filtering or attachment scanning are **out of scope**.
> - The classification approaches (Naive Bayes, Logistic Regression) transfer
>   directly to email text bodies, which justifies using this dataset as a
>   pedagogical stand-in.

---

## 3. Raw File Structure (`data/raw/spam.csv`)

The raw file uses `encoding='latin-1'` and contains the following columns:

| Column | Original Name | Type | Description |
|--------|--------------|------|-------------|
| Class label | `v1` | string | `"ham"` (legitimate) or `"spam"` |
| Message text | `v2` | string | Raw SMS text content |
| Unnamed: 2 | `Unnamed: 2` | mostly NaN | Artefact of CSV export — dropped |
| Unnamed: 3 | `Unnamed: 3` | mostly NaN | Artefact of CSV export — dropped |
| Unnamed: 4 | `Unnamed: 4` | mostly NaN | Artefact of CSV export — dropped |

---

## 4. Cleaned File Structure (`data/processed/clean_data.csv`)

Produced by `notebooks/01_data_setup_and_audit.ipynb`. Columns after cleaning:

| Column | Dtype | Description | Values |
|--------|-------|-------------|--------|
| `label` | object (str) | String class label | `"ham"`, `"spam"` |
| `message` | object (str) | Raw SMS text (unchanged from source) | Free text |
| `label_num` | int64 | Numeric encoding of `label` | `0` = ham, `1` = spam |

---

## 5. Class Distribution (post-cleaning)

> Exact counts are populated after running the notebook. Approximate values
> based on the published dataset:

| Class | String | Numeric | Count (approx.) | Percentage (approx.) |
|-------|--------|---------|-----------------|----------------------|
| Legitimate | `ham` | `0` | ~4,825 | ~86.6 % |
| Spam | `spam` | `1` | ~747 | ~13.4 % |

**Note**: The dataset is **imbalanced** (~87% ham / ~13% spam). This is
addressed in Phase 3 (modelling) — not corrected here.

---

## 6. Cleaning Steps Applied (Phase 1)

| Step | Detail | Applied by |
|------|--------|-----------|
| Encoding | Loaded with `encoding='latin-1'` to handle extended characters | Member 1 |
| Drop junk columns | `Unnamed: 2`, `Unnamed: 3`, `Unnamed: 4` dropped | Member 1 |
| Column rename | `v1 → label`, `v2 → message` | Member 1 |
| Missing value check | Verified 0 nulls in `label` and `message` after rename | Member 1 |
| Duplicate removal | Exact-duplicate rows detected and dropped; counts logged | Member 1 |
| Label encoding | `label` mapped to `label_num` via `LABEL_MAP` in `config.py` | Member 2 |

---

## 7. Explicitly NOT Done in Phase 1

The following text normalisation steps are **deferred to Phase 2** and are
deliberately absent from this cleaning pass:

- URL removal / replacement
- Currency symbol and number stripping
- Punctuation removal
- Stop-word filtering
- Stemming / lemmatisation
- Case normalisation

Raw text statistics (lengths, character counts) are logged in the notebook
for reference, but the `message` column is untouched.
