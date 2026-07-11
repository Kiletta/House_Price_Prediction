"""Paths, constants, column names, and display settings for the project."""

from pathlib import Path
import os

# ── Project root ──────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ── Data paths ────────────────────────────────────────────────────────────────
RAW_DATA = PROJECT_ROOT / "data" / "dataset_2.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
CLEAN_DATA = PROCESSED_DIR / "data_clean.csv"
FEATURES_DATA = PROCESSED_DIR / "data_features.csv"
FEATURE_LIST = PROCESSED_DIR / "feature_list.json"
METADATA = PROCESSED_DIR / "metadata.json"

# ── Output paths ──────────────────────────────────────────────────────────────
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
EDA_REPORT = OUTPUTS_DIR / "eda_report.md"
STATS_REPORT = OUTPUTS_DIR / "statistical_findings.md"
MODEL_RESULTS = OUTPUTS_DIR / "model_results.csv"
FEATURE_IMPORTANCE = OUTPUTS_DIR / "feature_importance.csv"
FINAL_REPORT = OUTPUTS_DIR / "final_report.md"

# ── Source / model paths ─────────────────────────────────────────────────────
MODELS_DIR = PROJECT_ROOT / "src" / "models"

# ── Column names ──────────────────────────────────────────────────────────────
AREA = "Area_SqFt"
ROOMS = "Rooms"
BUILD_YEAR = "Build_Year"
LOCATION = "Location"
STREET_TYPE = "Street_Type"
FURNISHING = "Furnishing"
PROPERTY_TYPE = "Property_Type"
HAS_POOL = "Has_Pool"
PRICE = "Price"

ALL_COLUMNS = [AREA, ROOMS, BUILD_YEAR, LOCATION, STREET_TYPE,
               FURNISHING, PROPERTY_TYPE, HAS_POOL, PRICE]

NUMERIC_COLUMNS = [AREA, ROOMS, BUILD_YEAR, PRICE]
CATEGORICAL_COLUMNS = [LOCATION, STREET_TYPE, FURNISHING, PROPERTY_TYPE, HAS_POOL]

# ── Valid categories ──────────────────────────────────────────────────────────
VALID_LOCATIONS = {"Noida", "Kanpur", "Prayagraj", "Delhi",
                   "Lucknow", "Jaipur", "Indore", "Gurugram"}
VALID_STREET_TYPES = {"Highway Facing", "Residential Lane", "Main Road",
                      "Corner Plot", "Gated Society"}
VALID_FURNISHING = {"Furnished", "Semi-Furnished", "Unfurnished"}
VALID_PROPERTY_TYPES = {"Apartment", "Independent House", "Duplex", "Villa"}
VALID_POOL_VALUES = {"Yes", "No"}

# ── Validation ranges ─────────────────────────────────────────────────────────
BUILD_YEAR_MIN = 1985
BUILD_YEAR_MAX = 2024
AREA_OUTLIER_THRESHOLD = 5500  # sqft

# ── Display ───────────────────────────────────────────────────────────────────
PALETTE = "Set2"
FIGSIZE = (10, 6)
DPI = 300

# ── Modeling ───────────────────────────────────────────────────────────────────
TEST_SIZE = 0.2
RANDOM_STATE = 42
