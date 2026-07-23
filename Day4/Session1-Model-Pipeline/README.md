# Day 4 · Session 1 — From One Neuron to the Resource Wall

**09:00 – 10:30 (1.5 hours) · Google Colab · Free T4 GPU**

Three things happen this session:

1. **A single neuron** learns a rule nobody told it
2. You **load a real language model** and prompt it
3. You try **Meta's Llama-2-7B** and watch it crash

Everything is free. No Azure, no credit card.

---

## Before you start

1. <https://colab.research.google.com> → sign in
2. **File → New notebook**
3. **Runtime → Change runtime type → T4 GPU → Save** ← do not skip

---

# PART 1 — The magic of a single neuron

## The puzzle (try this before any code)

Someone invented an operation called **⭗**. Here is everything you know:

```
4  ⭗  6  ⭗  8   =  100
5  ⭗  7  ⭗  9   =  110
6  ⭗  8  ⭗  10  =  120
8  ⭗  10 ⭗  12  =  140
```

**What is `14 ⭗ 16 ⭗ 18`?  What is `22 ⭗ 24 ⭗ 26`?**

Spend two minutes on it. You have only examples, never the rule — which is **exactly**
the situation every machine learning model is in.

## What a neuron is

```
output  =  w1·x1  +  w2·x2  +  w3·x3  +  b
```

Three **weights** and one **bias**. Four numbers. That is the whole model.

## How it learns — four steps, repeated 1,500 times

| Step | What happens |
|---|---|
| **1. Guess** | `w1·x1 + w2·x2 + w3·x3 + b` — at first, badly |
| **2. Measure error (loss)** | how far off? Think of loss as a **blame score** |
| **3. Share the blame (backpropagation)** | how much did each weight contribute to the error? |
| **4. Nudge** | move each number against its blame, then repeat |

## What you will see

```
epoch     1   loss   13830.9376   guesses [0.6 0.7 0.8 1. ]
epoch   100   loss      24.5328   guesses [ 94.4 107.8 121.1 147.8]
epoch   500   loss       2.0582   guesses [ 98.1 109.  120.  141.9]
epoch  1500   loss       0.0048   guesses [ 99.9 110.  120.  140.1]
```

Then the real test — numbers it has **never seen**:

```
14 ⭗ 16 ⭗ 18  =  200.4      (true answer 200)
22 ⭗ 24 ⭗ 26  =  280.7      (true answer 280)
```

**It learned the rule, not the answers.** Nobody told it anything.

> **This is all of machine learning, in twenty lines.** Everything else in this course
> is the same loop, made bigger.

## Scaling up

| Model | Parameters | vs our neuron |
|---|---|---|
| Our neuron | 4 | 1x |
| BERT-base | 110,000,000 | 27,500,000x |
| **Qwen2-0.5B** | **494,000,000** | 123,500,000x |
| Llama-2-7B (Meta) | 6,740,000,000 | 1,685,000,000x |
| PaLM 540B (Day 1!) | 540,000,000,000 | 135,000,000,000x |

Same loop. More numbers. Trillions of words instead of four examples.

---

# PART 2 — Load a real model and prompt it

## Qwen2-0.5B

494 million parameters. Predicted memory: **494M × 2 bytes ≈ 0.9 GB**.
Measured: **~0.94 GB**. The formula works.

That is **6% of your GPU**. All that free space is what makes training possible later.

## What a language model actually does

**It predicts the next word.** That is all. Everything else emerges from doing it well.

```
prompt = "The capital city of Ethiopia is ___"

next word        probability
--------------------------------------
' Addis'            84.2%   ################
' the'               4.1%   #
' located'           2.8%   #
' a'                 1.9%
```

No lookup table. No database. Just a probability for every word in the vocabulary,
learned by the same guess-blame-nudge loop as our single neuron.

**Try it in Amharic too** — notice the model is much less confident. That is Session 2.

---

# PART 3 — The wall: Meta's Llama-2-7B

Qwen used 6% of the GPU. So why not use something bigger and better?

## Do the arithmetic first (10 seconds)

```
memory_GB  =  parameters  ×  bytes_per_parameter  /  1,073,741,824
```

| Model | Load (fp16) | LoRA | Full FT | Verdict |
|---|---|---|---|---|
| Qwen2-0.5B | 0.9 GB | 1.2 GB | 7.4 GB | ✅ full fine-tuning fits |
| **Llama-2-7B (Meta)** | **12.6 GB** | 15.7 GB | 100.4 GB | ⚠️ **too tight → crashes** |
| Llama-3-70B (Meta) | 130.4 GB | 163.0 GB | 1,043 GB | ❌ will not load |
| PaLM 540B | 1,006 GB | 1,257 GB | 8,047 GB | ❌ ~110 A100 GPUs |

## The trap: you never get all 15 GB

```
GPU reports        : 15.0 GB
CUDA overhead      :  1.3 GB   (context, kernels, workspace)
Actually usable    : 13.7 GB   <-- the REAL wall
```

**Llama-2-7B needs 12.6 GB of weights against 13.7 GB usable.** That leaves under a
gigabyte for activations and KV cache — not enough to run even one short prompt.

> "It has 15 GB and the model is 12.6 GB, so it fits" is **wrong**.

## Prove it: find the wall by hitting it

The notebook allocates half a gigabyte at a time until the GPU refuses:

```
  allocated   0.5 GB
  allocated   1.0 GB
       ...
  allocated  12.5 GB  <-- Llama-2-7B needs this much
  allocated  13.5 GB

>>> CRASHED - torch.cuda.OutOfMemoryError <<<
>>> The GPU refused at 13.5 GB <<<
```

**Recovery:** `Runtime → Restart session`. Nothing is permanently broken.

> ### The real lesson
> The arithmetic predicted this in **ten seconds**. Downloading Llama-2-7B to find out
> would have taken **15+ minutes**. Always do the maths first.

### Why we do not just download it

The notebook uses `init_empty_weights()` to build the genuine Llama-2 architecture on a
"meta" device — **real layer shapes, real parameter count, zero memory, no 13 GB
download**. You get the true numbers instantly.

Cell 15 offers the real download as an optional instructor demo (`REALLY_TRY = True`)
if bandwidth allows.

---

## The choice this forces

You **cannot** run Meta's 7B model here. You **can** run Qwen2-0.5B — and this afternoon
you will fine-tune it into something genuinely useful for Amharic.

**A small model you can actually train beats a big model you can only admire.**

---

## Checklist

- [ ] I trained a single neuron and watched the loss fall to ~0.005
- [ ] It answered 200 and 280 for numbers it had never seen
- [ ] I can describe the four-step learning loop in my own words
- [ ] I loaded Qwen2-0.5B and saw ~0.94 GB used
- [ ] I prompted it and inspected the next-word probabilities
- [ ] I found my GPU's real usable memory by crashing it
- [ ] I can explain why Llama-2-7B will not run here

---

## If something goes wrong

| Problem | Fix |
|---|---|
| `torch.cuda.is_available()` is False | Runtime → Change runtime type → **T4 GPU** → Save |
| "Cannot connect to a GPU" | Free quota is busy. Wait, or pair up with a classmate. |
| The neuron's loss goes to `nan` | Learning rate too high. Keep `lr = 0.005`. |
| Neuron answers are far from 200/280 | Check you ran the full 1,500 epochs |
| Qwen download is slow | ~1 GB the first time. Normal. |
| OOM when you did **not** want one | Runtime → Restart session, re-run from Cell 6 |
| `ModuleNotFoundError: accelerate` | Run the `!pip install -q transformers accelerate` cell |
| Colab disconnected | It idles out after ~90 min. Reconnect and re-run. |

---

## What you learned

| Idea | Why it matters |
|---|---|
| **Guess → blame → nudge → repeat** | That is all learning is, at any scale |
| **494 million vs 4** | Qwen is the same loop, just much bigger |
| **Models output probabilities** | Not facts — a distribution over the vocabulary |
| **You never get the whole GPU** | 15 GB advertised, ~13.7 GB usable |
| **Do the maths first** | 10 seconds of arithmetic beats a 15-minute failed download |

**Next:** [Session 2 — Hugging Face & the Amharic Problem](../Session2/README.md)
