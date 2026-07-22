# Day 3 · Session 3 — Azure Machine Learning: Train Your First Model

**13:45 – 15:15 (1.5 hours)**

You will create a machine learning workspace, rent a computer by the minute, train a
model on the data you uploaded this morning, and save it properly.

> **Read this first:** this session is the only one today that costs real money.
> A compute instance bills every minute it runs. We stop it together at the end.

---

## 1. Words you need

| Word | What it means |
|---|---|
| **ML workspace** | The home for all your machine learning work: data, notebooks, models, experiments |
| **Compute instance** | A computer in Azure that you rent by the minute. **This is the part that costs money** |
| **Notebook** | Same idea as Google Colab on Day 1 — cells of code you run one at a time |
| **Training** | Showing the computer examples so it learns the pattern |
| **Inference** | Using the trained model to answer a new question |
| **Registered model** | A trained model saved in the workspace with a name and a version |
| **Idle shutdown** | A setting that switches the compute off by itself. Always turn it on |

---

## 2. Lab 3A — Create your ML workspace (20 min)

1. In the portal search bar type **`Azure Machine Learning`**, press Enter
2. Click **+ Create** → **New workspace**
3. Fill in:

   | Field | What to put |
   |---|---|
   | **Resource group** | **YOUR group** — `rg-student-yourname` |
   | **Workspace name** | `ml-abebe` |
   | **Region** | The same one you used this morning |
   | Storage account, Key vault, Application insights | Leave the defaults — Azure creates them for you |

4. Click **Review + create** → **Create**
5. Wait 2–3 minutes for the deployment to finish
6. Click **Go to resource** → **Launch studio**

A new tab opens at **ml.azure.com**. From here on you work there, not in the main portal.

---

## 3. Lab 3B — Start a compute instance (15 min)

1. In ML Studio, click **Compute** in the left menu
2. Make sure you are on the **Compute instances** tab, click **+ New**
3. Fill in:

   | Field | What to put |
   |---|---|
   | **Compute name** | `ci-abebe` |
   | **Virtual machine type** | **CPU** |
   | **Virtual machine size** | The smallest available, e.g. `Standard_DS11_v2` |

4. **Before you click Create**, open **Scheduling** (or *Idle shutdown*) and
   **enable shut down after 30 minutes of inactivity**
5. Click **Create**
6. It takes 3–5 minutes. The dot turns **green** when it is running.

> ### This is the expensive one
> A running compute instance bills every minute — including overnight, including when
> your laptop is closed. Idle shutdown is your safety net. **Set it now, not later.**

---

## 4. Lab 3C — Train a model (35 min)

1. In ML Studio click **Notebooks** in the left menu
2. Click the **upload** icon and upload **both** files from this folder:
   - `train_model.ipynb`
   - `soldiers_fitness.csv`
3. Click `train_model.ipynb` to open it
4. Top-right, make sure the **Compute** box shows `ci-abebe` and the kernel is
   **Python 3 - SDK v2**
5. Run each cell with **Shift + Enter**, from top to bottom

### The two lines that matter

```python
model.fit(X_train, y_train)      # TRAINING - the model learns
model.predict(new_person)        # INFERENCE - the model answers
```

Everything else is loading data, checking it, and measuring the result.

### About that 100% accuracy

You will probably get a perfect score. **Do not be impressed.** With 20 rows and an
obvious pattern, this is easy. Real datasets have thousands of rows, noise and
contradictions, and 70–85% is often a good result.

Always ask *why* a number is good — not just whether it is.

---

## 5. Lab 3D — Register the model (10 min)

A model inside a notebook disappears when the notebook closes. Registering gives it a
name, a version, and a home in the workspace.

The last cells of the notebook do this:

```python
joblib.dump(model, "fitness_model.pkl")          # save to a file

ml_client.models.create_or_update(Model(          # register it
    path="fitness_model.pkl",
    name="fitness-model",
    type=AssetTypes.CUSTOM_MODEL))
```

**Check it worked:** in ML Studio, click **Models** in the left menu. Your model is
listed with version 1.

---

## 6. STOP YOUR COMPUTE INSTANCE

**Do this before you leave the room. Every time.**

1. In ML Studio, click **Compute**
2. Tick the box next to `ci-abebe`
3. Click **Stop**
4. Wait until the status says **Stopped** — not *Stopping*

A stopped instance costs nothing. Your notebooks and files stay exactly where they are.

You can also do it from Cloud Shell:

```bash
az ml compute stop --name ci-abebe \
    --workspace-name ml-abebe \
    --resource-group rg-student-abebe
```

---

## 7. Files in this folder

| File | What it is |
|---|---|
| `README.md` | This guide |
| `train_model.ipynb` | The notebook to upload and run in ML Studio |
| `soldiers_fitness.csv` | The dataset (upload it next to the notebook) |
| `train_model.py` | The same code as a plain script, if you prefer |

---

## 8. Checklist

- [ ] I created an Azure ML workspace in my own resource group
- [ ] I started a compute instance **with idle shutdown enabled**
- [ ] I uploaded the notebook and the CSV
- [ ] I ran every cell and got an accuracy score
- [ ] I made a prediction for a new person
- [ ] My model is listed under **Models** in ML Studio
- [ ] **My compute instance says Stopped**

---

## 9. If something goes wrong

**The workspace takes forever to create**
2–3 minutes is normal. It is building four resources at once.

**"Compute instance name already exists"**
Names must be unique across the whole workspace. Add your initials or a number.

**No VM sizes are available in my region**
Some regions run out of quota. Ask the trainer — they may need to pick a different
region or request more quota.

**The notebook says "no compute selected"**
Top-right of the notebook, choose your compute instance from the dropdown. It must be
green/Running first.

**`ModuleNotFoundError: sklearn`**
Change the kernel (top-right) to **Python 3.10 - SDK v2**, which has it preinstalled.

**`FileNotFoundError: soldiers_fitness.csv`**
The CSV must be uploaded to the same folder as the notebook, not just to your computer.

**Cell 11 (registering) fails**
This only works when the notebook runs on a compute instance inside the workspace. If it
fails, do not worry — the important learning was training and predicting.

**I forgot to stop my compute yesterday**
Tell the trainer, stop it now, and set idle shutdown. It happens; the fix is the habit.

---

**Next:** [Session 4 — Azure AI Services & Cleanup](../Session4/README.md)
