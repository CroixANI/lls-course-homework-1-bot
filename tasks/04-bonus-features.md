# Task 04: Bonus Features

## Context
На данный момент полностью реализованы:
- `config.py` — конфигурация через `.env`
- `ollama_client.py` — `async def ask_llm(user_message: str) -> str`
- `bot.py` — рабочий Telegram-бот с polling и обработкой текстовых сообщений

Бот работает, но не имеет приветствия, системного промпта и структурированного логирования.

## Goal
Добавить бонусные функции поверх уже работающего кода, не нарушая существующую логику.

## Requirements

### 1. Команда `/start`
В `bot.py` добавить обработчик команды `/start`:
- Отправлять приветственное сообщение на русском языке с кратким описанием бота
- Пример текста:
  ```
  👋 Привет! Я AI-бот на базе локальной модели {OLLAMA_MODEL}.
  Просто напишите мне что-нибудь, и я отвечу.
  Каждое сообщение обрабатывается независимо — истории диалога нет.
  ```
- Зарегистрировать через `CommandHandler("start", start_command)`

### 2. Системный промпт
В `config.py` добавить новую переменную:
- В `.env.example` добавить:
  ```
  SYSTEM_PROMPT=You are a helpful assistant. Answer concisely and clearly.
  ```
- В `config.py` загрузить `SYSTEM_PROMPT` (с дефолтным значением, если не задан)

В `ollama_client.py` обновить функцию `ask_llm`:
- Если `SYSTEM_PROMPT` задан — добавлять его как первое сообщение с ролью `system`
- Формат сообщений Ollama:
  ```python
  messages = [
      {"role": "system", "content": SYSTEM_PROMPT},  # если задан
      {"role": "user", "content": user_message},
  ]
  ```

### 3. Логирование запросов в файл
В `bot.py` настроить дополнительный лог-хендлер:
- Логи пишутся одновременно в консоль **и** в файл `bot.log`
- Формат записи в файл: `timestamp | user_id | username | message_text | response_length`
- Файл `bot.log` добавить в `.gitignore`

## Expected output

Изменения в файлах:
- `config.py` — добавлена константа `SYSTEM_PROMPT`
- `.env.example` — добавлена переменная `SYSTEM_PROMPT`
- `ollama_client.py` — `ask_llm` учитывает системный промпт
- `bot.py` — добавлен `/start`, обновлено логирование
- `.gitignore` — добавлен `bot.log`

## Acceptance criteria
- [ ] Команда `/start` возвращает приветственное сообщение с именем модели
- [ ] Системный промпт применяется ко всем запросам, если задан в `.env`
- [ ] Если `SYSTEM_PROMPT` не задан в `.env` — бот работает как раньше
- [ ] После нескольких запросов файл `bot.log` содержит записи
- [ ] `bot.log` присутствует в `.gitignore`
