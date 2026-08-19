# Data Directory

## Raw Data (`data/raw/`)

The raw dataset is **not committed** to this repository because it exceeds
recommended GitHub single-file size guidelines and contains a redistributable
corpus (cite the original source when sharing).

### Dataset: UCI SMS Spam Collection

| Field | Value |
|-------|-------|
| **Name** | SMS Spam Collection |
| **Source** | [UCI ML Repository](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) |
| **Kaggle mirror** | <https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset> |
| **License** | Creative Commons Attribution 4.0 (CC BY 4.0) |
| **Size** | ~5,572 rows, 2 meaningful columns |
| **Original columns** | `v1` (label: `ham`/`spam`), `v2` (raw SMS text) |

### Manual Download Steps

1. Visit the Kaggle page above (free account required) **or** the UCI link.
2. Download `spam.csv`.
3. Place the file at **`data/raw/spam.csv`** (exactly this name and path).
4. Do **not** rename columns — the ingestion script handles renaming.
5. Verify the file is present before running any notebook.

> **Note**: `data/raw/*.csv` is listed in `.gitignore`. Your local copy will
> not be staged or committed accidentally.

## Processed Data (`data/processed/`)

`clean_data.csv` is generated automatically by
`notebooks/01_data_setup_and_audit.ipynb`.  
It is committed to version control (small, derived, reproducible).
