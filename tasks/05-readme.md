# Task 05: README

## Context
Проект полностью реализован. Существуют файлы:
- `.gitignore`, `.env.example`, `requirements.txt`
- `config.py`, `ollama_client.py`, `bot.py`
- Папка `tasks/` с описаниями подзадач

Структура проекта:
```
homework-1-bot/
├── .env.example
├── .gitignore
├── requirements.txt
├── config.py
├── ollama_client.py
├── bot.py
└── tasks/
```

## Goal
Написать `README.md` — документацию проекта для сдачи домашнего задания.

## Requirements

README должен содержать следующие разделы:

### 1. Заголовок и описание
- Название проекта: `Telegram-бот с локальной LLM`
- Одно предложение: что делает бот

### 2. Стек технологий
- Python 3.11+
- python-telegram-bot 21.3
- Ollama + qwen3:0.6b
- python-dotenv

### 3. Установка и запуск (пошагово)
```bash
# 1. Клонировать репозиторий
git clone <repo-url>
cd homework-1-bot

# 2. Создать и активировать venv
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Настроить окружение
cp .env.example .env
# Отредактируйте .env — вставьте токен Telegram-бота

# 5. Установить и запустить Ollama
# https://ollama.com/
ollama pull qwen3:0.6b
ollama serve

# 6. Запустить бота
python bot.py
```

### 4. Переменные окружения
Таблица с описанием переменных из `.env.example`:
| Переменная | Описание | Пример значения |
|---|---|---|
| `TELEGRAM_TOKEN` | Токен бота от @BotFather | `123456:ABC-DEF...` |
| `OLLAMA_BASE_URL` | Адрес Ollama API | `http://localhost:11434` |
| `OLLAMA_MODEL` | Название модели | `qwen3:0.6b` |
| `SYSTEM_PROMPT` | Системный промпт (опционально) | `You are a helpful assistant` |

### 5. Использованная LLM и подход к генерации кода
- Описать какую LLM использовали (Ollama + qwen3:0.6b)
- Описать подход: код генерировался с помощью LLM по структурированным промптам из папки `tasks/`
- Упомянуть, что каждая задача имела чёткий контекст, требования и acceptance criteria

### 6. Архитектура
```
Пользователь → Telegram → bot.py → ollama_client.py → Ollama (локально) → ответ обратно
```

## Expected output

Файл `README.md` в корне проекта.

## Acceptance criteria
- [ ] README содержит все 6 разделов
- [ ] Команды установки и запуска корректны и воспроизводимы
- [ ] Таблица переменных окружения заполнена
- [ ] Есть описание подхода к генерации кода (требование домашнего задания)
- [ ] Нет упоминания реального токена Telegram или других секретов
