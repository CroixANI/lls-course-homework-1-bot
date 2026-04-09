import ollama

from config import OLLAMA_BASE_URL, OLLAMA_MODEL, SYSTEM_PROMPT


async def ask_llm(user_message: str) -> str:
    """
    Отправляет сообщение пользователя в Ollama и возвращает ответ модели.

    Каждый вызов независим — история не сохраняется.
    Если задан SYSTEM_PROMPT, он добавляется первым сообщением с ролью system.
    При недоступности Ollama возвращает строку с описанием ошибки.
    """
    try:
        messages = []
        if SYSTEM_PROMPT:
            messages.append({"role": "system", "content": SYSTEM_PROMPT})
        messages.append({"role": "user", "content": user_message})

        client = ollama.AsyncClient(host=OLLAMA_BASE_URL)
        response = await client.chat(
            model=OLLAMA_MODEL,
            messages=messages,
        )
        return response.message.content
    except Exception:
        return "⚠️ Не удалось получить ответ от LLM. Убедитесь, что Ollama запущена."


if __name__ == "__main__":
    import asyncio

    response = asyncio.run(ask_llm("Привет! Как дела?"))
    print(response)
