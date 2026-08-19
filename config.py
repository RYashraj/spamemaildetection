# =============================================================================
# config.py
# Spam Email Detection — Project-wide configuration constants
#
# Member 2 (Config Lead): All reproducibility-critical constants are defined
# here and imported everywhere else. Nothing is hardcoded in notebooks or src/.
# =============================================================================

# ── Reproducibility ───────────────────────────────────────────────────────────
RANDOM_STATE: int = 42          # Seed for all random operations (sklearn, numpy)
TEST_SIZE: float = 0.20         # 80/20 train-test split — configured here,
                                # executed only in Phase 3 (train_test_split)

# ── File paths ────────────────────────────────────────────────────────────────
RAW_DATA_PATH: str = "data/raw/spam.csv"
PROCESSED_DATA_PATH: str = "data/processed/clean_data.csv"

# ── Label encoding ────────────────────────────────────────────────────────────
# Maps string labels (as they appear in the UCI dataset) to binary integers.
# Used in Phase 1 QC and Phase 3 modelling — never re-defined elsewhere.
LABEL_MAP: dict = {
    "ham": 0,
    "spam": 1,
}

# ── Column names (post-rename) ────────────────────────────────────────────────
LABEL_COL: str = "label"          # String class column (ham / spam)
LABEL_NUM_COL: str = "label_num"  # Numeric class column (0 / 1)
TEXT_COL: str = "message"         # Raw SMS text column
