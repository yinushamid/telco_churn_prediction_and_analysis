# Telco Customer Churn Prediction Project

# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load Dataset
raw_telco_data = pd.read_csv(r'c:\Users\Hp\Desktop\my_first_project\mydata project\WA_Fn-UseC_-Telco-Customer-Churn.csv')
telco_data = raw_telco_data.copy()

# Drop customerID as it's not useful for prediction
telco_data.drop('customerID', axis=1, inplace=True)

# Convert TotalCharges to numeric (some may be blank or space)
telco_data['TotalCharges'] = pd.to_numeric(telco_data['TotalCharges'], errors='coerce')

# Drop rows with missing values
telco_data.dropna(inplace=True)

# Encode target variable: Yes → 1, No → 0
telco_data['Churn'] = telco_data['Churn'].map({'Yes': 1, 'No': 0})

# Encode selected categorical features: Contract and PaymentMethod
le_contract = LabelEncoder()
telco_data['Contract'] = le_contract.fit_transform(telco_data['Contract'])
print("Contract classes mapping:", dict(zip(le_contract.classes_, le_contract.transform(le_contract.classes_))))

le_payment = LabelEncoder()
telco_data['PaymentMethod'] = le_payment.fit_transform(telco_data['PaymentMethod'])
print("PaymentMethod classes mapping:", dict(zip(le_payment.classes_, le_payment.transform(le_payment.classes_))))

# Separate Features and Target
X = telco_data.drop('Churn', axis=1)
y = telco_data['Churn']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Prediction on full data
y_pred_full = model.predict(X_scaled)
y_proba_full = model.predict_proba(X_scaled)[:, 1]  # Probability of churn (class = 1)

# Add predictions and probabilities to the original data
telco_data['PredictedChurn'] = y_pred_full
telco_data['ChurnProbability'] = y_proba_full

# Export prediction result
telco_data.to_csv(r"c:\Users\Hp\Desktop\my_first_project\mydata project\telco_churn_predictions.csv", index=False)

# Feature Importance (match to X.columns)
feature_names = X.columns
feat_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)

# Export feature importance
feat_importance_df.to_csv(r"c:\Users\Hp\Desktop\my_first_project\mydata project\feature_importance.csv", index=False)



