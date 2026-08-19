"""
src/nltk_setup.py
Spam Email Detection — NLTK resource bootstrap

Member 2 (NLP Specialist): Downloads NLTK corpora needed for Phase 2/3
preprocessing. Uses try/nltk.data.find to avoid re-downloading resources
that already exist locally. Safe to import and call multiple times.

Usage:
    from src.nltk_setup import ensure_nltk_resources
    ensure_nltk_resources()
"""

import nltk


# ── Resources required by the preprocessing pipeline ─────────────────────────
_REQUIRED_RESOURCES = [
    # (resource_path_for_find,         download_id)
    ("corpora/stopwords",              "stopwords"),
    ("corpora/wordnet",                "wordnet"),
    ("corpora/omw-1.4",                "omw-1.4"),
    ("tokenizers/punkt_tab",           "punkt_tab"),   # NLTK >= 3.8
    ("tokenizers/punkt",               "punkt"),       # fallback for older NLTK
]


def ensure_nltk_resources(quiet: bool = True) -> None:
    """
    Member 2 (NLP Specialist): Check for and download NLTK resources.
    Checks for existing local data first to avoid unnecessary downloads.

    Args:
        quiet: If True, suppress NLTK download output. Default True.
    """
    for find_path, download_id in _REQUIRED_RESOURCES:
        try:
            nltk.data.find(find_path)
            if not quiet:
                print(f"  [OK] {download_id} already present.")
        except LookupError:
            if not quiet:
                print(f"  [↓] Downloading {download_id} ...")
            nltk.download(download_id, quiet=quiet)


if __name__ == "__main__":
    print("Checking and downloading NLTK resources...")
    ensure_nltk_resources(quiet=False)
    print("Done.")
