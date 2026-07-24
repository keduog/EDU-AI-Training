# Day 5 · Session 2 — Controlling the Model

**10:45 – 12:45 (2 hours) · 5 hands-on labs**

Anyone can send a prompt. Getting **reliable, well-shaped** answers back — in a format
your program can actually use — is the real skill.

---

## 1. System instructions

A system instruction sets the model's role and rules. It applies to **every** message,
and the user never sees it.

```python
config = types.GenerateContentConfig(
    system_instruction=(
        "You are a helpful assistant for the Ethiopian Defense University. "
        "Answer in clear, simple language. "
        "If the question is asked in Amharic, reply in Amharic. "
        "Keep answers under 80 words. "
        "If you do not know something, say so plainly - never invent facts."
    ),
    max_output_tokens=300,
)
```

**This is the single highest-leverage line you will write today.**

---

## 2. ⚠️ The parameter that no longer works

Almost every tutorial online tells you to control creativity with **`temperature`**.

**On Gemini 3.x models that is no longer true.** Google deprecated `temperature`,
`top_p` and `top_k`. They are now **ignored**, and will return an error in future models.

> Source: [ai.google.dev/gemini-api/docs/latest-model](https://ai.google.dev/gemini-api/docs/latest-model)
> — *"Sampling parameter deprecation"*

| ❌ Old way | ✅ New way |
|---|---|
| `temperature: 0.7` | `system_instruction="Answer in exactly one factual sentence."` |
| `temperature: 1.2` | `system_instruction="Be imaginative. Take creative risks."` |

### Why this matters beyond Gemini

The whole industry is moving from **tuning numbers** to **writing clear instructions**.
Instructions are readable, reviewable, and transfer between providers. Numbers are none
of those things.

If you find a tutorial using `temperature` with a Gemini 3.x model, that tutorial is out
of date.

---

## 3. The labs

Open **`session2_controlling_the_model.ipynb`**.

| Lab | What you do | Time |
|---|---|---|
| **2A** | System instructions — give it a role and rules | 25 min |
| **2B** | Streaming — words appear as they are generated | 15 min |
| **2C** | Multi-turn chat — and its hidden token cost | 25 min |
| **2D** | Structured JSON output your program can parse | 25 min |
| **2E** | Rate limits, retries and quota tracking | 20 min |

---

## 4. Streaming

Waiting 8 seconds in silence feels broken. Same total time, completely different feel:

```python
stream = client.models.generate_content_stream(
    model=MODEL,
    contents="Explain how a satellite stays in orbit.")

for chunk in stream:
    if chunk.text:
        print(chunk.text, end="", flush=True)
```

That is how ChatGPT and Gemini feel fast. Nothing clever — they simply stream.

---

## 5. Chat has no memory — and it costs

```python
chat = client.chats.create(model=MODEL)
chat.send_message("My name is Abebe.")
chat.send_message("What is my name?")     # it remembers
```

> ### The hidden cost
> Every turn re-sends the **entire** conversation. Turn 20 costs roughly twenty times
> turn 1 in input tokens. Long chats get expensive quietly.
>
> **Fix:** keep only the last N turns, or ask the model to summarise the conversation
> and start fresh from the summary.

---

## 6. JSON output

Prose is for humans. If your **program** must read the answer, ask for JSON:

```python
config = types.GenerateContentConfig(
    response_mime_type="application/json",
    system_instruction="Return JSON with keys: name, region, population.")

data = json.loads(response.text)     # a real Python dictionary
```

**This is the difference between a demo and a product.**

---

## 7. Rate limits: two different problems

| Symptom | Cause | Fix |
|---|---|---|
| 429 after a burst | per-**minute** limit (RPM) | wait a few seconds, retry |
| 429 all afternoon | per-**day** limit (RPD) | wait for the reset, or upgrade |

Both arrive as HTTP **429** — read the message body to tell them apart. Retrying a
daily-quota error forever will never succeed.

**Always back off exponentially:** wait 1s, then 2s, then 4s. Never retry in a tight
loop — that burns the quota you are waiting for.

Current limits: <https://ai.google.dev/gemini-api/docs/rate-limits>

---

## 8. Checklist

- [ ] I set a system instruction and saw the model obey it
- [ ] I understand that `temperature` is deprecated on Gemini 3.x
- [ ] I controlled style using **instructions in words** instead
- [ ] I streamed a response
- [ ] I built a chat that remembered earlier turns
- [ ] I got valid JSON and parsed it with `json.loads()`
- [ ] I processed a batch without hitting the rate limit

---

## 9. If something goes wrong

| Problem | Fix |
|---|---|
| The system instruction seems ignored | Check you passed `config=config` to the call |
| JSON mode returns prose | Set `response_mime_type` **and** describe the keys in the instruction |
| `json.loads` fails | Print `r.text` first — the model may have wrapped it in a code fence |
| Streaming prints nothing | Some chunks have no text; guard with `if chunk.text:` |
| 429 during the batch cell | Increase the `time.sleep()` between calls |

---

**Next:** [Session 3 — Build Something Real](../Session3/README.md)
