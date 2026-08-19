"""
src/preprocessing.py
Spam Email Detection — Text cleaning pipeline

Member 2 (NLP Specialist): Defines clean_text(), the project's canonical
text normalisation function. Applied in Phase 2 to create the
clean_message column; reused unchanged in Phase 3 inside the sklearn
Pipeline to avoid train/test leakage.

Design decisions (defensible in viva):
- remove_numbers=False by default: digits and currency symbols are strong
  spam signals ("WIN £1000", "call 0800..."); stripping them by default
  would discard discriminative information before we know it helps.
- Lemmatization over stemming: produces real English words, which makes
  WordCloud and top-words EDA interpretable without post-processing.
- Punctuation removed AFTER stop-word removal to avoid tokenizer quirks.
"""

import re
import string
from typing import Optional

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from src.nltk_setup import ensure_nltk_resources

# ── One-time NLTK resource check ──────────────────────────────────────────────
ensure_nltk_resources(quiet=True)

# ── Module-level singletons (avoid re-instantiating on every call) ────────────
_LEMMATIZER = WordNetLemmatizer()
_STOP_WORDS: set = set(stopwords.words("english"))
_PUNCT_TABLE = str.maketrans("", "", string.punctuation)


def clean_text(text: str, remove_numbers: bool = False) -> str:
    """
    Member 2 (NLP Specialist): Canonical text cleaning function.

    Pipeline:
        1. Lowercase
        2. (Optional) Strip digits
        3. Tokenize with nltk.word_tokenize
        4. Remove English stop words
        5. Remove punctuation tokens
        6. Lemmatize each token (WordNetLemmatizer)
        7. Rejoin tokens into a single string

    Args:
        text: Raw input string (SMS message).
        remove_numbers: If True, strip digit characters before tokenization.
                        Default False — numbers are spam signals (see module
                        docstring).

    Returns:
        A single cleaned string ready for TF-IDF vectorisation in Phase 3.
    """
    if not isinstance(text, str):
        return ""

    # Step 1: Lowercase
    text = text.lower()

    # Step 2: (Optional) Remove digits
    if remove_numbers:
        text = re.sub(r"\d+", " ", text)

    # Step 3: Tokenize
    tokens = word_tokenize(text)

    # Steps 4 & 5: Remove stop words and punctuation
    tokens = [
        tok.translate(_PUNCT_TABLE)
        for tok in tokens
        if tok not in _STOP_WORDS
    ]
    # Drop tokens that became empty after punctuation removal
    tokens = [tok for tok in tokens if tok.strip()]

    # Step 6: Lemmatize
    tokens = [_LEMMATIZER.lemmatize(tok) for tok in tokens]

    # Step 7: Rejoin
    return " ".join(tokens)


def apply_cleaning(
    series,
    remove_numbers: bool = False,
    verbose: bool = True,
) -> "pd.Series":  # type: ignore[name-defined]
    """
    Member 2 (NLP Specialist): Vectorised wrapper to apply clean_text
    to a pandas Series.

    Args:
        series: pandas Series of raw message strings.
        remove_numbers: Passed through to clean_text.
        verbose: Print progress stats after cleaning.

    Returns:
        pandas Series of cleaned strings.
    """
    import pandas as pd  # local import — avoids hard dep at module level

    cleaned = series.apply(lambda x: clean_text(x, remove_numbers=remove_numbers))

    if verbose:
        null_count = cleaned.isnull().sum()
        empty_count = (cleaned == "").sum()
        print(f"  Cleaning complete: {len(cleaned):,} rows processed.")
        print(f"  Nulls after cleaning : {null_count}")
        print(f"  Empty strings        : {empty_count}")
        if empty_count > 0:
            print("  ⚠ Some messages became empty after cleaning — review source rows.")

    return cleaned
