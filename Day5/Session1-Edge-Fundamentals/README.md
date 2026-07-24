# Day 5 · Session 1 — What Is an API, and Your First Call

**09:00 – 10:30 (1.5 hours) · Google Colab · No GPU needed**

Yesterday you ran a model on your own GPU. Today you borrow a much larger one — free,
in five minutes, with no GPU at all.

---

## Before class

Create a free Gemini API key. It takes two minutes and needs **no credit card**.

1. Go to **<https://aistudio.google.com/apikey>**
2. Sign in with any Google account
3. Click **Create API key**
4. **Copy it** — it starts with `AIzaSy...` and is shown clearly only once

> If your account cannot create a key, pair up with a classmate. One key is enough for
> two people today.

---

## 1. Words you need

| Word | What it means |
|---|---|
| **API** | Application Programming Interface — a way for your code to ask somebody else's program to do something |
| **API key** | Your password to that service. It identifies you and bills you |
| **Endpoint** | The web address your request goes to |
| **SDK** | A library that hides the HTTP details so calling AI looks like a normal function |
| **Token** | A chunk of text, as on Day 4. APIs charge and rate-limit by tokens |
| **Rate limit** | How many requests you may send per minute and per day |

---

## 2. What actually happens

```
YOUR CODE  ->  REQUEST          ->  GOOGLE'S SERVERS  ->  RESPONSE
(Colab)        prompt + key         Gemini runs on        text comes
               over HTTPS           their GPUs            back
```

**Nothing is installed on your machine.** Your laptop sends a sentence and receives a
sentence. All the computing happens in a Google data centre.

---

## 3. API vs self-hosted — yesterday vs today

| | API (today) | Self-hosted (Day 4) |
|---|---|---|
| Working in | 5 minutes | a day |
| GPU needed | none | yes |
| Model quality | very high | limited by size |
| Works offline | ❌ no | ✅ yes |
| Data leaves your building | ⚠️ yes | ✅ no |
| Cost | grows per request | fixed once you own it |

**Neither is the winner.** A serious organisation uses both — API for reach and
capability, self-hosted for offline, private and cheap-at-scale work.

---

## 4. Your key is a password

> ### NEVER put an API key in your code.
> People run automated scanners over public GitHub repositories and find leaked keys
> within **minutes**. A leaked key gets used by strangers — and if billing is ever
> enabled, you pay for it.

| ❌ Never | ✅ Instead |
|---|---|
| `API_KEY = "AIzaSy..."` in a cell | Colab **Secrets** (key icon, left sidebar) |
| Commit a key to GitHub | Environment variables |
| Paste a key in a screenshot | A `.env` file that is gitignored |
| Share one key by WhatsApp | One key per person |

**If a key ever leaks:** delete it in AI Studio and create a new one. Immediately.

### Storing it in Colab

1. Click the **key icon** in the left sidebar (*Secrets*)
2. **Add new secret**
3. Name: **`GEMINI_API_KEY`** — exactly that
4. Value: paste your key
5. Turn **on** *Notebook access*

---

## 5. The labs

Open **`session1_first_api_call.ipynb`**.

| Cell | What you do |
|---|---|
| 1 | Load the key safely from Colab Secrets |
| 2 | **List the models your key can actually use** |
| 3 | Your first API call |
| 4 | Ask it in Amharic — compare with yesterday's fine-tuned model |
| 5 | See the token counts for a request |
| 6 | A helper that survives rate limits |
| 7 | Your own questions |

### Why Cell 2 matters

**Model names change often.** Rather than trusting any tutorial — including this one —
the notebook asks the API which models your key can use. If `gemini-3.5-flash` is not in
the list, change the `MODEL` variable to one that is.

---

## 6. The first call

```python
!pip install -q -U google-genai

from google import genai

client = genai.Client()          # reads GEMINI_API_KEY from the environment

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain what an API is, in two sentences.",
)

print(response.text)
```

That is the whole thing. No GPU, no download, no OOM crash.

---

## 7. Checklist

- [ ] I created an API key at aistudio.google.com/apikey
- [ ] I stored it in **Colab Secrets**, not in a code cell
- [ ] I listed the models my key can use
- [ ] I sent a prompt and got a real answer
- [ ] I saw the token counts for a request
- [ ] I have a helper function that survives a rate-limit error

---

## 8. If something goes wrong

| Error | Fix |
|---|---|
| `SecretNotFoundError` | Secret name must be exactly `GEMINI_API_KEY`, notebook access ON |
| `API key not valid` | Copy the key again — no spaces, no line breaks |
| `404` / model not found | Run Cell 2 and use a model name from that list |
| `429 RESOURCE_EXHAUSTED` | Rate limit. Wait a minute, or use the `ask()` helper |
| `ModuleNotFoundError: google.genai` | Run the `!pip install` cell first |
| Key works in AI Studio but not Colab | The secret's *Notebook access* toggle is off |

---

**Next:** [Session 2 — Controlling the Model](../Session2/README.md)
