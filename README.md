# Applied AI Training: A Five-Day Hands-On Course

A practical, lab-based course that takes institutional users from "what is AI?" to training, fine-tuning, deploying and safely using AI models across Hugging Face, AWS, Google Cloud and Azure, ending with retrieval-augmented generation, function calling and a group capstone.

Designed and delivered by **Kedir Yassin Hussen** (University of Gondar) for [institution / cohort name], [month year].

## Who it is for

Technical staff with basic computer literacy and little or no prior AI experience. Every concept is introduced through a hands-on lab, and every lab ends with a checklist so participants can confirm it worked.

## Course map

| Day | Theme | Sessions |
| --- | --- | --- |
| **1** | Foundations and tools | The AI ecosystem · GitHub basics (fork, clone) · Google Colab and Hugging Face · GitHub Copilot: build a personal website |
| **2** | Training and deploying models | Local Python environment and a first model · Amazon SageMaker training jobs · SageMaker deployment and MLOps · Google Cloud Vertex AI |
| **3** | Cloud AI on Azure | Azure foundations and access · Storage and the Azure CLI · Azure Machine Learning: train and register a model · Azure AI Language services and resource cleanup |
| **4** | Fine-tuning small models | Resource planning · Hugging Face and the Amharic tokenizer problem · LoRA fine-tuning · Evaluating results and publishing an adapter |
| **5** | Building with LLM APIs | What an API is and a first call · Controlling the model (system instructions, streaming, JSON output) · RAG, search grounding and function calling · Providers, cost, security audit and capstone · Edge AI on Jetson Nano |

**Mini-projects:** participants work in three groups on applied projects set in their own institutional context (see [`Mini-Projects/`](Mini-Projects/)).

## What participants learn

- Use GitHub, Google Colab and Hugging Face as everyday tools
- Train a model locally, then on the cloud (AWS SageMaker, Azure ML), and deploy it as a live endpoint
- Fine-tune a small language model with LoRA, and judge honestly whether it improved
- See why low-resource languages such as Amharic cost more to process (tokenization) and what that means in practice
- Call LLM APIs, control their output, and ground answers with retrieval (RAG) and function calling
- Estimate what an AI service will cost before relying on it
- Handle API keys and cloud resources safely, and always clean up what they create

## Teaching principles

- **Hands-on first.** Each session pairs a short concept section with timed labs.
- **Evidence over impressions.** Participants compare outputs on clear criteria and run at least one objective measurement before claiming a model works.
- **Cost awareness.** Every cloud lab ends by deleting its resources; Day 5 includes a cost-estimation exercise.
- **Security by default.** Keys are treated as passwords and stored in secrets, never in code; the capstone includes a security audit before anything is shared.

## Repository structure

```
Day1/            Foundations: AI ecosystem, GitHub, Colab, Hugging Face, Copilot
Day2/            Local training, AWS SageMaker, Google Cloud Vertex AI
Day3/            Azure: access, storage and CLI, Azure ML, AI services
Day4/            Fine-tuning: Hugging Face, Amharic tokenization, LoRA, evaluation
Day5/            LLM APIs, model control, RAG and function calling, cost and capstone, edge AI
Mini-Projects/   Group project templates and requirements
```

Each session folder contains the slides (`.pptx`), a `README.md` with step-by-step lab instructions, and the notebooks or scripts used in class.

## Getting started

1. Fork this repository and clone your fork (Day 1, Session 2 walks through this).
2. Open the notebooks in [Google Colab](https://colab.research.google.com) and switch the runtime to GPU where a lab asks for it.
3. For local labs, install Python 3.10+ and run `pip install -r requirements.txt` inside the session folder.
4. Cloud labs (AWS, Google Cloud, Azure) use accounts or subscriptions provided by the trainer; follow each session's README.
5. Store API keys in Colab Secrets or a local `.env` file, never in a notebook or commit.

## Datasets

All datasets in this repository are small and synthetic or public (for example, the Pima Indians Diabetes dataset), created or selected for teaching. They contain no personal or operational data.

## Author

**Kedir Yassin Hussen** · Lecturer in Computer Science, University of Gondar · PhD candidate, Bahir Dar University · AU–BAAI Master Trainer in AI Education
[GitHub](https://github.com/keduog) · [Hugging Face](https://huggingface.co/kedhamyas)

## License

[Choose a license, e.g. CC BY 4.0 for course materials and MIT for code.]
