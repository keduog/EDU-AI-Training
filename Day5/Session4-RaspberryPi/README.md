# Day 5 · Session 4 — Providers, Cost, Safety & Capstone

**15:30 – 16:30 (1 hour)**

Compare providers, estimate a real bill, audit your own security, and finish the week.

---

## 1. You are not locked in

| Provider | Free tier | Get a key | Strength |
|---|---|---|---|
| **Google Gemini** | Yes, no card | aistudio.google.com/apikey | Huge context, built-in search grounding |
| **Groq** | Yes | console.groq.com | Very fast, runs open models |
| **OpenRouter** | Some free models | openrouter.ai | One key, hundreds of models |
| **Hugging Face** | Yes | huggingface.co/settings/tokens | Open models — including yours from Day 4 |
| **Ollama** (local) | Free forever | no key needed | Offline, data never leaves the machine |

**Most providers copy OpenAI's request format**, so switching is often a two-line change.
That protects you from lock-in and makes your skills portable.

---

## 2. What would this actually cost?

You will be asked this by a manager one day. Here is how to answer.

```
SCENARIO A - small department help desk
  200 requests/day, 500 input + 300 output tokens each

  requests / month :        6,000
  input tokens     :    3,000,000   $    4.50
  output tokens    :    1,800,000   $   13.50
  --------------------------------------------
  ESTIMATED TOTAL                   $   18.00 / month
```

```
SCENARIO B - university-wide student assistant
  5,000 requests/day, 800 input + 400 output tokens each

  ESTIMATED TOTAL                   $  630.00 / month
```

### The lesson

Scenario A is affordable. Scenario B is a real financial decision needing approval.

**Notice what drives the cost:** output tokens are usually far more expensive than input
tokens. *Asking for shorter answers is one of the cheapest optimisations available* —
and a system instruction does it for free.

> Prices change constantly. Always check the current pricing page. But the **method**
> never changes: count requests, count tokens, multiply.

---

## 3. Three things to check before using free tier for real work

1. **Daily cap** — will your usage fit? Free quotas reset on a fixed schedule, not a
   rolling 24 hours.
2. **Data policy** — free-tier prompts may be used to improve the model. **Read the
   terms.**
3. **Availability** — free tiers carry no uptime guarantee.

> For anything sensitive, point 2 alone rules out the free tier. That is exactly what
> Day 4 was for: a fine-tuned small model on your own hardware sends nothing anywhere.

---

## 4. Security audit — before anything is shared

Every point below is a real incident that happens somewhere every week.

- [ ] Search the notebook for `AIzaSy` — if it appears, the key is exposed
- [ ] Every key comes from `userdata.get()` or `os.environ`
- [ ] **Clear all outputs** before sharing — keys can sit in old output cells
- [ ] No real personal data was pasted into a prompt while learning
- [ ] If a key ever leaked: **delete it in AI Studio and create a new one, immediately**
- [ ] Nothing sensitive was sent to a free-tier endpoint

The notebook includes an automated checker for the first three.

> Deleting a leaked key takes 30 seconds. Explaining an unexpected bill, or leaked data,
> takes considerably longer.

---

## 5. The capstone

Build **one assistant** that would genuinely help someone in your department.

### Requirements

1. A clear system instruction defining its role
2. Answers grounded in a document *or* live search
3. **Refuses politely** when it does not know
4. Error handling that survives a rate limit
5. Works with questions in English **and** Amharic

### Ideas

- An Amharic study helper for your students
- A policy question-answerer for your department
- A report summariser
- A lesson-plan generator
- A translation checker

### Then publish it

The notebook generates a standalone `capstone_assistant.py` — with **no key inside it**,
reading from the environment instead. Download it, add it to your `EDU-AI-Training`
repository under `Day5/`, commit and push.

---

## 6. Day 5 final checklist

- [ ] API key created and stored in Colab Secrets (not in code)
- [ ] Made API calls with a system instruction
- [ ] Streamed a response
- [ ] Built a multi-turn chat
- [ ] Parsed structured JSON output
- [ ] Handled a 429 rate-limit error without crashing
- [ ] Built an assistant that answers from a document
- [ ] It refuses questions it cannot answer
- [ ] Grounded an answer in live web search with sources
- [ ] Audited the notebook for leaked keys
- [ ] Saved the capstone and pushed it to GitHub

---

## 7. The whole week

```
DAY 1   The AI ecosystem, GitHub, Colab, Hugging Face, Copilot
DAY 2   Local Python and cloud AI platforms
DAY 3   Microsoft Azure: guest access, storage, ML workspace, AI services
DAY 4   One neuron -> 494M parameters -> LoRA fine-tuning for Amharic
DAY 5   APIs: rent a large model, control it, ground it, ship it
```

### Three ideas that ran through all five days

1. **Know what things cost.** GPU memory, cloud bills, API tokens. Every technical
   decision is also a budget decision.
2. **Prove what you claim.** Baseline before fine-tuning. Cite your sources. Say what
   did *not* improve.
3. **Choose the smallest tool that solves the problem.** Prompt before RAG. RAG before
   fine-tuning. API before buying hardware — unless you need offline or privacy, and
   then the reverse.

### What you can now do

Build, fine-tune, deploy and integrate AI systems — using tools that were free or nearly
free the entire week.

**Now go and build something your institution actually needs.**

---

**Back to:** [Day 5 overview](../README.md)
