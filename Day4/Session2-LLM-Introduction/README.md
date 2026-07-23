# Day 4 · Session 4 — Did It Work? Evidence, Sharing & Judgement

**15:30 – 16:30 (1 hour)**

Compare honestly, publish your adapter, and learn when fine-tuning is the **wrong** tool.

---

## 1. The comparison

Same questions. Same model. One thing changed.

Open **`session4_compare_and_share.ipynb`** and run the before/after cell.

### Judge each answer on three things

| Question | Before | After |
|---|---|---|
| Did it answer **in Amharic**? | | |
| Did it **stop**, or ramble forever? | | |
| Does it sound like **customer service**? | | |

---

## 2. Set your expectations correctly

Ten minutes of training on 1,000 examples produces a **real but modest** change.

**What usually improves**
- ✅ Answering in Amharic more consistently
- ✅ Following the question/answer format
- ✅ Stopping instead of rambling

**What usually does NOT improve**
- ❌ Factual knowledge it never had
- ❌ Reasoning ability
- ❌ Fluency beyond what the base model could already do

> **If you claim more than you can show, that is marketing, not engineering.**
>
> Being able to say clearly what did *not* improve is a professional skill. It is also
> what separates a trustworthy report from a demo that falls apart under questioning.

---

## 3. One objective measurement

Judgement is subjective. The notebook also counts something you can actually verify:
**what percentage of the reply is in Ge'ez script.**

```
Question        BEFORE     AFTER
----------------------------------
Q1                 40%       95%
Q2                 20%       88%
Q3                 55%       91%
----------------------------------
AVERAGE            38%       91%
```

> **Careful with this number.** A higher Amharic ratio means the model *replied in
> Amharic more often*. It does **not** mean the answers are correct or useful.
>
> Measuring the easy thing and claiming it proves the hard thing is a classic mistake —
> and it is everywhere in AI marketing.

---

## 4. Publish your adapter

Your 5 MB adapter can be used by anyone in the world, in three lines of code.

### Get a token
1. <https://huggingface.co/settings/tokens>
2. **New token** → role: **WRITE** → create
3. Copy it — it is shown only once

### Push it
```python
from huggingface_hub import notebook_login
notebook_login()          # paste the WRITE token

model.push_to_hub("YOUR-USERNAME/qwen2-0.5b-amharic-lora")
tok.push_to_hub("YOUR-USERNAME/qwen2-0.5b-amharic-lora")
```

### Anyone can now use your work
```python
from peft import PeftModel
from transformers import AutoModelForCausalLM

base  = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
model = PeftModel.from_pretrained(base, "YOUR-USERNAME/qwen2-0.5b-amharic-lora")
```

**That is a real contribution to Amharic AI.** Someone in Bahir Dar can build on it
tomorrow.

---

## 5. The most valuable lesson: when NOT to fine-tune

**Try these in order.** Most problems stop at step 1.

| Approach | Cost | Time | Use it when |
|---|---|---|---|
| **1. Better prompt** | Free | Minutes | Almost always try first |
| **2. RAG** (look facts up) | Cheap | Hours | The model needs *facts* it does not have |
| **3. Fine-tuning** | Real GPU cost | Days | You need consistent *style, format or language* |

### Fine-tuning is GOOD at
- Style, tone and output format
- Speaking a language more consistently
- Following your organisation's specific instructions
- Sounding like you

### Fine-tuning is BAD at
- Adding facts — **use RAG**, it looks them up and updates instantly
- Fixing what a better prompt would fix
- Making a small model as clever as a large one
- Compensating for bad or tiny data

> **A common and expensive mistake:** fine-tuning a model to memorise a company
> handbook. RAG does that better, cheaper, and updates the moment the handbook changes.

---

## 6. Why this matters beyond the classroom

**Big labs will not fix Amharic for you.** There is no commercial reason for them to
prioritise 60 million speakers. If it happens, people here do it.

**The dataset was the hard part, not the code.** You ran ten lines to fine-tune.
Someone spent months building the 83,000 examples that made it possible.

**Small models are the realistic path.** A 0.5B model that runs on hardware you actually
own beats a 70B model you can only rent.

**This runs on the edge.** A fine-tuned 0.5B model fits on a laptop or a field device —
no internet, no cloud bill, and the data never leaves the device. That connects straight
back to the Edge AI discussion on Day 1.

---

## 7. Day 4 final checklist

- [ ] I know how to check my GPU and its free memory
- [ ] I can predict whether a model will fit before downloading it
- [ ] I triggered an OOM crash on purpose and understand it
- [ ] I measured the Amharic tokenizer penalty
- [ ] I recorded baseline answers before changing anything
- [ ] I attached LoRA adapters and trained the model
- [ ] I compared before and after **honestly**
- [ ] I can say what did NOT improve
- [ ] **I downloaded my adapter or pushed it to Hugging Face**

> Colab deletes everything when the session ends. If your adapter is still only in
> Colab, save it **now**.

---

## 8. If something goes wrong

| Problem | Fix |
|---|---|
| `before` is not defined | Colab restarted. Run Cell 1B to reload from `baseline.pkl`, or re-run the baseline. |
| The "after" answers look no better | Honest and normal for 1,000 examples. Say so. That is a valid result. |
| `push_to_hub` fails with 401 | Your token is missing or is READ-only. Create a new one with **WRITE**. |
| `Repository not found` on push | Change `HF_USERNAME` to your actual Hugging Face username. |
| The adapter folder is missing | You did not run the save cell in Session 3. |

---

## What you learned

1. **Constraints are the skill.** Anyone can train with unlimited GPUs. Making it work
   in 15 GB is the job you will be paid for.
2. **Prove it, do not claim it.** Baseline first, compare honestly, state the limits.
3. **Small, local and yours.** A 0.5B model fine-tuned on Ethiopian data, running on
   Ethiopian hardware, answering in Amharic — that is the whole point.

---

**Tomorrow — Day 5:** deployment and the capstone project.

**Back to:** [Day 4 overview](../README.md)
