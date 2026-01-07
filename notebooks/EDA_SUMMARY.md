# Credit Risk Modeling — EDA & Baseline Summary

## 1. Objective
Build an interpretable baseline credit risk model to predict loan default, focusing on:
- Data quality
- Leakage prevention
- Feature behavior
- Model interpretability

This project prioritizes **clarity and correctness** over model complexity.

---

## 2. Data Overview
- Dataset: Small synthetic consumer credit sample
- Unit of observation: **Loan-level** (not customer-level)
- Target variable: `default` (binary: 1 = default, 0 = non-default)

Initial checks confirmed:
- Binary target with realistic class imbalance (~30% default)
- Presence of missing values, mixed types, and logical anomalies

---

## 3. Data Cleaning & Quality Fixes

Key issues addressed:
- **Exact duplicate rows** removed (no new information, bias frequency counts)
- Sentinel values (`months_on_file = -1`) replaced with missing
- Mixed-type columns (`income`, `credit_utilization`) coerced to numeric
- Percentage strings normalized to proportions
- Explicit missingness indicator created for income (`income_missing`)

After cleaning:
- All predictors are numeric or boolean
- Missingness is explicit and controlled
- No target leakage remains

---

## 4. Feature Intuition & Behavioral Analysis

Observed behaviors:

- **Age**: Non-monotonic relationship with default risk  
  → Binned into interpretable age groups

- **Income**: Heavy-tailed distribution  
  → Log-transformed to stabilize scale

- **Months on File**: Time-exposure effect (longer duration → more opportunity to default)  
  → Bucketed into exposure bands

- **Number of Past Dues**: Strong monotonic risk signal  
  → Higher past dues → higher default probability

- **Credit Utilization**: Clear monotonic risk relationship  
  → Higher utilization → higher default risk

These transformations align features with how linear models reason about risk.

---

## 5. Baseline Model — Logistic Regression

A regularized logistic regression was chosen as the primary baseline because:
- Coefficients are interpretable
- Monotonic signals are preserved
- Model is stable under small data perturbations

Results:
- ROC AUC ≈ 1.0 on small sample (expected due to dataset size)
- Coefficients aligned with domain intuition after feature engineering

This model serves as the **reference benchmark**.

---

## 6. Contrast Model — Decision Tree

A shallow decision tree (max_depth=3) was trained for contrast.

Findings:
- The tree placed **100% feature importance on `num_past_dues`**
- Other features were ignored once purity was achieved
- Test ROC AUC ≈ 0.7

Interpretation:
- Trees greedily exploit dominant shortcuts
- Feature importance reflects training splits, not overall risk relevance
- This reinforces why tree models can be unstable and misleading in credit risk contexts

---

## 7. Key Takeaways

- Data quality and feature definition matter more than model choice
- Logistic regression provides stable, explainable baselines
- Tree models highlight dominant signals but risk over-reliance
- Perfect metrics on tiny datasets are not meaningful; behavior matters more

This project demonstrates a complete, realistic baseline credit risk workflow suitable for regulated environments.

---

## 8. Next Steps
- Freeze baseline model
- Add documentation (README)
- Optional: experiment with boosted trees for comparison (not replacement)
- Prepare model explanation for interview and portfolio review

