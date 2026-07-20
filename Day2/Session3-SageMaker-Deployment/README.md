# Session 3 — Amazon SageMaker Part 2: Deployment & MLOps

**Day 2 · 13:15 – 15:15**

Session 2 produced a trained model sitting in S3. In this session you turn that file into a
**live prediction service** — then practice the single most important cloud habit: deleting
what you started.

---

## 1. Key definitions

| Term | Beginner-friendly definition |
|---|---|
| **Deployment** | Making a trained model available so applications can use it — the step that turns a file into a service. |
| **Endpoint** | A URL backed by an always-on rented machine hosting your model. Applications send data to it and receive predictions. Billed every hour it exists. |
| **Real-time inference** | One request, one instant answer — what an endpoint provides. For a drone camera or a chatbot. |
| **Batch transform** | Predictions for a whole file of rows at once, with no permanent server — cheaper when answers are not needed instantly. |
| **Serverless inference** | An endpoint that scales to zero when idle — you pay only per request. Good for rarely-used models. |
| **Invoke** | To call an endpoint with input data and receive a prediction. |
| **MLOps** | Machine Learning Operations — the engineering discipline around models in production: versioning, automated pipelines, monitoring, and retraining. |
| **Model registry** | A catalog of model versions, so you always know which version is deployed and can roll back. |
| **Monitoring / drift** | Watching a deployed model's inputs and accuracy over time. "Drift" means the real world changed and the model is going stale — time to retrain. |
| **CloudWatch** | AWS's monitoring service — where endpoint logs and metrics (invocations, latency, errors) appear. |

---

## 2. From artifact to live service

```
  Model artifact (S3)  ──deploy──▶  Endpoint (always-on)  ──invoke──▶  Client apps
                                          │
                                    ⚠ COST RULE:
                              bills hourly until deleted
```

---

## 3. Hands-On Lab E — Deploy and invoke an endpoint (60 min)

Use [`day2_sagemaker_deploy.ipynb`](./day2_sagemaker_deploy.ipynb) in this folder.

1. **If you still have Session 2's notebook open in the same kernel:** skip straight to
   Cell 4 — the `est` object already holds your trained model.
2. **Starting a new kernel or a new day?** Run Cell 0 first: copy your training job's exact
   name from **SageMaker → Training → Training jobs** and paste it in, then run
   `SKLearn.attach(...)` to reconnect.
3. Run Cell 4 to deploy, then Cell 5 to invoke.

**What you should see:** Cell 4 prints dashes for ~5 minutes while the endpoint machine
starts, then `----!`. Cell 5 returns `['high', 'low']` — your model, answering over the
internet. In the console: **SageMaker → Endpoints** shows status `InService`.

Open **CloudWatch** from the endpoint's Monitoring tab to see the invocation count and
latency graphs — this is MLOps monitoring in its simplest form.

**Discussion (10 min):** walk the MLOps loop on the whiteboard — data → train → deploy →
monitor → drift detected → retrain → redeploy. Day 4 covers the train/fine-tune stages in
depth.

---

## 4. Hands-On Lab F — DELETE the endpoint (10 min, mandatory)

Run Cell 6:

```python
predictor.delete_endpoint()
```

**Verify in the console:** SageMaker → Endpoints must be **EMPTY**. Your trainer checks
every screen before the break.

> **Cost rule:** a forgotten `ml.m5.large` endpoint costs roughly $80–100 per month.
> Training jobs shut themselves down; endpoints never do. The habit: deploy → test →
> **DELETE**. No exceptions, today or ever.

Save the notebook to GitHub, message: `Add SageMaker training and deployment notebook`.

---

## If something goes wrong

| Problem | Fix |
|---|---|
| Deploy stuck on "Creating" | Normal for 3–5 minutes — the hosting instance is provisioning |
| `predict()` throws a shape error | Column order/count must match training exactly — check the DataFrame columns |
| Endpoint shows `Failed` | Check **CloudWatch Logs** under the endpoint — usually a missing dependency in the inference code |
| Can't find `delete_endpoint()` | Use `predictor.delete_endpoint()`, or delete manually: **SageMaker → Endpoints → Delete** |
| Not sure it's really deleted | Refresh the Endpoints console list — it must show **zero rows**, not just "Deleting" |
| Lost the `est`/`predictor` object (new kernel) | Run Cell 0 with your training job's exact name to reattach |

---

## Checklist

- [ ] Endpoint deployed and status showed `InService`
- [ ] `predictor.predict(...)` returned real predictions
- [ ] CloudWatch invocation graph viewed at least once
- [ ] Endpoint list confirmed **EMPTY** before the break
- [ ] Notebook committed and pushed to GitHub

**Next:** [Session 4 — Google Cloud AI Platform](../Session4-GCP-AI/README.md) proves this
whole pattern isn't AWS-specific — it's cloud ML.
