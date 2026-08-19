# Preprocessing Notes — Phase 2

> **Project**: Spam Email Detection  
> **Phase**: 2 — EDA & Text Preprocessing  
> Member 3 (Research Lead): Authored and maintains this document

---

## 1. Text Cleaning Pipeline (`src/preprocessing.py`)

### Steps Applied (in order)

| Step | Action | Tool / Method |
|------|--------|--------------|
| 1 | Lowercase the entire message | `str.lower()` |
| 2 | *(Optional)* Remove digits | `re.sub(r"\d+", " ", text)` |
| 3 | Tokenize | `nltk.word_tokenize()` |
| 4 | Remove English stop words | `nltk.corpus.stopwords` |
| 5 | Remove punctuation tokens | `str.maketrans` + translate |
| 6 | Lemmatize each token | `nltk.stem.WordNetLemmatizer` |
| 7 | Rejoin tokens | `" ".join(tokens)` |

### Why These Choices?

**Lemmatization over Stemming**  
`WordNetLemmatizer` produces grammatically valid English words
(e.g., "running" → "run", "better" → "good"). Stemming (Porter, Snowball)
produces truncated stems (e.g., "running" → "run", "studies" → "studi")
that are unreadable in WordCloud and top-words plots. Since interpretability
of EDA output is a project requirement, lemmatization is strictly superior
here.

**Stop-word removal before punctuation stripping**  
NLTK's `word_tokenize` preserves punctuation as separate tokens. Removing
stop words first (by string match) avoids accidentally keeping hyphenated
or apostrophe-containing stop words that the translator would partially
strip.

---

## 2. The `remove_numbers` Parameter: Why `False` by Default

The `clean_text(text, remove_numbers=False)` function deliberately keeps
digits and currency symbols by default. Rationale:

- **Digits are spam signals**: Common spam phrases include "WIN £1000",
  "call 0800 FREE NOW", "claim your £500 prize". Stripping digits before
  the model trains discards exactly the kind of evidence that makes spam
  distinguishable from ham.
- **Defensibility**: Making it a function parameter (not a hardcoded
  choice) means we can run an ablation test in Phase 3 — train once with
  `remove_numbers=False`, once with `True`, compare F1 on spam class, and
  report the result. This is a valid contribution to the methodology section.
- **Phase constraint**: The project spec explicitly says "Do not strip URLs,
  currency symbols, or numbers from text yet" in Phase 1. Phase 2 carries
  this forward by making it opt-in, not automatic.

---

## 3. Engineered Features (computed on RAW text, pre-split)

These features are computed deterministically per row — they do NOT fit on
the dataset distribution — so computing them before the train-test split
introduces **no leakage**.

| Feature | Type | Description | Spam signal? |
|---------|------|-------------|-------------|
| `msg_length_chars` | int | Total character count | ✅ Spam tends to be longer |
| `msg_length_words` | int | Word count (whitespace split) | ✅ Same pattern |
| `has_url` | int (0/1) | Regex: `http`, `https`, `www` present | ✅ Strong signal |
| `has_currency` | int (0/1) | Regex: `$`, `£`, `₹` present | ✅ Prize/offer language |
| `digit_count` | int | Count of digit characters | ✅ Phone numbers, codes |
| `digit_ratio` | float | digit_count / max(msg_length_chars, 1) | ✅ Proportion metric |
| `uppercase_word_count` | int | Words that are ALL CAPS | ✅ Urgency / shouting |
| `exclamation_count` | int | Count of `!` characters | ✅ Excitement / urgency |

> These columns are retained in `eda_ready.csv` so Phase 3 can test
> text-only vs. text + engineered features as separate ablation runs.

---

## 4. Class Imbalance — Observed Ratio

> Exact values populated after notebook execution. Approximate based on
> UCI dataset documentation:

| Class | Count (approx.) | Percentage (approx.) |
|-------|----------------|----------------------|
| ham | ~4,516 (post-dedup) | ~86.6 % |
| spam | ~653 (post-dedup) | ~13.4 % |

**Imbalance ratio**: approximately **6.9 : 1** (ham : spam).

**Implication for Phase 4**: Accuracy alone is a misleading metric.
A classifier that labels everything as "ham" achieves ~87% accuracy with
zero spam recall. We will prioritise **spam recall** and **F1 (weighted)**
as primary evaluation metrics. Class imbalance will be noted as a scope
limitation — oversampling (SMOTE) or class_weight adjustment are
out-of-scope stretch goals.

---

## 5. Key EDA Observations (for Report Section)

> To be populated / confirmed after running `notebooks/02_eda.ipynb`.

1. **Message length**: Spam messages are on average longer than ham
   messages in both character count and word count. This is visible in
   the violin/box plots and is consistent with published literature on
   the UCI SMS dataset.

2. **URL presence**: The proportion of messages containing a URL is
   substantially higher in the spam class than ham — URL presence is
   likely to be a highly weighted feature in both MNB and LR models.

3. **ALL-CAPS usage**: Uppercase word count shows a class-level
   difference: spam messages use more ALL-CAPS words, consistent with
   urgency-inducing language patterns.

4. **Top words**: The most frequent words in spam (after cleaning) include
   domain-specific terms like "free", "win", "prize", "call", "claim",
   "text" — strongly discriminative and expected to receive high TF-IDF
   weights. Ham top words are more conversational.

---

## 6. What Was NOT Done in Phase 2 (Deferred / Out of Scope)

| Item | Status |
|------|--------|
| TF-IDF / CountVectorizer fitting | ❌ Phase 3 only (inside Pipeline, after split) |
| `train_test_split` execution | ❌ Phase 3 only |
| SMOTE / oversampling | ❌ Out of scope (noted as limitation) |
| URL expansion / scraping | ❌ Out of scope |
| `remove_numbers=True` ablation | ⏳ Stretch goal for Phase 3 |
| Multilingual support | ❌ Out of scope |
