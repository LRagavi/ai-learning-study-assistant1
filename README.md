# 📚 AI Learning & Study Assistant

A simple demo agent that helps students study by combining:

- **RAG** — retrieves concept explanations from course materials (`data/materials.py`)
- **Tools** — `create_study_plan_tool()` builds a day-wise plan; `generate_quiz_tool()` creates practice questions
- **Memory** — remembers which topics were studied and which quizzes were taken

This is a minimal, dependency-free example (pure Python) meant to illustrate
the core building blocks of an AI agent before scaling up to real
embeddings/vector DBs and LLM calls.

## 📁 Project Structure

```
ai-learning-study-assistant/
├── data/
│   ├── __init__.py
│   └── materials.py     # Course notes + quiz bank (simulated RAG source)
├── main.py               # Agent logic: RAG + Tools + Memory
├── requirements.txt
└── README.md
```

## ▶️ Run it

```bash
git clone https://github.com/<your-username>/ai-learning-study-assistant.git
cd ai-learning-study-assistant
python main.py
```

## 💬 Sample Output

```
=== AI Learning & Study Assistant ===

You: What are Python data structures?
Assistant: Common Python data structures include lists (ordered, mutable), tuples (ordered, immutable), dictionaries (key-value pairs), and sets (unique items).

You: Explain functions
Assistant: Functions are defined using the 'def' keyword. They can take parameters, have default values, and return one or more values.

You: Give me a study plan
Assistant: Here is your study plan:
   Day 1: loops, data structures
   Day 2: functions, oop

You: Quiz me on loops
Assistant: Quiz on 'loops':
   Q1: Which loop is best when you know the exact number of iterations?
   Q2: What keyword stops a loop early in Python?

--- Study Memory ---
Topics studied: data structures, functions
Quiz taken on 'loops' (2 questions)
```

## 🚀 Next Steps (to make it "real")

- Swap the keyword `retrieve()` function for embeddings + a vector DB (FAISS/Chroma)
- Replace hand-written notes with an LLM call (e.g. Anthropic API) that explains concepts on demand
- Auto-generate quiz questions with an LLM instead of a fixed quiz bank
- Persist memory to a file/database so study progress is saved across sessions
- Add a spaced-repetition tool that resurfaces weak topics

## 🗂️ Maps to Use Case #5

| Requirement | Implementation |
|---|---|
| RAG | `retrieve()` searches `data/materials.py` |
| Memory | `Memory` class stores studied topics + quiz history |
| Tools | `create_study_plan_tool()` and `generate_quiz_tool()` |
