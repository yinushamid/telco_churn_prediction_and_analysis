# Telco Customer Churn Prediction & Analysis


## Overview

In today's competitive telecom industry, **understanding customer churn** is essential for long-term profitability. This project goes beyond churn prediction — it explains **who is churning, why they are churning, and how much revenue is at risk**, all visualized through a **Power BI dashboard** powered by Python modeling.

---

##  Table of Contents

- [Business Problem](#business-problem)
- [Dashboard-Driven Insights](#dashboard-driven-insights)
- [Top Churn Segments](#top-churn-segments)
- [Feature Importance Highlights](#feature-importance-highlights)
- [ML Model (Python)](#ml-model-python)
- [Files Included](#files-included)

---

##  Business Problem

> “How can we predict customer churn and uncover the patterns behind customer attrition in order to reduce revenue loss?”

Churn costs telecom providers thousands in lost revenue monthly. This analysis enables business teams to:
- Identify customers likely to leave
- Understand churn patterns using explainable features
- Prioritize interventions with financial impact in mind

---

## 📊 Dashboard-Driven Insights

The Power BI dashboard tells a **compelling story** in a single view. Here's what it reveals:

###  Churn at a Glance
- **Total Customers**: `7,032`
- **Churned Customers**: `1,869` (~**26.58% churn rate**)
- **Revenue Lost to Churn**: `$139K+`
- **Total Revenue**: `$455K+`

Churn is not just a number — it's costing the business over **30% of potential earnings**.

---

##  Top Churn Segments

The dashboard drills down into the **who** and **why** behind churn:

###  By Contract Type
- **Month-to-month customers** churn the most: `~1.7K` churned
- Very few churners had one-year or two-year contracts → **long-term contracts reduce churn**

###  By Payment Method
- **Electronic Check users** are most at risk (`1,071` churned) — possibly due to failed payments or low trust
- **Auto-pay methods** like credit card or bank transfer have much lower churn

###  By Monthly Charges
- Churn is high among customers paying **$70–$99/month**
- Those paying less than $50 churn less frequently

###  By Tenure
- Customers with **0–6 months tenure** had the highest churn (`784`)
- Suggests that **new users are not retained**, possibly due to onboarding issues or unmet expectations

---

##  Feature Importance Highlights

The model trained in Python helped rank the most influential factors that impact churn.

| Rank | Feature           | Importance |
|------|-------------------|------------|
| 1️⃣   | Total Charges      | 0.18       |
| 2️⃣   | Monthly Charges    | 0.18       |
| 3️⃣   | Tenure             | 0.15       |
| 4️⃣   | Contract Type      | 0.08       |
| 5️⃣   | Payment Method     | 0.05       |

> These features were used to **score each customer** and assign a probability of churn, helping business teams take proactive action.

---

## 🤖 ML Model (Python)

While the focus is on dashboard insights, the **backend engine** is a Random Forest model trained with Python. Here's a quick summary:

- Encoded categorical features (`Contract`, `PaymentMethod`, `Churn`)
- Scaled numeric features for better learning
- Trained a `RandomForestClassifier` with 100 estimators
- Achieved **~80% accuracy**
- Exported:
  - Predicted churn values
  - Churn probabilities per customer
  - Feature importance rankings

This enriched data was visualized in Power BI for business decision-making.

---

##  Files Included

| File | Description |
|------|-------------|
| `telco_churn_predictions.csv` | Dataset with churn predictions and probabilities |
| `feature_importance.csv` | Ranked feature importances from the ML model |
| `telco_churn_model.py` | Python script for model training and output |
| `telco_churn_dashboard.pbix` | Power BI file for visual insights |
| `README.md` | Project documentation |

---

##  Conclusion

The Power BI dashboard gives executives and analysts a **clear, actionable lens** into churn behavior. With insights powered by machine learning, the business can:
- Design targeted retention campaigns
- Improve onboarding for new customers
- Encourage auto-pay options to reduce risk

**Data isn't just for prediction — it tells a story.** This project transforms raw churn data into visual, strategic insight.

---

##  Author

**Yinus Hamid**  
 Data Analyst | Power BI | Python 
[LinkedIn](https://www.linkedin.com) • [GitHub](https://github.com)

---

