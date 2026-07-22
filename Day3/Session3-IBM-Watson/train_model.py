"""
Day 3 - Session 3  |  The same code as the notebook, as a plain script.

Use this if you prefer scripts to notebooks, or to run it in Cloud Shell.

HOW TO RUN
    pip install pandas scikit-learn joblib
    python train_model.py
"""

import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split


def main():
    # ---------------------------------------------------------------
    # 1. Load the data
    # ---------------------------------------------------------------
    df = pd.read_csv("soldiers_fitness.csv")
    print(f"Loaded {len(df)} rows\n")
    print(df.head(), "\n")

    # ---------------------------------------------------------------
    # 2. Split into questions (X) and answer (y)
    # ---------------------------------------------------------------
    X = df[["age", "pushups", "run_5km_min"]]
    y = df["level"]

    # ---------------------------------------------------------------
    # 3. Hold back 30% so we can test honestly
    # ---------------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    print(f"Training on {len(X_train)} rows, testing on {len(X_test)}\n")

    # ---------------------------------------------------------------
    # 4. TRAINING - the model learns the pattern
    # ---------------------------------------------------------------
    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)
    print("Training finished.\n")

    # ---------------------------------------------------------------
    # 5. How good is it on data it has never seen?
    # ---------------------------------------------------------------
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy on unseen data: {accuracy:.0%}")
    print("(A perfect score on 20 rows means the problem was easy,")
    print(" not that the model is brilliant.)\n")

    # ---------------------------------------------------------------
    # 6. INFERENCE - ask it about somebody new
    # ---------------------------------------------------------------
    new_person = pd.DataFrame({
        "age": [25],
        "pushups": [48],
        "run_5km_min": [23],
    })
    print("A 25-year-old doing 48 pushups, 5km in 23 minutes")
    print("is predicted to be:", model.predict(new_person)[0], "\n")

    # ---------------------------------------------------------------
    # 7. See the rules it worked out by itself
    # ---------------------------------------------------------------
    print("The rules the model learned:")
    print(export_text(model, feature_names=list(X.columns)))

    # ---------------------------------------------------------------
    # 8. Save it
    # ---------------------------------------------------------------
    joblib.dump(model, "fitness_model.pkl")
    print("Saved as fitness_model.pkl")
    print("\nTo register it in Azure ML, use the notebook version.")


if __name__ == "__main__":
    main()
