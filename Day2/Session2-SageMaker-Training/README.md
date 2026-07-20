# Session 2 — Amazon SageMaker Part 1: Cloud ML Basics

**Day 2 · 10:15 – 12:15**

In Session 1 you trained a model on your own laptop. In this session you do the same
training — but on a machine you rent from Amazon Web Services. The big idea: **your
notebook doesn't train — it launches.**

---

## 1. Key definitions

| Term | Beginner-friendly definition |
|---|---|
| **AWS** | Amazon Web Services — the largest cloud provider. Rents computing, storage, and AI services by the hour. |
| **AWS Console** | The website (console.aws.amazon.com) where you manage everything in your AWS account. |
| **Region** | A physical location of AWS data centers (e.g. `eu-west-1` in Ireland). You choose one and create everything inside it. |
| **IAM** | Identity and Access Management — AWS's system of users, roles, and permissions. A "role" is a badge that lets one AWS service act on your behalf. |
| **S3** | Simple Storage Service — AWS's file storage. Data for training always starts in S3. |
| **Bucket** | A top-level folder in S3 with a globally unique name. Files inside are called objects. |
| **Amazon SageMaker** | AWS's managed machine-learning platform: notebooks, training jobs, model hosting, and MLOps in one service. |
| **SageMaker Studio** | The web-based IDE of SageMaker — Jupyter notebooks running in AWS, similar to Colab but connected to your AWS account. |
| **Training job** | A SageMaker task that rents a machine, runs your training script on data from S3, saves the model back to S3, and shuts the machine down automatically. |
| **Instance type** | The size of machine you rent — e.g. `ml.m5.large` (CPU, cheap) or `ml.p3.2xlarge` (GPU, powerful, expensive). |
| **Estimator** | The SageMaker Python object where you declare: my script, my instance type, my data — then call `.fit()` to launch the training job. |
| **Free tier** | AWS's limited free allowance for new accounts. Our exercises are designed to stay small, but always clean up (Session 3). |

---

## 2. The cloud training pattern

One idea explains the whole session: **your notebook does not do the training** — it
launches a separate rented machine that does, then disappears.

```
   Your notebook                Rented machine (training job)
  (SageMaker Studio)                       │
        │  est.fit(...)                    │
        └──────────────────────────────────▶  starts, runs train.py,
                                               saves model.tar.gz to S3,
                                               shuts itself down
```

Data lives in **S3**, the training job runs on a **rented machine**, and a **model
artifact** comes out. This is the same pattern on every cloud — you will see it again on
GCP this afternoon, and on Azure tomorrow.

---

## 3. Guided tour: AWS Console (15 min)

1. Sign in at <https://console.aws.amazon.com> with the training account credentials
   provided by your trainer.
2. Top-right corner: select the course region (your trainer will announce it — everyone
   must use the same one).
3. Use the search bar to find and open **S3**, then **SageMaker** — pin both to the
   toolbar. These are the only two services we need today.

> If individual AWS accounts are not ready, pair up on a prepared shared account.

---

## 4. Hands-On Lab C — Create an S3 bucket and upload the dataset (20 min)

1. Open **S3 → Create bucket**. Name: `ai-lab-<your-username>` (bucket names are globally
   unique — your GitHub username makes it unique). Leave all defaults. **Create.**
2. Open the bucket → **Create folder** named `data`.
3. Download `soldiers_fitness.csv` from this repository's [`data/`](../../data/) folder
   (or from your own Day 1 fork), then in S3: **Upload → Add files** → select the CSV →
   **Upload**.

**What you should see:** inside your bucket, `data/soldiers_fitness.csv` with a size of a
few hundred bytes. Your data now lives in the cloud — the starting point of every cloud ML
project.

---

## 5. Hands-On Lab D — Train a model with a SageMaker training job (50 min)

1. Open **SageMaker Studio** (your trainer pre-creates the domain) and launch a JupyterLab
   space.
2. Open [`day2_sagemaker_training.ipynb`](./day2_sagemaker_training.ipynb) from this folder
   — or create a new notebook with the same name and copy the three cells in.
3. **Before running:** replace `<your-username>` in Cell 1 with your bucket suffix from Lab
   C.
4. Run the cells one at a time, top to bottom.

**What you should see:** several minutes of log lines — the machine is provisioned
(`Starting`), your script runs (`Training complete.`), and the job ends with `Billable
seconds: ~120`. In the console, **SageMaker → Training jobs** shows status `Completed`, and
your S3 bucket now contains a `model.tar.gz` artifact.

> **Concept check:** compare with `train_local.py` from Session 1 — the code is nearly
> identical, but that ran on YOUR laptop while this ran on a machine you rented for ~2
> minutes and never have to maintain. Note the honest trade-off: for 5 rows of data, the
> cloud was slower (machine startup) and cost money — the cloud wins only when data and
> models outgrow the laptop.

---

## If something goes wrong

| Problem | Fix |
|---|---|
| Bucket name already taken | S3 names are global — add more of your username or a random suffix |
| `AccessDenied` on upload or training | Check that the SageMaker execution role has S3 permissions |
| Training job stuck on "Starting" | Normal for ~3 minutes while the instance provisions — wait it out |
| Training job shows `Failed` | Open **CloudWatch Logs** for the job — the Python traceback is at the bottom |
| Can't find `model.tar.gz` | Check the exact S3 output path shown in the job's summary tab |

---

## Checklist

- [ ] S3 bucket `ai-lab-<your-username>` created, containing `data/soldiers_fitness.csv`
- [ ] `day2_sagemaker_training.ipynb` run top to bottom inside SageMaker Studio
- [ ] Training job shows status **Completed** in the SageMaker console
- [ ] `model.tar.gz` visible in my S3 bucket

**Next:** [Session 3 — SageMaker Part 2: Deployment & MLOps](../Session3-SageMaker-Deployment/README.md)
takes this saved model and turns it into a live prediction service.
