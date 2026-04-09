# Task 03: Telegram Bot Core

## Context
На данный момент реализованы:
- `config.py` — загружает `TELEGRAM_TOKEN`, `OLLAMA_BASE_URL`, `OLLAMA_MODEL`
- `ollama_client.py` — содержит `async def ask_llm(user_message: str) -> str`
- `bot.py` — пустая заглушка, которую нужно заполнить

Архитектура: `Telegram → Bot → LLM → Bot → Telegram`
Telegram Bot API используется через **polling** (не webhook).

## Goal
Реализовать `bot.py` — главный файл бота, точка входа для запуска из консоли.

## Requirements

1. Использовать библиотеку `python-telegram-bot==21.3` (async API, `Application`).

2. Реализовать **обработчик текстовых сообщений** `handle_message`:
   - Принимает любое текстовое сообщение от пользователя
   - Пока LLM обрабатывает запрос — отправить пользователю статус `"⏳ Думаю..."`
     (используя `await context.bot.send_chat_action(...)` или отдельное сообщение)
   - Вызвать `ask_llm(user_message)` из `ollama_client.py`
   - Ответить пользователю полученным текстом

3. Обработка ошибок в обработчике:
   - Обернуть вызов в `try/except`
   - При любой неожиданной ошибке отправить пользователю:
     `"❌ Произошла ошибка. Попробуйте ещё раз позже."`
   - Залогировать ошибку через стандартный `logging`

4. Настроить `logging` в начале файла:
   ```python
   logging.basicConfig(
       format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
       level=logging.INFO
   )
   ```

5. Функция `main()`:
   - Создаёт `Application` с токеном из `config.py`
   - Регистрирует `MessageHandler` для `filters.TEXT & ~filters.COMMAND`
   - Запускает polling через `application.run_polling()`

6. Точка входа:
   ```python
   if __name__ == "__main__":
       main()
   ```

## Expected output

Файл `bot.py` с полной реализацией бота.

## How to run
```bash
source venv/bin/activate
python bot.py
```

## Acceptance criteria
- [ ] Бот запускается командой `python bot.py` без ошибок
- [ ] Бот отвечает на любое текстовое сообщение в Telegram
- [ ] Пока генерируется ответ — пользователь видит индикатор активности
- [ ] Если Ollama недоступна — бот не падает, а отвечает понятным сообщением
- [ ] В консоли видны INFO-логи о входящих сообщениях
- [ ] Polling корректно останавливается по Ctrl+C
