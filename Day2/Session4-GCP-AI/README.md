# Session 4 — Google Cloud AI Platform (Vertex AI)

**Day 2 · 15:30 – 16:30**

With one hour, we prove one big idea: **cloud skills transfer.** Everything you did on AWS
this morning has a Google Cloud equivalent — only the names change.

---

## 1. Key definitions

| Term | Beginner-friendly definition |
|---|---|
| **GCP** | Google Cloud Platform — Google's cloud, the same one that runs Colab and trained PaLM (the TPU pods from Day 1's slide). |
| **Project** | GCP's container for everything you create — like an AWS account-plus-region in one concept. All resources live inside a project. |
| **Cloud Storage** | GCP's file storage — the S3 of Google Cloud. Also organized in buckets. |
| **Vertex AI** | Google's managed ML platform — the SageMaker of GCP: notebooks (Workbench), training, endpoints, and AutoML in one place. |
| **AutoML** | Training where the platform picks the algorithm and tuning for you — upload data, click train. Powerful, but slower and less transparent; good for prototypes. |
| **Model Garden** | Vertex AI's catalog of ready-made Google and open models — the Hugging Face idea inside GCP. |
| **Pretrained APIs** | Google AI services that need no training at all: Translation, Vision, Natural Language, Speech. One API call and you get the answer. |

---

## 2. Hands-On Lab G — A first GCP AI task (35 min)

1. Open <https://console.cloud.google.com> and sign in with a Google account (the same one
   used for Colab yesterday).
2. Top bar → project selector → **New Project**. Name: `ai-lab-day2`. Create, then make
   sure it is selected.
3. Search bar → **Cloud Translation API** → **Enable**. (Enabling an API is GCP's way of
   switching a service on for your project.)
4. Open the Translation service page and use the built-in demo: translate a sentence
   between Amharic and English, both directions — discuss the quality with the class.
5. Search **Vertex AI** → open the **Dashboard** and **Model Garden**. Guided tour only:
   point out **Workbench** (their Studio), **Training** (their training jobs),
   **Endpoints** (their endpoints) — you should recognize every concept from this morning.

**What you should see:** a working translation in the console demo, and a Vertex AI
dashboard whose left-hand menu reads like a translated version of SageMaker's.

### Optional: the same task in code

[`translate_demo.py`](./translate_demo.py) in this folder calls the same Translation API
from Python instead of the console widget, for anyone who wants to see the code path. It
needs `pip install google-cloud-translate` and `gcloud auth application-default login`
first — not required to complete the lab.

---

## 3. AWS ↔ GCP: the translation table

| AWS | GCP |
|---|---|
| Amazon S3 | Cloud Storage |
| SageMaker Studio | Vertex AI Workbench |
| SageMaker training job | Vertex AI custom training / AutoML |
| SageMaker endpoint | Vertex AI endpoint |
| IAM role | Service account |
| CloudWatch | Cloud Monitoring |

> **Concept check:** tomorrow (Azure ML and IBM Watson) makes it four clouds — and by then
> you should be able to predict this table yourself. The concepts are the skill; the
> product names are vocabulary.

---

## If something goes wrong

| Problem | Fix |
|---|---|
| "Billing account required" | Free tier still needs a linked billing account — use a personal card and watch the quota |
| API not enabled error | **APIs & Services → Library** → search "Translation" → **Enable**, then retry |
| Project selector shows nothing | Wait a few seconds after creating — GCP project provisioning is not instant |
| Translation gives an odd Amharic result | Expected — use it as a discussion point on machine translation quality |
| Console feels totally different from AWS | That's the point of this session — same concepts, different names |

---

## Checklist

- [ ] GCP project `ai-lab-day2` created and selected
- [ ] Cloud Translation API enabled and invoked (console demo, or `translate_demo.py`)
- [ ] Vertex AI dashboard and Model Garden toured
- [ ] I can name the GCP twin of S3, SageMaker Studio, and an endpoint

---

## End of Day 2

- [ ] PyCharm project + venv + AI stack installed (Session 1)
- [ ] `train_local.py` trained a model locally → pushed to GitHub (Session 1)
- [ ] S3 bucket contains `data/soldiers_fitness.csv` (Session 2)
- [ ] SageMaker training job **Completed** → `model.tar.gz` in S3 (Session 2)
- [ ] Endpoint deployed, invoked — and **DELETED** (Session 3)
- [ ] GCP project exists, one pretrained service invoked (Session 4)

**Three ideas to remember:**
1. The pattern: storage → training job → artifact → endpoint. Every cloud, same shape.
2. Training jobs stop billing themselves; endpoints bill until **you** stop them.
3. You didn't learn "AWS" today — you learned cloud ML, twice.

**Tomorrow — Day 3:** Microsoft Azure Machine Learning and IBM Watson AI Services complete
the cloud tour: four clouds touched by hand, compared from experience, not marketing.
