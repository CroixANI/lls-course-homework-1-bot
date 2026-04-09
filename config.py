import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:0.6b")

if not TELEGRAM_TOKEN:
    raise ValueError(
        "TELEGRAM_TOKEN is not set. "
        "Please copy .env.example to .env and fill in your Telegram bot token."
    )
