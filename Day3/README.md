# Day 3 · Session 4 — Azure AI Services & Cleaning Up

**15:30 – 16:30 (1 hour)**

In Session 3 you trained a model yourself. Now you will use one Microsoft already
trained — no compute instance, no training, no waiting.

Then everybody cleans up together.

---

## 1. Two ways to get AI

| Train it yourself (Session 3) | Call a ready-made service (now) |
|---|---|
| You need your own data | Microsoft already trained it |
| You need a compute instance — **costs money** | No compute instance at all |
| Takes time and skill | Working in five minutes |
| Best when the problem is specific to you | Best for common tasks: text, speech, vision |

**Rule of thumb:** try the ready-made service first. Only train your own when nothing
off the shelf fits your problem.

---

## 2. Words you need

| Word | What it means |
|---|---|
| **Azure AI services** | Ready-trained models Microsoft hosts: language, vision, speech, translation |
| **AI Language** | The text one — sentiment, key phrases, language detection, entities |
| **Endpoint** | The web address your code sends text to. It looks like a normal URL |
| **Key** | Your password for that endpoint. **Anyone holding it can spend your money** |
| **Free tier (F0)** | A free allowance, plenty for this class. Choose it when creating the resource |
| **SDK** | A Python library that hides the web request, so calling AI looks like calling a function |

---

## 3. Lab 4A — Create the AI Language resource (10 min)

1. In the portal search bar type **`Language`** and choose **Language service**
2. Click **Create**
3. On the "Select additional features" screen, just click **Continue to create your resource**
4. Fill in:

   | Field | What to put |
   |---|---|
   | **Resource group** | **YOUR group** |
   | **Region** | The same one as before |
   | **Name** | `lang-abebe` |
   | **Pricing tier** | **Free F0** |

5. Tick the Responsible AI notice
6. **Review + create** → **Create**
7. When it finishes, click **Go to resource** → **Keys and Endpoint** in the left menu

**Copy two things and keep them somewhere:**
- **KEY 1**
- **Endpoint** (a URL like `https://lang-abebe.cognitiveservices.azure.com/`)

> ### Never put your key in a public repository
> Anybody who finds it can use your subscription. If you ever paste one by accident,
> go back to **Keys and Endpoint** and click **Regenerate Key 1** — the old one stops
> working immediately.

---

## 4. Lab 4B — Call it from Python (25 min)

Open Cloud Shell (the `>_` icon), then:

```bash
pip install azure-ai-textanalytics

# paste your key and endpoint - the quotes matter
export AZURE_LANGUAGE_KEY="paste-your-key-here"
export AZURE_LANGUAGE_ENDPOINT="paste-your-endpoint-here"

python language_demo.py
```

Upload `language_demo.py` to Cloud Shell first using the upload button.

### The whole thing in five lines

```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

client = TextAnalyticsClient(ENDPOINT, AzureKeyCredential(KEY))

for result in client.analyze_sentiment(["The training today was excellent!"]):
    print(result.sentiment, result.confidence_scores)
```

Expected output:

```
positive {'positive': 1.0, 'neutral': 0.0, 'negative': 0.0}
```

This is the same idea as Hugging Face on Day 1 — but hosted, scaled and maintained by
Microsoft, and it understands far more languages.

---

## 5. Lab 4C — Try the other features (10 min)

The same client does several jobs. `language_demo.py` runs all of them:

| Feature | What it answers |
|---|---|
| `analyze_sentiment` | Is this positive or negative? |
| `extract_key_phrases` | What is this text about? |
| `detect_language` | What language is this? |
| `recognize_entities` | Which people, places and dates are mentioned? |

### Try Amharic

On Day 1, the English-trained Hugging Face model scored Amharic near 0.5 — it was
guessing. Run the language detection on:

```
አገልግሎቱ በጣም ጥሩ ነበር።
```

It should identify Amharic correctly. That difference is what a hosted, maintained,
multilingual service buys you.

Try your own sentences in Amharic, Afaan Oromoo and English. Note which features work
well and which do not — that judgement is the real skill.

---

## 6. Lab 4D — Clean up, everybody together (10 min)

**We do this at 16:20. Nobody leaves with a compute instance running.**

1. **ML Studio → Compute →** tick your instance → **Stop** → wait for **Stopped**
2. **Portal → your resource group →** check nothing else says *Running*
3. **Keep** the storage account and the Language resource — they cost almost nothing
4. Optional: to remove everything, open your resource group and click
   **Delete resource group**

Or from Cloud Shell:

```bash
# Stop the compute instance
az ml compute stop --name ci-abebe \
    --workspace-name ml-abebe \
    --resource-group rg-student-abebe

# See what still exists in your group
az resource list --resource-group rg-student-abebe --output table
```

There is a script for this: **`cleanup.sh`** in this folder.

> **Deleting the resource group deletes everything inside it.** That is the fastest
> cleanup — and it cannot be undone.

---

## 7. Files in this folder

| File | What it is |
|---|---|
| `README.md` | This guide |
| `language_demo.py` | All four AI Language features, ready to run |
| `.env.example` | Where to put your key and endpoint safely |
| `cleanup.sh` | Stops compute and shows what is left running |

---

## 8. Day 3 final checklist

- [ ] I accepted the invitation and can sign in to the Azure portal
- [ ] I switched directory and can see my own resource group
- [ ] I created a storage account and uploaded a CSV
- [ ] I ran Azure CLI commands in Cloud Shell
- [ ] I created an ML workspace and trained a model
- [ ] I registered my model in the workspace
- [ ] I created an AI Language resource on the free tier
- [ ] I called it from Python and got results
- [ ] **MY COMPUTE INSTANCE SAYS STOPPED**

The trainer checks the subscription tonight. Anything left running gets stopped and
noted.

---

## 9. If something goes wrong

**`401 Unauthorized` / `Access denied due to invalid subscription key`**
The key or endpoint is wrong. Copy them again from **Keys and Endpoint** — no extra
spaces, and the endpoint must end with a `/`.

**`ModuleNotFoundError: azure.ai.textanalytics`**
Run `pip install azure-ai-textanalytics` first.

**`Free tier F0 is not available`**
You may already have a free Language resource in this subscription — only one is
allowed. Ask the trainer, or choose the lowest paid tier (it costs a few cents).

**`404 Resource not found`**
The endpoint URL is wrong or belongs to a different resource. Check it in the portal.

**My results look wrong for Amharic**
Some features support more languages than others. Language *detection* is very broad;
sentiment is narrower. Checking what a service actually supports is part of the job.

**I cannot find the Stop button in ML Studio**
Click **Compute** in the left menu, tick the checkbox to the left of the instance name,
then Stop appears in the toolbar above.

---

## 10. What you did today

```
   Signed in as a guest with Contributor rights
              |
   Created a storage account and uploaded data
              |
   Did the same thing again with one command
              |
   Rented a computer, trained a model, registered it
              |
   Called an AI service Microsoft already trained
              |
   Switched everything off
```

**Tomorrow — Day 4:** fine-tuning. Take a model that already exists and train it a
little further on your own data, so it specialises for your task.

---

**Back to:** [Day 3 overview](../README.md)
