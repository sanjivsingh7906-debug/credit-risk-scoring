# Credit Risk Scoring — Baseline Model

## Overview

This project builds a **baseline credit risk model** to predict loan default.
The emphasis is on **EDA discipline, data quality, leakage prevention, and interpretability**, not complex modeling.

The workflow follows a practical credit-risk setup:
EDA → cleaning → feature engineering → baseline model → comparison.

---

## Problem Statement

Given historical loan-level data, predict whether a loan will **default (1)** or **not default (0)**.

Constraints:
- Small dataset
- Explainability required
- Avoid target leakage
- Preference for stable models

---

## Project Structure
credit-risk-scoring/
│
├── data/
│   └── sample_credit_data.csv
│
├── notebooks/
│   ├── EDA.ipynb
│   └── EDA_SUMMARY.md
│
├── src/
│   └── data_loader.py
│
├── requirements.txt
├── README.md
└── LICENSE

---

## Data

- Unit: Loan-level records
- Target: `default`
- Features include:
  - age
  - income
  - months_on_file
  - num_past_dues
  - credit_utilization

The dataset contains missing values, mixed types, duplicates, and anomalies,
which are handled during EDA and cleaning.

---

## Methodology

### 1. Exploratory Data Analysis
- Target distribution checks
- Leakage detection
- Missingness analysis
- Feature–target behavior review

Details are documented in `notebooks/EDA_SUMMARY.md`.

---

### 2. Data Cleaning
- Removed duplicates
- Fixed data types
- Normalized percentage fields
- Handled missing values
- Added missingness indicators

---

### 3. Feature Engineering
- Binning for non-linear effects
- Log transform for skewed variables
- Bucketing exposure-related features
- Explicit modeling of missingness

---

### 4. Baseline Model
- Logistic Regression (L2 regularized)
- Train/test split with stratification
- Scaling and imputation

Chosen for stability and interpretability.

---

### 5. Comparison Model
- Shallow Decision Tree
- Used to contrast behavior with logistic regression

---

## Key Observations

- Data quality has strong impact on model behavior
- Logistic regression provides stable and interpretable results
- Tree models tend to over-focus on dominant variables

---

## Limitations

- Small dataset
- Metrics are illustrative
- No temporal validation

---



