# LLM Engineering

A hands-on learning repository focused on building modern LLM applications with LangChain, LangGraph, prompt engineering, retrieval-augmented generation (RAG), streaming responses, and agent-based workflows.

This project is designed for experimenting with the core ideas behind real-world AI applications, from writing better prompts to building conversational agents and Q&A systems.

## Table of contents

- [Overview](#overview)
- [Repository structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Environment variables](#environment-variables)
- [Notebook walkthrough](#notebook-walkthrough)
- [Project examples](#project-examples)
- [How to run](#how-to-run)
- [Learning outcomes](#learning-outcomes)

## Overview

This repository combines:

- Prompt engineering fundamentals
- LLM provider integration
- Conversation memory and state
- Streaming generation
- Tool-using and agent patterns
- RAG pipelines for document-grounded Q&A
- LangGraph-based workflows and chatbot patterns

The goal is to help you move from basic LLM usage to practical application development with reusable building blocks.

## Repository structure

```text
llm-engineering/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 1-langchain-prompts.ipynb
│   ├── 02-prompt-engineering.ipynb
│   ├── 03-conversation-memory.ipynb
│   ├── 04-llm-providers.ipynb
│   ├── 05-streaming-responses.ipynb
│   ├── 06-basic-tool-agents.ipynb
│   ├── 07-rag-based-qna.ipynb
│   └── 08-introduction-to-rag.ipynb
├── projects/
│   ├── langgraph-chatbot.py
│   └── qna-bot.py
└── .env.example (optional, if added locally)
```

## Prerequisites

Before starting, make sure you have:

- Python 3.10 or newer
- pip or conda for package installation
- A virtual environment
- Access to at least one LLM provider API such as OpenAI, Groq, Anthropic, Google Gemini, or a local model endpoint

## Setup

1. Clone the repository:

```bash
git clone <repo-url>
cd llm-engineering
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a local `.env` file with your API keys:

```bash
cp .env.example .env
```

If there is no `.env.example`, create `.env` manually.

## Environment variables

Depending on the notebooks and apps you use, you may need keys like:

```bash
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
EXPLABS_API_KEY=your_explabs_key
```

The project includes examples for multiple providers, so you can swap models and APIs without changing the core workflow structure.

## Notebook walkthrough

The notebooks in this repo are arranged as a progression from foundational LLM concepts to production-style patterns:

- `1-langchain-prompts.ipynb`  
  Introduction to LangChain primitives and prompt construction.

- `02-prompt-engineering.ipynb`  
  Strategies for designing clearer, more reliable prompts and improving model behavior.

- `03-conversation-memory.ipynb`  
  Understanding conversational state, memory, and chat history management.

- `04-llm-providers.ipynb`  
  Connecting with different LLM providers and comparing integration patterns.

- `05-streaming-responses.ipynb`  
  Working with token streaming for more interactive experiences.

- `06-basic-tool-agents.ipynb`  
  Building tool-using agents that can reason and act on external capabilities.

- `07-rag-based-qna.ipynb`  
  Building a Q&A system grounded in knowledge sources using retrieval.

- `08-introduction-to-rag.ipynb`  
  Core ideas behind retrieval-augmented generation, chunking, indexing, and retrieval quality.

## Project examples

### Q&A bot

File: `projects/qna-bot.py`

This is a Streamlit application that uses LangChain and an LLM API to answer questions in a simple chat interface.

Run it with:

```bash
streamlit run projects/qna-bot.py
```

### LangGraph chatbot

File: `projects/langgraph-chatbot.py`

This example demonstrates a small chatbot built with LangGraph and in-memory checkpointing. It shows how to define a state graph and keep conversational context across messages.

Run it with:

```bash
python projects/langgraph-chatbot.py
```

## How to run

### Jupyter notebooks

Launch Jupyter from the project root:

```bash
jupyter notebook
```

Then open the notebook files in the `notebooks/` directory.

### Streamlit app

```bash
streamlit run projects/qna-bot.py
```

### CLI chatbot

```bash
python projects/langgraph-chatbot.py
```

## Learning outcomes

By the end of this project, you should be able to:

- Design and improve prompts for LLMs
- Connect to multiple model providers through a common abstraction
- Build chat experiences with memory and state
- Stream responses for better UX
- Create simple tool-enabled agents
- Implement RAG workflows for grounded Q&A
- Explore LangGraph patterns for stateful application logic
