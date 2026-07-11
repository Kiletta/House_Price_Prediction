# Analysis Framework — House Price Prediction

A structured, repeatable framework for analyzing the Indian Residential Property Price Dataset.  
Follow these phases in order for any analysis direction you choose (prediction, segmentation, amenity premium, or luxury deep-dive).

---

## Table of Contents

1. [Phase 1: Environment & Data Loading](#phase-1-environment--data-loading)
2. [Phase 2: Data Quality & Cleaning](#phase-2-data-quality--cleaning)
3. [Phase 3: Exploratory Data Analysis (EDA)](#phase-3-exploratory-data-analysis-eda)
4. [Phase 4: Feature Engineering](#phase-4-feature-engineering)
5. [Phase 5: Statistical Analysis](#phase-5-statistical-analysis)
6. [Phase 6: Modeling](#phase-6-modeling)
7. [Phase 7: Interpretation & Reporting](#phase-7-interpretation--reporting)
8. [Utility Modules](#utility-modules)
9. [Checklist & Sign-off](#checklist--sign-off)

---

## Phase 1: Environment & Data Loading

**Goal**: Ensure reproducible environment, load raw data, and establish project paths.

### Steps

1. **Check dependencies** — verify `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`, `scikit-learn` are installed.
2. **Load data** — read `data/dataset_2.csv` with `pd.read_csv()`. Use `Path` from `pathlib` for cross-platform paths.
3. **Initial shape & dtypes** — confirm 1,124 rows × 9 columns. Cast `Build_Year` to int, `Has_Pool` to bool.
4. **Snapshot** — save a `data/processed/metadata.json` with row count, column list, dtypes, and timestamp.

### Outputs

- `data/dataset_2.csv` — raw data (untouched)
- `data/processed/` — all cleaned/engineered data lives here

---

## Phase 2: Data Quality & Cleaning

**Goal**: Handle missing values, check for errors, produce a clean copy.

### Steps

1. **Missing value audit**
   - 33 missing in `Area_SqFt`, 33 in `Rooms`, 33 in `Furnishing` — confirm they don't overlap.
   - **Imputation strategy** (choose one):
     - *Median/mode* (simple): median `Area_SqFt`, median `Rooms`, mode `Furnishing`.
     - *Model-based* (advanced): predict `Area_SqFt` from `Rooms` + `Property_Type`, etc.
   - Tag imputed rows with a `_imputed` boolean column per field.

2. **Outlier identification**
   - `Area_SqFt` > 5,500 sqft (≈10 properties) — flag but don't remove.
   - `Price` — check distribution; look for listings below ₹250K or above ₹2M.
   - Decide: cap, transform (log), or segment separately.

3. **Validate fields**
   - `Build_Year` ∈ [1985, 2024]
   - `Location` ∈ {Noida, Kanpur, Prayagraj, Delhi, Lucknow, Jaipur, Indore, Gurugram}
   - `Has_Pool` ∈ {Yes, No}
   - No negative `Area_SqFt` or `Rooms`.

4. **Save cleaned data**
   - `data/processed/data_clean.csv`

### Decision Log

| Decision | Chosen Option | Rationale |
|---|---|---|
| `Area_SqFt` imputation | | |
| `Rooms` imputation | | |
| `Furnishing` imputation | | |
| Outlier treatment | | |

*Fill this as you go — it becomes the "data processing" section of your final report.*

---

## Phase 3: Exploratory Data Analysis (EDA)

**Goal**: Understand distributions, correlations, and group patterns in the data.

### A. Univariate Analysis

- **Price** — histogram + KDE; check skewness, kurtosis.
- **Area_SqFt** — histogram + KDE; note right-skew.
- **Rooms** — bar chart (discrete distribution).
- **Build_Year** — histogram + KDE.
- **Categoricals** — count plots for `Location`, `Property_Type`, `Furnishing`, `Street_Type`, `Has_Pool`.

### B. Bivariate Analysis

| X (feature) | Y (target) | Plot | Statistic |
|---|---|---|---|
| `Area_SqFt` | `Price` | scatter + reg line | Pearson r = 0.86 |
| `Rooms` | `Price` | boxplot per room count | Spearman ρ |
| `Location` | `Price` | boxplot / violin | ANOVA F-stat |
| `Property_Type` | `Price` | boxplot | ANOVA |
| `Furnishing` | `Price` | boxplot | ANOVA |
| `Street_Type` | `Price` | boxplot | ANOVA |
| `Has_Pool` | `Price` | boxplot | t-test |
| `Build_Year` | `Price` | scatter | Pearson r = 0.11 |

### C. Multivariate Analysis

- **Price per sqft** by city + property type (heatmap or grouped bar).
- **Correlation matrix** (numeric features only).
- **Pairplot** of `Price`, `Area_SqFt`, `Rooms`, `Build_Year` — colored by `Location`.
- **Interaction plot**: does the `Area_SqFt` → `Price` slope differ by `Property_Type`?

### D. Key Questions from the Readme

1. Is the Build_Year → Price relationship hiding a non-linear effect?
2. Is the pool premium real or just a proxy for larger / premium properties?
3. Does the Gated Society premium hold after controlling for area?
4. Are Villas genuinely overpriced, or just larger on average?

### Outputs

- `outputs/figures/` — all plots saved as PNG.
- `outputs/eda_report.md` — summary stats and key findings.

---

## Phase 4: Feature Engineering

**Goal**: Create features that capture non-linear/complex relationships.

### Suggested Features

1. **Price per sqft** — `Price / Area_SqFt` (normalized value metric).
2. **Age** — `2024 - Build_Year` (linear age in years).
3. **Age_bracket** — binned age categories (e.g., 0–5, 6–15, 16–25, 26–39).
4. **Has_Pool_numeric** — `1` if Yes, `0` if No.
5. **Rooms_sqft_interaction** — `Area_SqFt * Rooms` (catch interplay).
6. **Property_Type_encoded** — one-hot or ordinal.
7. **Location_encoded** — one-hot or target-encoded.
8. **Street_Type_encoded** — one-hot.
9. **Is_large_property** — binary flag for Area_SqFt > 75th percentile.
10. **Log_Price** — `log(Price)` for models assuming normality.
11. **Log_Area** — `log(Area_SqFt)` to handle right skew.

### Outputs

- `data/processed/data_features.csv`
- `data/processed/feature_list.json` — names, types, descriptions

---

## Phase 5: Statistical Analysis

**Goal**: Formal hypothesis tests and confidence intervals.

### Tests to Run

1. **Global ANOVA** — do mean prices differ by city? By property type?
2. **Pairwise t-tests** (with Bonferroni correction) — which city pairs are significantly different?
3. **ANCOVA** — does the Area–Price slope differ by property type or city? (interaction test)
4. **Variance Inflation Factor (VIF)** — check multicollinearity among numeric features.
5. **Shapiro-Wilk** — normality test on Price (expect reject — motivates log transform).

### Outputs

- Written up in `outputs/statistical_findings.md`
- Significant results flagged for the modeling phase.

---

## Phase 6: Modeling

**Goal**: Build and compare models to predict `Price`.

### Train / Test Split

- 80/20 stratified split (strata = `Location` to keep city balance in both sets).
- Scale numeric features (StandardScaler or RobustScaler — robust is better if keeping outliers).

### Candidate Models

| Model | Strengths | When to Choose |
|---|---|---|
| **Linear Regression** | Baseline, interpretable | Strong linear relationships, low multicollinearity |
| **Ridge / Lasso** | Handles multicollinearity, feature selection | 10+ features, correlated predictors |
| **Decision Tree** | Non-linear, interactions | If you suspect non-linear effects like age |
| **Random Forest** | Best default ensemble, feature importance | Typically the strongest out-of-the-box |
| **Gradient Boosting (XGBoost / LightGBM)** | State-of-the-art for tabular data | After Random Forest, if you need higher accuracy |

### Evaluation Metrics

- **R²** — variance explained
- **RMSE** — absolute error in ₹
- **MAE** — median error in ₹
- **MAPE** — percentage error (useful for non-technical audience)
- **Residual plots** — check for homoscedasticity

### Feature Importance

- Extract and rank by:
  - Linear: coefficient magnitudes (standardized)
  - Tree: impurity-based or SHAP values

### Outputs

- `src/models/` — saved model artifacts (`.pkl`)
- `outputs/model_results.csv` — metrics for all models
- `outputs/feature_importance.csv`

---

## Phase 7: Interpretation & Reporting

**Goal**: Translate results into actionable insights.

### Deliverables

1. **Summary report** (`outputs/final_report.md`)
   - Executive summary (one paragraph for a general audience)
   - Key drivers of price (ranked)
   - City-level price differences (with confidence)
   - Model performance (in plain language)
   - Limitations & caveats

2. **Visual dashboard** (optional)
   - Matplotlib figures or an interactive HTML (Plotly)

3. **Presentation deck** (optional)
   - Key charts + talking points

### Cheat Sheet — Which Question Needs What

| Question | Analysis Phase | Key Output |
|---|---|---|
| What drives house prices? | EDA + Modeling | Feature importance ranking |
| Which city is cheapest/most expensive? | EDA (bivariate) + Stats | City mean prices + CI |
| Is a pool worth the investment? | Model coefficients (with controls) | Pool coefficient in log-price model = % premium |
| Are older homes cheaper? | EDA + Feature Engineering | Age vs. price scatter, non-linear check |
| Can I predict a price from a few inputs? | Modeling | Best model + RMSE |
| Are luxury properties a different market? | Modeling (segment) | Separate model for >5,500 sqft |

---

## Utility Modules

The `src/` directory contains reusable Python modules:

| Module | Purpose |
|---|---|
| `src/config.py` | Paths, constants, column names, color palettes |
| `src/loader.py` | Data loading & initial validation |
| `src/cleaning.py` | Imputation, outlier handling, validation |
| `src/eda.py` | Distribution plots, correlation matrices, summary tables |
| `src/features.py` | Feature engineering functions |
| `src/stats.py` | Statistical tests helper |
| `src/models.py` | Model training, evaluation, comparison |
| `src/report.py` | Generate markdown reports from results |
| `src/utils.py` | Common utilities (dir setup, logging, timing) |

Each module has a single responsibility. Notebooks import from `src/` rather than duplicating code.

---

## Checklist & Sign-off

Use this to track your progress:

- [ ] Phase 1: Environment ready, data loaded
- [ ] Phase 2: Missing values handled, data cleaned
- [ ] Phase 3: EDA complete with saved figures
- [ ] Phase 4: Engineered features created
- [ ] Phase 5: Statistical tests run and documented
- [ ] Phase 6: Models built, evaluated, compared
- [ ] Phase 7: Final report generated and reviewed
- [ ] All figures saved to `outputs/figures/`
- [ ] All data saved to `data/processed/`
- [ ] Notebooks are clean, sequential, and commented

---

## Quick Start

```python
# 1. Load
from src.loader import load_data
df = load_data("data/dataset_2.csv")

# 2. Clean
from src.cleaning import clean_data
df_clean = clean_data(df)

# 3. Explore (in a notebook)
from src.eda import plot_price_dist, correlation_heatmap
plot_price_dist(df_clean)
correlation_heatmap(df_clean)

# 4. Feature engineer
from src.features import create_features
df_feat = create_features(df_clean)

# 5. Model
from src.models import train_and_evaluate
results = train_and_evaluate(df_feat, target="Price")
