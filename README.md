<div align="center">

# 🧠 AURA Research Architect

### *Self-Evolving Cognitive Pipeline for Autonomous Research Synthesis*

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![DSPy](https://img.shields.io/badge/DSPy-Powered-6366f1?style=for-the-badge)](https://github.com/stanfordnlp/dspy)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br>

> ⚠️ **EARLY PREVIEW** — This project is under active development. Features may change.

<br>

[📚 Documentation](#-architecture) • [🚀 Quick Start](#-quick-start) • [🎯 Features](#-features) • [🔧 Configuration](#-configuration)

</div>

---

## 🌟 What is AURA?

**AURA** (Autonomous Universal Research Architect) is a next-generation research synthesis system built on Stanford's [DSPy](https://github.com/stanfordnlp/dspy) framework. It transforms simple research questions into structured, grounded insights through a multi-stage cognitive pipeline.

Unlike traditional RAG systems, AURA features:

- 🔄 **Self-Evolving Prompts** — Automatically optimizes its own prompts using DSPy's compilation
- 🧠 **Multiple Reasoning Modes** — Standard RAG, Multi-Hop, ReAct Agents, and Self-Reflection
- 💸 **Hybrid LLM Engine** — Use free local models (Ollama) or cloud APIs (DeepSeek, OpenAI)
- 📊 **Built-in Evaluation** — LLM-as-judge metrics for quality assessment

---

## 🎯 Features

### 🏗️ Four Cognitive Architectures

| Mode | Description | Best For |
|------|-------------|----------|
| **Standard RAG** | Query → Retrieve → Synthesize | Quick factual research |
| **Multi-Hop Reasoning** | Iterative retrieval with context chaining | Complex multi-part questions |
| **ReAct Agent** | Autonomous tool use with reasoning traces | Dynamic problem solving |
| **Self-Reflecting Architect** | Generates multiple candidates, selects best | High-stakes synthesis |

### 🔌 Hybrid LLM Engine

```
┌─────────────────────────────────────────────────────────┐
│                   AURA Hybrid Engine                    │
├─────────────────┬─────────────────┬─────────────────────┤
│   🦙 Ollama     │   🌊 DeepSeek   │    🤖 OpenAI       │
│   (Free/Local)  │   (Low Cost)    │    (Premium)       │
│   llama3, phi   │   deepseek-chat │    gpt-4o-mini     │
└─────────────────┴─────────────────┴─────────────────────┘
```

- **Ollama**: Run locally, no API key needed, completely free
- **DeepSeek**: Affordable cloud API with excellent performance
- **OpenAI**: Industry-standard, highest quality outputs

### 📚 Flexible Retrieval

- **Local Knowledge Base**: Built-in mock retriever with curated AI/ML passages
- **ColBERTv2**: Wikipedia knowledge via Stanford's public endpoint
- **Extensible**: Easy to add custom retrievers

---

## 📁 Project Structure

```
AURA/
├── 📄 app.py                    # Streamlit Web Interface
├── 📄 main.py                   # CLI Entry Point
├── 📄 config.py                 # Configuration Constants
│
├── 📂 src/
│   ├── 📂 signatures/           # DSPy Signature Definitions
│   │   ├── search.py            # Query generation signature
│   │   └── synthesis.py         # Research synthesis signature
│   │
│   ├── 📂 modules/              # DSPy Module Implementations
│   │   ├── rag.py               # Standard RAG (AuraArchitect)
│   │   ├── multihop.py          # Multi-Hop Reasoning
│   │   ├── agent.py             # ReAct Agent
│   │   └── reflector.py         # Self-Reflecting Module
│   │
│   └── 📂 utils/
│       └── model_factory.py     # LLM Provider Factory
│
├── 📂 pipelines/                # Optimization & Training
│   ├── optimize_bootstrap.py    # BootstrapFewShot compilation
│   ├── optimize_mipro.py        # MIPRO advanced optimization
│   └── distill.py               # Model distillation
│
├── 📂 evaluation/               # Quality Assessment
│   ├── data.py                  # Gold dataset definitions
│   └── metrics.py               # LLM-as-judge evaluators
│
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai) (for free local inference)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/AURA.git
cd AURA

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull a model (if using Ollama)
ollama pull llama3
# Or for faster inference:
ollama pull phi
```

### Run the Application

```bash
# Start the Streamlit UI
streamlit run app.py

# Or use the CLI
python main.py --help
```

Visit `http://localhost:8501` in your browser.

---

## 🔧 Configuration

### Using Ollama (Free, Local)

1. Install [Ollama](https://ollama.ai)
2. Pull a model: `ollama pull phi` (fast) or `ollama pull llama3` (quality)
3. Select "Ollama (Free/Local)" in the sidebar
4. No API key needed!

### Using Cloud APIs

1. Select "DeepSeek" or "OpenAI" in the sidebar
2. Enter your API key
3. Choose your preferred model

### Environment Variables (Optional)

Create a `.env` file:

```env
OPENAI_API_KEY=sk-...
DEEPSEEK_API_KEY=sk-...
```

---

## 🏛️ Architecture

### DSPy Pipeline Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Research   │────▶│    Query     │────▶│  Retrieval   │
│     Goal     │     │  Generation  │     │   (k=3)      │
└──────────────┘     └──────────────┘     └──────────────┘
                                                 │
                                                 ▼
                     ┌──────────────┐     ┌──────────────┐
                     │   Insight    │◀────│   Passage    │
                     │  Synthesis   │     │   Context    │
                     └──────────────┘     └──────────────┘
```

### Key DSPy Concepts Used

| Concept | Implementation | Purpose |
|---------|----------------|---------|
| **Signatures** | `GenerateSearchQuery`, `ResearchSynthesizer` | Define input/output contracts |
| **Modules** | `AuraArchitect`, `AuraMultiHop` | Encapsulate reasoning pipelines |
| **Predictors** | `dspy.Predict`, `dspy.ChainOfThought` | Execute LLM calls |
| **Retrievers** | `dspy.Retrieve`, `MockRetriever` | Fetch relevant context |

---

## 📊 Optimization & Evaluation

### Self-Evolving Prompts

AURA can automatically improve its prompts using DSPy's compilation:

```bash
# Bootstrap few-shot optimization
python pipelines/optimize_bootstrap.py

# Advanced MIPRO optimization
python pipelines/optimize_mipro.py
```

### Evaluation Metrics

The system includes LLM-as-judge evaluation:

```python
from evaluation.metrics import validate_aura_insight

# Assess quality of generated insights
score = validate_aura_insight(
    research_goal="...",
    generated_insight="...",
    gold_insight="..."
)
```

---

## 🎨 UI Preview

The Streamlit interface features:

- 🌓 **Light/Dark Mode** — Automatically adapts to system theme
- 🎯 **Clean, Minimal Design** — Focus on content, not decoration
- ⚡ **Real-time Progress** — See each pipeline step as it executes
- 📱 **Responsive Layout** — Works on all screen sizes

---

## 🗺️ Roadmap

### Current Version (v0.1-preview)

- [x] Core DSPy architecture (Signatures, Modules)
- [x] Four cognitive modes (RAG, MultiHop, Agent, Reflector)
- [x] Hybrid LLM Engine (Ollama, DeepSeek, OpenAI)
- [x] Local MockRetriever fallback
- [x] Streamlit Web UI
- [x] Basic evaluation pipeline

### Upcoming Features

- [ ] Custom knowledge base upload (PDF, Markdown)
- [ ] Conversation memory & context persistence
- [ ] Advanced optimization with MIPRO v2
- [ ] API endpoint for programmatic access
- [ ] Export research reports (PDF, Markdown)
- [ ] Multi-language support

---

## 🤝 Contributing

This project is in active development. Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Stanford NLP DSPy](https://github.com/stanfordnlp/dspy) — The foundation of this project
- [Ollama](https://ollama.ai) — Making local LLMs accessible
- [Streamlit](https://streamlit.io) — Rapid UI development

---

<div align="center">

**Built with 💜 using DSPy**

*AURA — Transforming questions into structured knowledge*

</div>
#   A U R A - R e s e a r c h - A r c h i t e c t  
 