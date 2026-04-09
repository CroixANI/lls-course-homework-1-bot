# Task 01: Project Setup

## Context
Это первая задача проекта. Никаких файлов кода ещё не существует.
Цель проекта — Telegram-бот на Python, который принимает сообщения от пользователя,
передаёт их в локальную LLM (Ollama) и возвращает ответ. Без базы данных, без хранения истории.

## Goal
Создать скелет проекта: структуру папок, виртуальное окружение, зависимости,
конфигурационные файлы и защиту от попадания секретов в git.

## Requirements

1. Создать файл `.gitignore` со следующим содержимым (минимум):
   - `.env`
   - `venv/`
   - `__pycache__/`
   - `*.pyc`
   - `.DS_Store`

2. Создать файл `.env.example` — шаблон переменных окружения (без реальных значений):
   ```
   TELEGRAM_TOKEN=your_telegram_bot_token_here
   OLLAMA_BASE_URL=http://localhost:11434
   OLLAMA_MODEL=qwen3:0.6b
   ```

3. Создать файл `requirements.txt` со следующими зависимостями:
   ```
   python-telegram-bot==21.3
   ollama==0.2.1
   python-dotenv==1.0.1
   ```

4. Создать файл `config.py`, который:
   - Загружает переменные из `.env` с помощью `python-dotenv`
   - Экспортирует три константы: `TELEGRAM_TOKEN`, `OLLAMA_BASE_URL`, `OLLAMA_MODEL`
   - Если `TELEGRAM_TOKEN` не задан — бросает `ValueError` с понятным сообщением

5. Создать пустые файлы-заглушки (просто `pass` или комментарий):
   - `ollama_client.py`
   - `bot.py`

## Expected output

Файлы в корне проекта:
```
.gitignore
.env.example
requirements.txt
config.py
ollama_client.py     ← заглушка
bot.py               ← заглушка
```

## Acceptance criteria
- [ ] `.env` присутствует в `.gitignore`
- [ ] `.env.example` содержит все три переменные (без реальных значений)
- [ ] `config.py` использует `python-dotenv` и поднимает ошибку при отсутствии токена
- [ ] `requirements.txt` содержит все три зависимости с версиями
- [ ] Проект можно инициализировать командами:
  ```bash
  python -m venv venv
  source venv/bin/activate   # Windows: venv\Scripts\activate
  pip install -r requirements.txt
  cp .env.example .env
  ```
