# Bonus Exercise — Predicting Diabetes Risk: Comparing Two Models

**Optional stretch task for Session 1.** Finished Lab A and Lab B early? Do this next.

---

## Scenario

During routine medical screening, health staff collect basic vitals from personnel —
blood glucose, blood pressure, BMI, age, and a few others. They want a quick way to flag
people at higher risk of diabetes for a follow-up check, using only numbers already
collected on-site — no lab wait, no new equipment.

**You've been asked to build and compare two candidate models on a real, published
medical dataset, and recommend which one to use.**

## The question

Which of two models — a **Decision Tree** (the same algorithm as Lab B) or **Logistic
Regression** — makes better predictions on patients the model has **never seen** during
training? And why might a more complex model sometimes do *worse*, not better?

---

## The dataset

The **Pima Indians Diabetes Database** — 768 real patient records, originally from the
National Institute of Diabetes and Digestive and Kidney Diseases. It's free, public, and
needs no signup or API key.

A copy lives in this repo at [`data/pima_indians_diabetes.csv`](../../../data/pima_indians_diabetes.csv)
(with a header row added for clarity). The script fetches it from the **course's upstream
repository** (`keduog/EDU-AI-Training`), not from your personal fork — unlike
`train_local.py`, this file wasn't authored by you, so there's nothing to push from your
own copy, and no `<your-username>` to edit.

> **Instructor note:** this only works once `data/pima_indians_diabetes.csv` has been
> committed to the `main` branch of `keduog/EDU-AI-Training` (see the repo update package
> that included this exercise). Trainees need no fork-sync step either way — the file is
> read directly from the course repo, live, every time the script runs.

| Column | Meaning |
|---|---|
| `pregnancies` | Number of times pregnant |
| `glucose` | Plasma glucose concentration (2-hour oral glucose tolerance test) |
| `blood_pressure` | Diastolic blood pressure (mm Hg) |
| `skin_thickness` | Triceps skinfold thickness (mm) |
| `insulin` | 2-hour serum insulin |
| `bmi` | Body mass index |
| `diabetes_pedigree` | A score summarizing family history of diabetes |
| `age` | Age in years |
| `outcome` | **1** = diabetic, **0** = not diabetic (what we're predicting) |

Unlike the 5-row `soldiers_fitness.csv` from Lab B, this dataset has enough rows (768) to
genuinely hold some back for testing — which is the whole point of this exercise.

---

## What the script does

Open [`bonus_exercise.py`](./bonus_exercise.py) and run it (no setup beyond Lab A's
`pip install` — it only needs packages you already installed):

```bash
python bonus_exercise.py
```

1. **Loads the data directly from a URL** — no download step, same pattern as
   `train_local.py`.
2. **Splits it 80/20** into training patients and test patients the model never trains
   on — the piece Lab B skipped.
3. **Trains two models** on the exact same training data: `DecisionTreeClassifier` (same
   class as Lab B) and `LogisticRegression`.
4. **Scores both models** on the 20% of patients held back, using accuracy.
5. **Saves a scatter plot** (`glucose_bmi_scatter.png`) of glucose vs. BMI, colored by
   outcome, so you can see visually why this is a hard problem — the two groups overlap.

---

## What you should see

```
Loaded 768 patient records.
...
Training on 614 patients, testing on 154 unseen patients.

=== Results on unseen test patients ===
Decision Tree accuracy       : 72.73%
Logistic Regression accuracy : 71.43%

Better model on this test split: Decision Tree
```

Your exact percentages may differ slightly by scikit-learn version, but both models
should land somewhere in the high-60s to mid-70s — nowhere near 100%. **That's expected,
and it's the lesson:** real medical data is noisy, and no simple model separates these
patients perfectly.

---

## Reflection questions (discuss with your table or trainer)

1. Which model won on your run? Was it the same one every time you re-ran with a
   different `random_state`?
2. `DecisionTreeClassifier` has no depth limit set here — it can, in principle, memorize
   the training data perfectly. Look up **overfitting**: why doesn't perfect training
   accuracy guarantee good test accuracy?
3. Try changing `X = df.drop(columns=["outcome"])` to use only `["glucose", "bmi"]`
   instead of all 8 columns. Does accuracy go up, down, or stay about the same? Why might
   *fewer* features sometimes help?
4. Look at `glucose_bmi_scatter.png`. Where do the red and blue points overlap most? What
   does that overlap mean for how confident any model can be in that region?

---

## If something goes wrong

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` for sklearn/pandas/matplotlib | Run `pip install -r ../requirements.txt` from the Session 1 folder |
| `HTTPError: 404` when loading the URL | The dataset hasn't been pushed to the course repo yet — ask your trainer to confirm `data/pima_indians_diabetes.csv` exists on `keduog/EDU-AI-Training`'s `main` branch |
| Script can't reach the URL at all | Check your network connection |
| Accuracy numbers differ from the README | Normal — small variation across scikit-learn versions is expected; the *comparison*, not the exact number, is the point |
| No plot window appears | Expected — the script **saves** the plot to a file instead of opening a window; open `glucose_bmi_scatter.png` from your file explorer |

---

## Checklist

- [ ] Script runs without errors and prints both models' accuracy
- [ ] `glucose_bmi_scatter.png` was created and I looked at it
- [ ] I can explain in one sentence why a train/test split matters
- [ ] I tried at least one change (fewer features, or a different `random_state`) and
      observed what happened

**Back to:** [Session 1 — Python Development Environment](../README.md)

____________________________________________

Try the bonus stretch exercise:
[**Predicting Diabetes Risk — Comparing Two Models**](./bonus-model-comparison/README.md).
It uses a real, 768-patient public dataset to introduce train/test splitting and model
comparison — two ideas Lab B doesn't cover, and a preview of what Day 4 calls "evaluation."

**Next:** [Session 2 — Amazon SageMaker Part 1](../Session2-SageMaker-Training/README.md)
takes this exact pattern and moves it to the cloud.