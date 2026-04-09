import logging

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from config import OLLAMA_MODEL, TELEGRAM_TOKEN
from ollama_client import ask_llm

# --- Настройка логирования ---
_log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

_console_handler = logging.StreamHandler()
_console_handler.setFormatter(_log_formatter)

_file_handler = logging.FileHandler("bot.log", encoding="utf-8")
_file_handler.setFormatter(_log_formatter)

logging.basicConfig(level=logging.INFO, handlers=[_console_handler, _file_handler])
logger = logging.getLogger(__name__)

# Отдельный логгер для структурированных записей запросов
_request_logger = logging.getLogger("requests")
_request_file_handler = logging.FileHandler("bot.log", encoding="utf-8")
_request_file_handler.setFormatter(logging.Formatter("%(message)s"))
_request_logger.addHandler(_request_file_handler)
_request_logger.propagate = False


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start — отправляет приветственное сообщение."""
    text = (
        f"👋 Привет! Я AI-бот на базе локальной модели {OLLAMA_MODEL}.\n"
        "Просто напишите мне что-нибудь, и я отвечу.\n"
        "Каждое сообщение обрабатывается независимо — истории диалога нет."
    )
    await update.message.reply_text(text)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    user = update.effective_user
    logger.info("Сообщение от %s (id=%s): %s", user.full_name, user.id, user_message)

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING,
    )

    try:
        reply = await ask_llm(user_message)
    except Exception as e:
        logger.error("Неожиданная ошибка при вызове LLM: %s", e, exc_info=True)
        reply = "❌ Произошла ошибка. Попробуйте ещё раз позже."

    # Структурированная запись: timestamp | user_id | username | message_text | response_length
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    username = user.username or user.full_name or "unknown"
    _request_logger.info(
        "%s | %s | %s | %s | %d",
        timestamp,
        user.id,
        username,
        user_message,
        len(reply),
    )

    await update.message.reply_text(reply)


def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    logger.info("Бот запущен. Нажмите Ctrl+C для остановки.")
    application.run_polling()


if __name__ == "__main__":
    main()
