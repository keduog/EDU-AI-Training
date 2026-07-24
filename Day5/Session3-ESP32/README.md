# Day 5 · Session 3 — Build Something Real

**13:45 – 15:15 (1.5 hours)**

An assistant that answers from **your own documents**, checks **live facts**, and can
call **your own code**.

---

## 1. The problem: models make things up

Ask about something the model cannot possibly know, and it will often answer anyway —
confidently, plausibly, and wrongly.

That is not a bug you can prompt away. It is what a next-word predictor does when it has
no facts: it produces the most *plausible* continuation.

**The fix is not a better model. It is giving it the facts.**

---

## 2. RAG — Retrieval Augmented Generation

```
WITHOUT RAG                          WITH RAG

"What is our leave policy?"          1. find the relevant policy text
        |                            2. put it in the prompt
        v                            3. "Answer using ONLY this text"
model guesses from training                  |
-> confident, plausible, WRONG               v
                                     grounded, checkable answer
```

### Why RAG beats fine-tuning for facts

| | RAG | Fine-tuning |
|---|---|---|
| Cost | cheap, no GPU | GPU hours |
| Time to update | instant — edit the document | a whole new training run |
| Can you cite the source? | ✅ yes | ❌ no |
| Good for facts | ✅ | ❌ |
| Good for style/language | ❌ | ✅ |

This is why RAG is the **default choice in industry** for factual questions.

---

## 3. The labs

Open **`session3_build_something_real.ipynb`**.

| Lab | What you do | Time |
|---|---|---|
| **3A** | Answer from a document, and refuse when it is not covered | 30 min |
| **3B** | Chunking a document too big for one prompt | 15 min |
| **3C** | Ground answers in live Google Search, with sources | 20 min |
| **3D** | Function calling — let the model use your Python code | 25 min |

---

## 4. The most important test you will run today

**Test that it refuses.**

```python
questions = [
    "How many days must I attend to be certified?",   # in the document
    "What is the salary for instructors?",            # NOT in the document
    "Who won the World Cup in 2022?",                 # NOT in the document
]
```

The last two must be **refused**. If the model answered them, your system instruction is
not strict enough — tighten it and run again.

> ### "I do not know" is a feature
> An assistant that invents answers is worse than no assistant. In a defence context it
> is not merely unhelpful — it is dangerous.
>
> Instruct it to refuse, then **verify that it does**.

---

## 5. Search grounding

The model's training has a cutoff date. Google Search grounding gives it today's
information — with sources.

```python
config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())])

r = client.models.generate_content(model=MODEL, contents=q, config=config)

meta = r.candidates[0].grounding_metadata
for c in meta.grounding_chunks:
    print(c.web.title, c.web.uri)
```

> **Always print the sources.** An answer you cannot trace is an answer you cannot
> defend.

---

## 6. Function calling

You describe a function. The model decides **when** it is needed. Your code decides
**what** is allowed to run.

```python
def get_trainee_count(day: str) -> dict:
    """Return how many trainees attended a given training day."""
    ...

config = types.GenerateContentConfig(tools=[get_trainee_count])
```

The SDK reads the function signature and docstring automatically — so **write good
docstrings**, because the model reads them to decide when to call.

### The safety boundary

The model can only *request* a call. Your Python code decides what functions exist and
what they may do. **That boundary is your security layer, and you control it entirely.**

---

## 7. A note on honest limitations

The chunking in Lab 3B uses **keyword overlap** — crude but understandable in five
minutes. Production RAG uses **embeddings**: vectors that capture meaning, so "laptop"
matches "computer equipment".

Gemini offers an embeddings API, and that is the natural next step after this course.
We use the simple version so you can see exactly what is happening.

---

## 8. Prompt, RAG or fine-tune?

| Problem | Best tool | Cost |
|---|---|---|
| "Answers are too long" | system instruction | minutes, free |
| "It does not know our policy" | **RAG** | hours, cheap |
| "It does not know today's news" | search grounding | minutes |
| "It must query our database" | function calling | hours |
| "It writes in the wrong style/language" | fine-tuning (Day 4) | days |
| "It must run with no internet" | self-hosted (Day 4) | hardware |

**Try them in that order.** Most problems are solved in the first two rows.

> Yesterday you learned to fine-tune. Today you learn **when not to** — that judgement
> is worth more than either technique.

---

## 9. Checklist

- [ ] My assistant answers from a document I supplied
- [ ] It **refuses** questions the document does not cover
- [ ] I split a longer document into chunks
- [ ] I grounded an answer in Google Search and printed the sources
- [ ] I let the model call a Python function I wrote
- [ ] I can explain RAG in one sentence
- [ ] I replaced the document with something from my own work

---

## 10. If something goes wrong

| Problem | Fix |
|---|---|
| It answers questions it should refuse | Make the instruction stricter and give the exact refusal wording |
| `grounding_metadata` is None | The model did not need to search. Ask something time-sensitive |
| Function is never called | Improve the docstring — the model reads it to decide |
| `TypeError` on function tools | Add type hints (`day: str`) — the SDK needs them |
| Answers are cut off | Raise `max_output_tokens` |

---

**Next:** [Session 4 — Providers, Cost & Capstone](../Session4/README.md)
