"""
Ollama configuration for ai-dojo notebooks.

The Ollama URL is determined by:
1. OLLAMA_HOST environment variable (set by VS Code, Docker, or shell)
2. Default: http://localhost:11434

To use a remote Ollama server:
    1. Copy .env.example to .env in the project root
    2. Set OLLAMA_HOST=http://your-server:11434
    3. VS Code loads .env automatically; in a terminal, export OLLAMA_HOST
"""
import os

DEFAULT_OLLAMA_URL = "http://localhost:11434"


def get_ollama_url() -> str:
    """
    Get the Ollama server URL.
    
    Returns OLLAMA_HOST from environment, or http://localhost:11434 by default.
    """
    return os.getenv("OLLAMA_HOST", DEFAULT_OLLAMA_URL)
