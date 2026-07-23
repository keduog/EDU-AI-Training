# Day 4 — Fine-Tuning: Making Small Models Work

**Ethiopian Defense University · AI Lab Training · 6 hours**

Everything today is **free**. Google Colab + Hugging Face. No Azure, no credit card.

**The question of the day:** you have 15 GB of GPU memory. What can you actually build?

---

## Schedule

| Time | Session | Folder | Open in Colab |
|---|---|---|---|
| 09:00 – 10:30 | **1. From One Neuron to the Resource Wall** | [`Session1/`](Session1/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keduog/EDU-AI-Training/blob/main/Day4/Session1/session1_resource_wall.ipynb) |
| 10:30 – 10:45 | *Break* | | |
| 10:45 – 12:45 | **2. Hugging Face & the Amharic Problem** | [`Session2/`](Session2/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keduog/EDU-AI-Training/blob/main/Day4/Session2/session2_huggingface_amharic.ipynb) |
| 12:45 – 13:45 | *Lunch* | | |
| 13:45 – 15:15 | **3. LoRA Fine-Tuning** | [`Session3/`](Session3/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keduog/EDU-AI-Training/blob/main/Day4/Session3/session3_finetune_lora.ipynb) |
| 15:15 – 15:30 | *Break* | | |
| 15:30 – 16:30 | **4. Evidence & Sharing** | [`Session4/`](Session4/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keduog/EDU-AI-Training/blob/main/Day4/Session4/session4_compare_and_share.ipynb) |

---

## The story of the day

```
Session 1   One neuron learns a rule -> scale it to 494M params -> prompt a real model
            -> then watch Meta's Llama-2-7B crash on a free GPU.
              ↓
Session 2   The small model you CAN run is bad at Amharic. Here is the evidence.
              ↓
Session 3   LoRA makes fine-tuning fit in 2 GB. Train it for real.
              ↓
Session 4   Did it work? Prove it honestly. Then share it with the world.
```

Two threads run through the day:

**How it works** — a single neuron guessing, being blamed, and nudging its four numbers
is the *same* loop that trains a 494-million-parameter language model.

**What it costs** — resources decide what is possible, and working inside the limit is
the actual skill.

---

## What each folder contains

```
Day4/
├── README.md                                you are here
│
├── Session1/
│   ├── README.md                            neuron demo, prompting, the 15 GB wall
│   ├── Day4_Session1_Resource_Wall.pptx     17 slides
│   └── session1_resource_wall.ipynb         46 cells: neuron -> Qwen prompt -> Llama crash
│
├── Session2/
│   ├── README.md                            tokenizers, baselines, datasets
│   ├── Day4_Session2_HuggingFace_Amharic.pptx
│   └── session2_huggingface_amharic.ipynb   measure the Amharic penalty, record baseline
│
├── Session3/
│   ├── README.md                            what LoRA is and how to configure it
│   ├── Day4_Session3_LoRA_Training.pptx
│   └── session3_finetune_lora.ipynb         the real training run (~10 min)
│
└── Session4/
    ├── README.md                            honest comparison, publishing, judgement
    ├── Day4_Session4_Evidence_and_Sharing.pptx
    └── session4_compare_and_share.ipynb     before/after, push to Hugging Face
```

---

## Before class — trainer setup

**Nothing to provision.** No accounts to create for students, no roles to assign.
Everything runs on free Colab.

### Do these three things

1. **Run the notebooks yourself, start to finish.** Especially Session 3 — time how long
   training takes on the day's network. Free Colab GPU availability varies.
   In Session 1, check that the allocation loop in Cell 14 really crashes on your T4
   and note the number it stops at — you can then quote the real figure in class.
2. **Tell students to create a Hugging Face account** (free, no card) before class, at
   <https://huggingface.co/join>. They need it in Session 4.
3. **Have a backup plan for GPU quota.** Free Colab sometimes refuses a GPU at peak
   times. If that happens, students pair up on one machine — everything still works.

### What could go wrong, and what to do

| Risk | Mitigation |
|---|---|
| No GPU available on free Colab | Pair students up. Or run the CPU-only cells (Sessions 1–2 mostly work without a GPU). |
| Training takes longer than planned | Reduce `N` from 1000 to 500 in Session 3, Cell 3 |
| Slow internet, model download crawls | The base model is ~1 GB. Download it once on the projector first so the class sees it work. |
| Dataset unavailable | Have students inspect the raw dataset page on huggingface.co and use a smaller local sample |

---

## Trainer note — the puzzle answers

Session 1 opens with a puzzle (`4⭗6⭗8=100`, etc.). **The answers are 200 and 280.**

Do not give them away. Let students struggle for two minutes, then let the neuron solve
it in front of them. The point lands much harder that way.

The rule is underdetermined from four examples — several weight combinations fit — but
every consistent solution gives the same answer for the two test cases. The trained
neuron lands on 200.4 and 280.7.

---

## The three things students always get wrong

**1. Forgetting the GPU runtime.**
Runtime → Change runtime type → **T4 GPU**. Without it everything is 50x slower or fails.
(Part 1 of Session 1 — the neuron — runs fine on CPU, so students may not notice until Part 2.)

**2. Skipping the baseline.**
If you fine-tune first and test afterwards, you cannot prove anything improved.
Session 2, Lab 2B is not optional.

**3. Not downloading the adapter.**
Colab deletes everything when the session ends. Push to Hugging Face or download the
folder before leaving.

---

## What students take home

- A working understanding of **why small models matter** — with the arithmetic to back it
- A fine-tuned Amharic adapter, published under their own Hugging Face account
- The habit of **measuring before claiming**
- An honest sense of when fine-tuning is the wrong answer

---

## A note on the bigger picture

Nothing today requires a data centre. A 0.5B model, fine-tuned on Ethiopian data,
running on a free GPU — and later on a laptop or a field device with no internet at all.

That connects directly back to Day 1: **cloud for training, edge for deployment**.
It also makes a harder point. Big labs have no commercial reason to prioritise 60 million
Amharic speakers. If Amharic AI gets built, it gets built by people in this room.

---

## The week

| Day | Topic |
|---|---|
| Day 1 | AI ecosystem, GitHub, Colab, Hugging Face, Copilot |
| Day 2 | Local Python and cloud AI: SageMaker, Google Cloud |
| Day 3 | Microsoft Azure |
| **Day 4** | **Fine-tuning small models** ← you are here |
| Day 5 | Deployment and capstone project |
