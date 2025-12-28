# 🧠 AURA Research Architect

## Self-Evolving Cognitive Pipeline for Autonomous Research Synthesis

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![DSPy](https://img.shields.io/badge/DSPy-Powered-6366f1?style=for-the-badge)](https://github.com/stanfordnlp/dspy)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)

---

### ⚠️ EARLY PREVIEW (Under Development)
**This project is currently in its DEMO stage. Features and architectures are subject to refinement.**

---

## 🌟 What is AURA?

**AURA** (Autonomous Universal Research Architect) is a next generation research synthesis system built on the **DSPy** framework. It transforms research questions into structured, grounded insights through a multi stage cognitive pipeline.

Unlike traditional RAG systems, AURA features:

*   🔄 **Self-Evolving Prompts**: Automatically optimizes prompts using DSPy's compilation.
*   🧠 **Multiple Reasoning Modes**: Standard RAG, Multi Hop, ReAct Agents, and Self-Reflection.
*   💸 **Hybrid LLM Engine**: Works with free local models (Ollama) or cloud APIs (DeepSeek, OpenAI).
*   📊 **Intrinsic Evaluation**: Built in quality assessment using LLM as judge metrics.

---

## 🎯 Core Features

### 🏗️ Cognitive Architectures

| Mode | Description | Best For |
| :--- | :--- | :--- |
| **Standard RAG** | Classic Rewrite Retrieve Read flow | Factual research |
| **Multi-Hop** | Iterative context chaining | Complex investigations |
| **ReAct Agent** | Autonomous tool orchestration | Dynamic problem solving |
| **Reflector** | Self reflection and quality filtering | High stakes synthesis |

### 🔌 Hybrid Engine
*   **Ollama (Free/Local)**: Run Llama3, Phi-3, or Mistral on your own hardware.
*   **DeepSeek API**: High performance, low-cost intelligence.
*   **OpenAI API**: Industry leading frontier models.

---

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone thttps://github.com/yusufcalisir/AURA-Research-Architect.git
cd AURA-Research-Architect

# Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Local Setup (Ollama)

```bash
# Pull your preferred model
ollama pull llama3
# For faster performance on low-end PCs:
ollama pull phi3
```

### 3. Launch

```bash
streamlit run app.py
```

---

## 📁 Project Overview

*   `app.py`: The primary Streamlit interface.
*   `src/modules/`: Core DSPy module logic (RAG, Multi-Hop, etc.).
*   `src/signatures/`: Input/output definitions for LLM tasks.
*   `pipelines/`: Optimization scripts for compiling prompts.
*   `evaluation/`: Performance tracking and quality metrics.

---

## 🗺️ Roadmap (Next Steps)

- [ ] **Custom KB**: PDF and Markdown document upload support.
- [ ] **Memory**: Persistent conversation and research history.
- [ ] **Reports**: Automated PDF/Markdown research report generation.
- [ ] **Optimization**: Advanced MIPRO v2 training pipelines.

---

## 🤝 Contributing

This is an open "Work in Progress." Feel free to fork, open issues, or submit PRs to help evolve the AURA architecture.

---

**Built with 💜 by Yusuf Çalışır**
*AURA-Research-Architect*


