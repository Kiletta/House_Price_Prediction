# Indian Residential Property Price Dataset

A structured dataset of residential property listings across eight Indian cities, built for price-driver analysis and predictive modeling. This README documents the data, its quality, early patterns, and the recommended direction for analysis.

## 1. Dataset at a Glance

| | |
|---|---|
| **File** | `dataset_2.csv` |
| **Rows** | 1,124 listings |
| **Columns** | 9 |
| **Duplicates** | None |
| **Missing values** | 33 each in `Area_SqFt`, `Rooms`, `Furnishing` (independent, not the same rows) |
| **Cities covered** | Noida, Kanpur, Prayagraj, Delhi, Lucknow, Jaipur, Indore, Gurugram |
| **Build years** | 1985 – 2024 |
| **Price range** | ₹248,640 – ₹2,071,402 |

## 2. Data Dictionary

| Column | Type | Description | Notes |
|---|---|---|---|
| `Area_SqFt` | float | Built-up area in square feet | 700 – 10,267; right-skewed, a handful of large outliers (>6,000 sqft) |
| `Rooms` | float | Number of rooms | Range 2–7, fairly evenly distributed |
| `Build_Year` | int | Year the property was built | 1985–2024, no missing values |
| `Location` | string | City | 8 categories, roughly balanced (127–156 listings each) |
| `Street_Type` | string | Street/plot classification | Highway Facing, Residential Lane, Main Road, Corner Plot, Gated Society |
| `Furnishing` | string | Furnishing status | Furnished, Semi-Furnished, Unfurnished |
| `Property_Type` | string | Property category | Apartment, Independent House, Duplex, Villa |
| `Has_Pool` | string (Yes/No) | Whether the property has a pool | 297 Yes / 827 No |
| `Price` | float | Listing price (target variable) | No missing values |

## 3. Data Quality Notes

- **Missingness is independent**, not clustered — the 33 nulls in `Area_SqFt`, `Rooms`, and `Furnishing` do not overlap in the same rows, so a single "incomplete listing" explanation doesn't hold; each needs its own handling (e.g. median/mode imputation or model-based imputation) rather than a blanket row drop.
- **No exact duplicate rows.**
- **Area outliers**: most listings sit under 3,000 sqft, but ~10 properties exceed 5,500 sqft (up to 10,267 sqft), mostly Villas and Independent Houses. These are legitimate large properties, not obvious data errors, but they pull averages and regression coefficients — worth flagging or treating as a separate segment rather than discarding outright.
- **Price per sqft** ranges from ₹144 to ₹538, averaging ₹281 — a useful normalized field for cross-city comparison once you control for size.

## 4. Early Patterns Worth Investigating Further

These are first-pass signals from the raw data, not final conclusions — the framework in `ANALYSIS_FRAMEWORK.md` is built to test and deepen each of these.

- **Area is the dominant price driver** — correlation of 0.86 with Price, far ahead of Rooms (0.21) and Build_Year (0.11).
- **City matters**: Delhi (avg ₹667,981) and Gurugram (avg ₹655,687) command the highest prices; Prayagraj (avg ₹567,968) and Kanpur (avg ₹570,913) the lowest — roughly a 17% spread between top and bottom city.
- **Property type matters**: Villas average ₹705,290 vs. Apartments at ₹573,034 — about a 23% premium.
- **Furnishing adds value**: Furnished properties average ₹631,178 vs. Unfurnished at ₹584,549.
- **Gated Society street type** carries the highest average price among street types (₹642,344), ahead of Highway Facing (₹597,058) — counter to an assumption that highway-facing commercial accessibility would dominate.
- **Pool effect is modest**: ₹628,807 (with pool) vs. ₹600,801 (without) — a smaller premium than property type or location, suggesting it's a secondary amenity rather than a core price driver.
- **Build year shows almost no linear relationship with price** (0.11) — worth checking for a non-linear effect (e.g. very old heritage properties or very new builds priced differently) rather than ruling out age entirely.

## 5. Suggested Project Directions

Pick one as a focused deliverable rather than trying to cover all of them:

1. **Price prediction model** — regression (linear, then tree-based) using Area, Rooms, Location, Property_Type, Furnishing, Street_Type as features. Good candidate for a clean, presentable ML project with feature importance as the headline insight.
2. **Market segmentation / city comparison** — a policy- or buyer-facing analysis of what drives price differences between cities, useful if you want a data-for-good or housing-affordability framing.
3. **Amenity premium analysis** — isolate the dollar value of specific features (pool, furnishing, gated society) after controlling for size and location, using regression coefficients rather than raw averages.
4. **Outlier / luxury segment deep dive** — separate analysis of the high-area, high-price tail (Villas >5,000 sqft) versus the mainstream market.

## 6. Suggested Repository Structure

```
project/
├── data/
│   └── dataset_2.csv
├── notebooks/
│   └── 01_eda_and_cleaning.ipynb
├── README.md
├── ANALYSIS_FRAMEWORK.md
└── outputs/
    └── (charts, model results, summary reports)
```

## 7. Tools

Python (pandas, numpy), statistical testing (scipy/statsmodels), visualization (matplotlib/seaborn), optional modeling (scikit-learn).
