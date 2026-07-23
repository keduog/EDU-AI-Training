# Day 4 · Session 2 — Hugging Face & the Amharic Problem

**10:45 – 12:45 (2 hours) · 4 hands-on labs**

Find a model, find a dataset, and **prove the model is bad at Amharic** before trying
to fix it.

---

## 1. Words you need

| Word | What it means |
|---|---|
| **Hugging Face Hub** | The GitHub of AI. 1M+ models, 200k+ datasets, mostly free. |
| **Tokenizer** | Cuts text into pieces the model understands. Each model has its own. |
| **Dataset** | The examples you train on. Today: 83,000 Amharic conversations. |
| **Model card** | The documentation page: training data, licence, known failures. |
| **Baseline** | How the model performs **before** you change anything. |
| **Instruction format** | Rewriting data as "question → answer" so the model learns to reply. |

---

## 2. The Amharic tokenizer problem

A model cannot read letters. It reads **tokens** — numbers standing for pieces of text.

### Remember this from the lecture

BERT tokenizes "The capital of Ethiopia is Addis Ababa" like this:

```
["[CLS]", "the", "capital", "of", "ethiopia", "is", "add", "##is", "ababa", "."]
[  101,   1996,    3007,   1997,    11567,   2003,  2799,  4280,   1012,   102 ]
```

Notice **"addis" split into "add" + "##is"** — the tokenizer had never seen the word
often enough to keep it whole. English words survive; less common words get chopped.

Now apply that same logic to an entire language.

Qwen's tokenizer was trained mostly on **English and Chinese**. Ge'ez script was not a
priority, so Amharic gets chopped into many tiny fragments — often single characters.

| Language | Tokens for the same meaning |
|---|---|
| English | 1.0x |
| French | ~1.3x |
| **Amharic** | **~3.4x** |

### What 3x actually costs you

- 3x more memory for the same sentence
- 3x more compute — so 3x the price, if you are paying
- You hit the model's length limit 3x sooner

**This is not a bug.** Nobody set out to disadvantage Amharic. But someone chose the
training data, and the effect is real.

> **Discussion for the class:** if every Amharic query costs three times an English one,
> who pays for that? What does it mean for building AI services in Ethiopia?

---

## 3. The most important rule of the day

> ### Record the baseline BEFORE you change anything.

If you fine-tune first and test afterwards, you have **no evidence** that anything
improved. You will be guessing, and you will probably fool yourself.

This is the step beginners skip. Do not skip it.

---

## 4. The labs

Open **`session2_huggingface_amharic.ipynb`**.

| Lab | What you do | Time |
|---|---|---|
| **2A** | Measure Amharic vs English token counts yourself | 25 min |
| **2B** | Record baseline answers to 3 Amharic questions | 30 min |
| **2C** | Load the 83,000-example Amharic dataset and inspect it | 35 min |
| **2D** | Format 1,000 examples into question/answer text | 25 min |

---

## 5. The dataset

**`addisai/FineTome-single-turn-dedup-amharic`** — 83,000 Amharic conversations,
built by Ethiopian researchers, free to download.

We use only **1,000 examples** today so training finishes inside the lesson. Real
projects use all 83,000 and run for hours — same code, more patience.

> **This dataset exists because people chose to build it.** The code you run this
> afternoon is ten lines. The dataset took months. Amharic AI is not going to arrive
> by accident.

### Always look at your data first

Ten real examples read carefully will teach you more than 83,000 rows you never opened.
Bad data trains bad models **silently** — the loss still goes down, and the output is
still garbage.

---

## 6. Why `eos_token` matters

When formatting the training text, we end every example with the tokenizer's
end-of-sequence token:

```python
f"### ጥያቄ:\n{question}\n\n### መልስ:\n{answer}{tok.eos_token}"
```

That token tells the model **where the answer stops**. Leave it out and your fine-tuned
model rambles on forever without ending its reply. It is one of the most common
beginner mistakes.

---

## 7. Checklist

- [ ] I searched the Hugging Face Hub and read a model card
- [ ] I measured Amharic vs English token counts
- [ ] I looked at **how** the tokenizer splits Amharic
- [ ] I recorded baseline answers and saved them in `before`
- [ ] I loaded the 83,000-example dataset
- [ ] I looked at real examples before training on them
- [ ] I formatted 1,000 examples into question/answer text

**The `before` answers are the most important thing you have. Do not lose them.**

---

## 8. If something goes wrong

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: datasets` | Run the `!pip install` cell first |
| Dataset download is slow | It is a large file. Give it a few minutes. |
| Amharic shows as boxes or `???` | A font problem in your browser, not a code problem. The token counts are still correct. |
| `KeyError: conversations_amharic` | Check `raw.column_names` — the dataset structure may have changed |
| Colab restarted and `before` is gone | Re-run the baseline cell. This is why we also save it to `baseline.pkl`. |

---

## What you learned

1. **Tokenizers are not neutral.** Amharic costs 3x English on this model.
2. **Baseline before you build.** Without a "before", your "after" proves nothing.
3. **Look at your data.** Bad data trains bad models, silently.

**Next:** [Session 3 — LoRA Fine-Tuning](../Session3/README.md)
