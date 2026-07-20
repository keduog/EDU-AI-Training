# train_local.py — my first locally trained model
#
# Trains a tiny decision tree on the soldiers_fitness dataset committed on Day 1.
# Everything here runs on YOUR laptop — no cloud account needed for this file.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Replace <your-username> with your own GitHub username.
url = (
    "https://raw.githubusercontent.com/<your-username>/"
    "EDU-AI-Training/main/data/soldiers_fitness.csv"
)
df = pd.read_csv(url)

X = df[["age", "pushups_per_min", "run_5km_minutes"]]
y = df["fitness_level"]

model = DecisionTreeClassifier().fit(X, y)

print(
    "Prediction for a 24-year-old, 48 pushups, 23-min 5km:",
    model.predict([[24, 48, 23]])[0],
)
