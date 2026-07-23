# Day 4 · Session 3 — LoRA: Fine-Tuning That Actually Fits

**13:45 – 15:15 (1.5 hours)**

Freeze 99.8% of the model, train the other 0.2%, and run it for real on a free GPU.

> The notebook is **self-contained** — it reloads everything, so it works even if Colab
> restarted over lunch.

---

## 1. What fine-tuning actually is

A model is a huge pile of numbers — Qwen2-0.5B has **494 million** of them, learned by
reading enormous amounts of text.

**Fine-tuning** shows it examples of the behaviour you want, and nudges those numbers
to match.

The problem: changing *all* of them is brutally expensive.

| | Full fine-tuning | LoRA |
|---|---|---|
| Numbers trained | 494,000,000 | ~1,000,000 |
| Memory needed | ~8 GB (optimizer alone) | ~2 GB total |
| Fits on free Colab? | Barely, if at all | Comfortably |
| Result file | ~1 GB | **~5 MB** |

---

## 2. How LoRA works, in plain language

1. **Freeze** the entire original model. Nothing in it will change.
2. **Add** small extra matrices ("adapters") beside the attention layers.
3. **Train only the adapters.**

Because the frozen 99.8% needs no gradients and no optimizer state, the memory cost
collapses. You get most of the benefit for a fraction of the resources.

**The payoff:** your fine-tuned result is a 5 MB file. You can email it. You can keep
fifty of them — one per language, per task, per customer — alongside a single copy of
the base model.

---

## 3. The three settings you will touch

```python
LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,                              # rank
    lora_alpha=32,                     # strength
    lora_dropout=0.05,
    target_modules=["q_proj","v_proj"] # which layers
)
```

| Setting | What it means | Normal range |
|---|---|---|
| **`r` (rank)** | Adapter capacity. Higher learns more, uses more memory. | 8 – 32 |
| **`lora_alpha`** | How strongly the adapter affects the model. | usually 2 × r |
| **`target_modules`** | Which layers get adapters. `q_proj`/`v_proj` are the attention layers. | standard choice |

After applying it you should see roughly:

```
trainable params: 1,081,344 || all params: 495,114,240 || trainable%: 0.2184
```

**0.2%.** That is the whole idea.

---

## 4. The labs

Open **`session3_finetune_lora.ipynb`**.

| Lab | What you do | Time |
|---|---|---|
| **3A** | Attach LoRA adapters, see trainable params drop to 0.2% | 20 min |
| **3B** | Run the real fine-tuning (~10 min on a T4) | 40 min |
| **3C** | Save the adapter and see how small it is | 10 min |

---

## 5. Reading the loss while it trains

The `loss` column is the single number to watch.

| What you see | What it means | What to do |
|---|---|---|
| Falling (2.5 → 1.6) | **Learning.** This is what you want. | Nothing. Let it run. |
| Flat | Learning rate too low, or the data is broken | Check your data formatting |
| Jumping wildly | Learning rate too high | Lower it to 1e-4 |
| `nan` | Numerical blow-up | Restart, lower the learning rate |

**Do not close the browser tab** — Colab disconnects and you lose the run.

---

## 6. Why only 1,000 examples and 1 epoch?

So it finishes inside the lesson.

Real projects use all 83,000 examples and train for hours or days. **The code is
identical** — only the numbers change. What you learn here scales directly.

---

## 7. Download your adapter before you leave

> ### Colab deletes everything when the session ends.

In the file panel on the left: right-click the `qwen-amharic-lora` folder → **Download**.

Or push it to Hugging Face in Session 4 — better, because then it is permanent and
shareable.

---

## 8. Checklist

- [ ] I can explain LoRA in my own words
- [ ] I attached adapters and saw ~0.2% trainable parameters
- [ ] GPU memory stayed low — no OOM
- [ ] Training started and the **loss went down**
- [ ] Training finished without crashing
- [ ] I saved the adapter and checked its size
- [ ] I downloaded it (or will push it in Session 4)

---

## 9. If something goes wrong

| Problem | Fix |
|---|---|
| OOM during training | Lower `per_device_train_batch_size` from 4 to 2, or `MAX_LEN` from 384 to 256 |
| Loss is `nan` | Restart, then set `learning_rate=1e-4` |
| Loss does not fall | Check `data[0]["text"]` looks correct — the formatting may be broken |
| `ValueError: target modules not found` | Different model architecture. For Qwen use `["q_proj","v_proj"]`. |
| Training is very slow | Check you are on a **T4 GPU**, not CPU. `torch.cuda.is_available()` must be True. |
| Colab disconnected mid-training | You lose the run. Re-run from Cell 1. Keep the tab visible next time. |
| `!du` shows nothing | You did not run the save cell. Run Cell 8. |

---

## What you learned

1. **Freeze most, train little.** 0.2% of the parameters, most of the benefit.
2. **Loss falling = learning.** The one number to watch.
3. **An adapter is 5 MB.** One base model, many tiny adapters — that is how teams ship.

**Next:** [Session 4 — Evidence & Sharing](../Session4/README.md)
