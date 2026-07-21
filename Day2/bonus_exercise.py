# bonus_exercise.py — Bonus Exercise: Predicting Diabetes Risk, Comparing Two Models
#
# Scenario: military medical staff collect basic vitals during routine screening
# (glucose, blood pressure, BMI, age, ...) and want a quick way to flag personnel
# at higher risk of diabetes for a follow-up check. This script trains TWO models
# on a real, published medical dataset and compares them on data neither model has
# seen during training.
#
# Dataset: Pima Indians Diabetes Database (768 patients), originally from the
# National Institute of Diabetes and Digestive and Kidney Diseases. Free, public,
# no signup or API key required. Mirror used below is the same one referenced in
# hundreds of published ML tutorials (jbrownlee/Datasets on GitHub).

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# ---------------------------------------------------------------------------
# 1. Load the data
# ---------------------------------------------------------------------------
# Unlike train_local.py, this file was NOT authored by you — it's reference data
# supplied with the course. So we fetch it from the course's own upstream repo,
# not your personal fork. That way it works immediately, with no fork-syncing
# step, even if you forked before this file was added.
URL = "https://raw.githubusercontent.com/keduog/EDU-AI-Training/main/data/pima_indians_diabetes.csv"
df = pd.read_csv(URL)

print(f"Loaded {len(df)} patient records.")
print(df.head(), "\n")

# ---------------------------------------------------------------------------
# 2. Split into training and test sets
# ---------------------------------------------------------------------------
# Lab B trained and predicted on the SAME 5 rows — fine for a first taste of
# scikit-learn, but it can't tell us how the model performs on NEW data. Here we
# hold back 20% of the patients and never let the models see them during training.
X = df.drop(columns=["outcome"])
y = df["outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Training on {len(X_train)} patients, testing on {len(X_test)} unseen patients.\n")

# ---------------------------------------------------------------------------
# 3. Train two different models on the same training data
# ---------------------------------------------------------------------------
tree_model = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
logreg_model = LogisticRegression(max_iter=1000).fit(X_train, y_train)

# ---------------------------------------------------------------------------
# 4. Compare them on the held-out test set
# ---------------------------------------------------------------------------
tree_acc = accuracy_score(y_test, tree_model.predict(X_test))
logreg_acc = accuracy_score(y_test, logreg_model.predict(X_test))

print("=== Results on unseen test patients ===")
print(f"Decision Tree accuracy       : {tree_acc:.2%}")
print(f"Logistic Regression accuracy : {logreg_acc:.2%}")

better = "Decision Tree" if tree_acc > logreg_acc else "Logistic Regression"
print(f"\nBetter model on this test split: {better}")

# ---------------------------------------------------------------------------
# 5. Visualize why the models can (or can't) separate the two outcomes
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt

colors = df["outcome"].map({0: "tab:blue", 1: "tab:red"})
plt.scatter(df["glucose"], df["bmi"], c=colors, alpha=0.5)
plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.title("Diabetes outcome by glucose and BMI (red = diabetic)")
plt.savefig("glucose_bmi_scatter.png")
print("\nSaved plot to glucose_bmi_scatter.png")
