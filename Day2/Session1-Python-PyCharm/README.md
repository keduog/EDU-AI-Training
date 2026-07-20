# Session 1 — Python Development Environment & AI Dev Stack

**Day 2 · 09:00 – 10:00**

Yesterday every tool was free and ran in the browser. Today we start renting professional
cloud power — but professionals always write and test their code **locally first**. In this
session you install Python and PyCharm, and train your first model entirely on your own
laptop.

---

## 1. Key definitions

| Term | Beginner-friendly definition |
|---|---|
| **Python** | The programming language of AI. Nearly every tool this week — Colab, SageMaker, Vertex AI, even the Raspberry Pi on Day 5 — is driven with Python. |
| **Interpreter** | The program that reads your Python code and executes it line by line. |
| **Package / library** | Ready-made code written by others that you install and reuse — NumPy for math, pandas for tables, scikit-learn for classic ML. |
| **pip** | Python's package installer. `pip install pandas` downloads and installs the pandas library. |
| **Virtual environment (venv)** | A private folder of packages for one project, so Project A's library versions never break Project B. Professional Python always uses one. |
| **IDE** | Integrated Development Environment — an editor with a debugger, terminal, and project tools built in. |
| **PyCharm** | The most popular Python IDE (free Community Edition). Yesterday we used VS Code; PyCharm is the Python-specialist alternative — knowing both lets you choose. |
| **requirements.txt** | A text file listing a project's packages, so anyone can recreate the environment with one command. |
| **scikit-learn** | The classic machine-learning library: ready-made algorithms (decision trees, logistic regression) that train in seconds on small data. |

---

## 2. Why a local environment when the cloud exists?

Yesterday's PaLM slide showed why *big* training needs the cloud. But professionals still
write and test everything **locally first**: it's free, instant, and works offline.

**The rule of thumb for the whole day: write locally, scale in the cloud.**

---

## 3. Hands-On Lab A — Install Python + PyCharm and create a project (25 min)

1. Install Python from <https://python.org/downloads> — on Windows, tick **"Add python.exe
   to PATH"** during install.
2. Install **PyCharm Community Edition** (free) from <https://jetbrains.com/pycharm> —
   accept the defaults.
3. Open PyCharm → **New Project**. Name it `day2-cloud-ai`, and keep **"Create a
   virtualenv"** selected — PyCharm builds the virtual environment for you.
4. Open the built-in **Terminal** (bottom bar) and run:

   ```bash
   pip install numpy pandas scikit-learn matplotlib
   ```

   Or, using the `requirements.txt` in this folder:

   ```bash
   pip install -r requirements.txt
   ```

**What you should see:** the Terminal prints `Successfully installed …`. In the project
tree, a `.venv` folder now exists — that is your virtual environment. The Python
interpreter shown in the bottom-right corner ends with `(day2-cloud-ai)`.

---

## 4. Hands-On Lab B — Train your first model locally (25 min)

We reuse the `soldiers_fitness.csv` dataset committed to GitHub on Day 1 — continuity is
the point: same data, new tool.

1. In PyCharm, create a new file `train_local.py` and type (or Copilot-complete) the script
   in this folder — see [`train_local.py`](./train_local.py).
2. **Before running:** replace `<your-username>` in the script with your own GitHub
   username.
3. Run it with the green **▶** button. Training finishes in under a second — the dataset is
   tiny and the model is simple.

**What you should see:** the console prints something like:

```
Prediction for a 24-year-old, 48 pushups, 23-min 5km: high
```

4. Push the evidence: use PyCharm's Git menu (**VCS → Share Project on GitHub**, or commit
   inside your cloned repo) with the message `Add local training script`.

> **Concept check:** this model trained in milliseconds on your CPU because the data is 5
> rows. Scale the data to 5 million rows and the same code needs the cloud — which is
> exactly where Session 2 goes next.

---

## If something goes wrong

| Problem | Fix |
|---|---|
| `'python' is not recognized` | PATH wasn't set during install — reinstall and tick "Add to PATH" |
| `pip install` hangs or fails | Check your network connection; try again, or add `--user` |
| Wrong interpreter in PyCharm | **Settings → Project → Python Interpreter** → select the `.venv` folder |
| Import error when running the script | The package didn't install into this project's venv — reinstall from PyCharm's own Terminal |
| `git push` rejected | Run `git pull --rebase` first, resolve conflicts, then push again |

---

## Checklist

- [ ] Python and PyCharm Community Edition installed
- [ ] New project `day2-cloud-ai` created with its own virtual environment
- [ ] `numpy`, `pandas`, `scikit-learn`, `matplotlib` installed inside that venv
- [ ] `train_local.py` edited with my GitHub username and run successfully
- [ ] The script printed a fitness-level prediction
- [ ] The script is committed and pushed to my GitHub repository

**Next:** [Session 2 — Amazon SageMaker Part 1](../Session2-SageMaker-Training/README.md)
takes this exact pattern and moves it to the cloud.
