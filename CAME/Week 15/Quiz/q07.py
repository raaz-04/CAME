import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Load dataset
df = pd.read_csv("customer_churn.csv")

# Target
y = df["churn"]

# Features
X = df.drop(columns=["churn"])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    stratify=y,
    random_state=42
)

# a) Share of training set that churned
train_churn_share = y_train.mean()

print(round(train_churn_share,4))

# Standardization
scaler = StandardScaler()

X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Logistic Regression
model = LogisticRegression(max_iter=1000)

model.fit(X_train_s, y_train)

# Predictions
y_pred = model.predict(X_test_s)

# b) Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(round(accuracy,4))

# c) Precision, Recall and F1
precision = precision_score(y_test, y_pred, pos_label=1)
recall = recall_score(y_test, y_pred, pos_label=1)
f1 = f1_score(y_test, y_pred, pos_label=1)

print(round(precision,4),round(recall,4),round(f1,4))

# d) Confusion matrix
cm = confusion_matrix(y_test, y_pred)

TN, FP, FN, TP = cm.ravel()

print(round(TN,4),round(FP,4),round(FN,4),round(TP,4))