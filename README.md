<div align="center">
  <h1>AI Dojo: Generative AI</h1>

  <p><b>Training material on generative AI, large language models and AI assistants</b></p>
  <a href="notebooks/dojo.ipynb"><b>Table of Contents</b></a>

<p>
<img src="notebooks/graphics/artwork/ai-dojo.png" width=300 />
</p>

</div>


> **_dōjō_ (道場, Japanese) - a place for immersive learning. Literally, a place to learn the path (_dō_).**

The AI Dojo is a place for learning about AI and data science through Jupyter notebooks: introductory material, code demos, and interactive coding exercises. This repository contains a course on generative AI.

## Course

**Generative AI**: from how language models work to building your own AI assistants. Run proprietary and open LLMs, build Python applications with Retrieval-Augmented Generation (RAG), structured outputs and tool use, and work with vision and speech models.

- **Level**: Intermediate
- **Prerequisites**: Python programming; basics of deep learning are helpful
- **Start here**: [📓 Course agenda](notebooks/index/generative-ai.ipynb)

## Setup

### 1. Install uv

This project uses [uv](https://docs.astral.sh/uv/) to manage Python and the dependencies.

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Install the dependencies

In the repository directory, run:

```bash
uv sync
```

This creates a virtual environment in `.venv` with Python 3.12, all required packages, and the `ai_dojo` helper package that the notebooks import.

<details>
<summary>Without uv</summary>

With Python 3.10–3.12 installed:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

</details>

### 3. Start JupyterLab

```bash
uv run jupyter lab
```

Open [`notebooks/dojo.ipynb`](notebooks/dojo.ipynb), and run [`notebooks/test.ipynb`](notebooks/test.ipynb) to check that everything works.

### 4. Install Ollama and pull models

Most notebooks run open language models locally with [Ollama](https://ollama.com). [Install Ollama](https://ollama.com/download), start it, and pull a chat model and an embedding model to begin with:

```bash
ollama pull qwen3.5:4b
ollama pull nomic-embed-text
```

Each notebook names the models it uses, so you can pull further models as you go. The courses use these models:

| Model | Used for |
|-------|----------|
| `tinyllama`, `qwen3.5:1.7b` | First steps with small models |
| `qwen3.5:4b`, `qwen3.5:9b`, `olmo-3:7b` | Chat, RAG, structured output, tool use, vision |
| `llama3:text`, `llama3:instruct` | Base model vs. chat model |
| `nomic-embed-text`, `mxbai-embed-large` | Text embeddings and RAG |
| `mixtral` | LlamaIndex example (large: skip it on a laptop) |

To use Ollama on another machine, set the environment variable `OLLAMA_HOST`, for example `OLLAMA_HOST=http://my-server:11434` (see [`.env.example`](.env.example)).

### 5. API keys (optional)

A few notebooks show proprietary model APIs, and need an API key:

- [`lm-proprietary-api.ipynb`](notebooks/language-models/lm-proprietary-api.ipynb): a [Poe](https://poe.com/api_key) API key, entered when prompted
- [`lm-intro-llamaindex.ipynb`](notebooks/language-models/lm-intro-llamaindex.ipynb): an [Anthropic](https://console.anthropic.com/) API key in the environment variable `ANTHROPIC_API_KEY`, or entered when prompted

### Your own chat app

To chat with your Ollama models in a ChatGPT-style web interface, follow [Hosting your own AI Chat App - with LibreChat and Ollama](notebooks/language-models/lm-host-librechat.ipynb).

## Repository Structure

```
notebooks/
├── dojo.ipynb          # table of contents
├── index/              # course index notebooks
├── ai/                 # introduction to AI
├── language-models/    # language model notebooks
├── dl/                 # deep learning background
├── .assets/data/       # datasets (see the README there)
└── test.ipynb          # setup check
src/ai_dojo/            # helper package used by the notebooks
```

## Contributing

Notebooks are committed without outputs. To strip outputs automatically on commit, run once:

```bash
uv run nbstripout --install
```

## License

Except where otherwise noted, the training material in this repository is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/) license, see [LICENSE](LICENSE). Third-party figures are credited in their captions. For the sources and licenses of the datasets, see [`notebooks/.assets/data/README.md`](notebooks/.assets/data/README.md).

The `ai_dojo` Python package in [`src/ai_dojo/`](src/ai_dojo/) is licensed under the [MIT License](LICENSE-CODE).
