# Master Prompt — Telegram Bot with Local LLM

## Описание проекта

Telegram-бот на Python, который принимает текстовые сообщения от пользователя,
передаёт их в локальную LLM через Ollama и возвращает ответ.
Каждое сообщение обрабатывается независимо — история диалога не хранится.

---

## Стек технологий

| Компонент | Технология |
|---|---|
| Язык | Python 3.11+ |
| Виртуальное окружение | `venv` (стандартный) |
| Telegram Bot API | `python-telegram-bot==21.3` (async) |
| Локальная LLM | Ollama + `qwen3:0.6b` |
| Конфигурация | `python-dotenv` + `.env` файл |
| Запуск | Прямой запуск из консоли: `python bot.py` |

---

## Структура проекта

```
homework-1-bot/
├── .env                   ← ❌ НЕ коммитить! В .gitignore
├── .env.example           ← ✅ Шаблон без реальных значений
├── .gitignore
├── requirements.txt
├── config.py              ← Загрузка конфига из .env
├── ollama_client.py       ← Клиент для Ollama LLM
├── bot.py                 ← Точка входа, Telegram polling
├── README.md
├── master-prompt.md       ← Этот файл
└── tasks/
    ├── 01-project-setup.md
    ├── 02-llm-client.md
    ├── 03-bot-core.md
    ├── 04-bonus-features.md
    └── 05-readme.md
```

---

## ⚠️ Критически важно: безопасность секретов

**НИКОГДА не коммитить в git:**
- Файл `.env` (содержит реальный токен Telegram)
- Любые файлы с реальными токенами, паролями или API-ключами

**Перед первым `git add` убедиться:**
1. Файл `.env` присутствует в `.gitignore`
2. Выполнить `git status` и проверить, что `.env` не в списке файлов для коммита
3. В репозиторий попадает только `.env.example` с заглушками

**Если токен случайно попал в коммит:**
1. Немедленно отозвать токен в @BotFather (`/revoke`)
2. Получить новый токен
3. Очистить историю git (через `git filter-branch` или BFG Repo Cleaner)

---

## Порядок выполнения задач

Задачи выполняются **последовательно**. Каждая следующая задача опирается на результаты предыдущей.

### Task 01 — Project Setup
**Файл:** `tasks/01-project-setup.md`

Создать скелет проекта. LLM должна сгенерировать:
`.gitignore`, `.env.example`, `requirements.txt`, `config.py`, заглушки для `ollama_client.py` и `bot.py`.

**Промпт для LLM:**
```
Прочитай файл tasks/01-project-setup.md и реализуй все требования из него.
Создай все указанные файлы в корне проекта.
```

**Review checklist:**
- `.env` в `.gitignore`
- `config.py` бросает ошибку при отсутствии токена
- Можно выполнить `pip install -r requirements.txt`

---

### Task 02 — Ollama LLM Client
**Файл:** `tasks/02-llm-client.md`

Реализовать `ollama_client.py`. LLM должна написать асинхронную функцию
`ask_llm(user_message)`, которая обращается к Ollama и обрабатывает ошибки соединения.

**Промпт для LLM:**
```
Прочитай файл tasks/02-llm-client.md.
В проекте уже есть config.py (экспортирует OLLAMA_BASE_URL и OLLAMA_MODEL).
Реализуй ollama_client.py согласно требованиям.
```

**Review checklist:**
- Функция `async def ask_llm`
- Нет хранения истории
- `python ollama_client.py` возвращает ответ от модели
- Ошибка возвращается как строка, не как исключение

---

### Task 03 — Telegram Bot Core
**Файл:** `tasks/03-bot-core.md`

Реализовать `bot.py`. LLM должна написать бота на `python-telegram-bot` с polling,
обработчиком текстовых сообщений и базовым логированием.

**Промпт для LLM:**
```
Прочитай файл tasks/03-bot-core.md.
В проекте уже есть:
- config.py с TELEGRAM_TOKEN
- ollama_client.py с функцией ask_llm(user_message: str) -> str
Реализуй bot.py согласно требованиям.
```

**Review checklist:**
- `python bot.py` запускается без ошибок
- Бот отвечает на сообщения в Telegram
- При недоступной Ollama — бот живёт и отвечает пользователю
- Polling останавливается по Ctrl+C

---

### Task 04 — Bonus Features
**Файл:** `tasks/04-bonus-features.md`

Добавить `/start`, системный промпт и логирование в файл.
Это бонусные улучшения поверх работающего кода.

**Промпт для LLM:**
```
Прочитай файл tasks/04-bonus-features.md.
Текущее состояние проекта:
- config.py: загружает TELEGRAM_TOKEN, OLLAMA_BASE_URL, OLLAMA_MODEL
- ollama_client.py: async def ask_llm(user_message: str) -> str
- bot.py: работающий Telegram-бот с polling
Внеси изменения согласно требованиям, не нарушая существующую логику.
```

**Review checklist:**
- `/start` возвращает приветствие с именем модели
- Системный промпт применяется если задан в `.env`
- Файл `bot.log` создаётся и наполняется
- `bot.log` в `.gitignore`

---

### Task 05 — README
**Файл:** `tasks/05-readme.md`

Сгенерировать `README.md` для репозитория.

**Промпт для LLM:**
```
Прочитай файл tasks/05-readme.md.
Напиши README.md для проекта Telegram-бот с локальной LLM.
Используй структуру и требования из файла задачи.
Не включай в README реальные токены или секреты.
```

**Review checklist:**
- Команды установки воспроизводимы
- Таблица переменных окружения заполнена
- Описан подход к генерации кода (требование ДЗ)
- Нет реальных токенов

---

## Итоговая проверка перед публикацией в GitHub

```bash
# 1. Проверить, что .env не попадёт в коммит
git status
cat .gitignore | grep .env

# 2. Убедиться, что в репозитории нет секретов
git grep -i "token" -- "*.py" "*.md"

# 3. Проверить финальную структуру
ls -la

# 4. Запустить бота финально
python bot.py
```

---

## Быстрый старт для проверяющего

```bash
git clone <repo-url>
cd homework-1-bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Вставить TELEGRAM_TOKEN в .env
ollama serve &
ollama pull qwen3:0.6b
python bot.py
```
