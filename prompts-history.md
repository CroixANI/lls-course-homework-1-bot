# Получение данных об ДЗ

```md
Сходи в интернет и достань условия домашнего задания с этой страницы https://larchanka.yonote.ru/share/0651382b-e62a-4c82-8da4-d13315ae758b/doc/telegram-bot-s-lokalnoj-llm-NLQbGlDRTJ. Оформи это как markdown файл с именем "homework-1.md" и сохрани его в папку проекта.
```

# Изучал вопрос как все сделать только через запросы к LLM

```md
Есть задача реализовать код для домашнего задания с помощью LLM. 
Основная идея убедиться, что весь код будет полностью написан с помощью LLM. Я буду делать review - либо принимать, либо просить LLM код исправить.

Для реализации основной цели. Мне кажется можно сгенерировать master prompt для LLM в виде markdown файла. 
Который сможет пробежаться по всем подзадачам. 
Подзадачи буду храниться как markdown файлы в папке “tasks” в виде “01-task.md”, “02-task.md” и так далее. 
Каждая подзадача будет содержать prompt с требования к подзадаче и инструкциями по ее реализации. и реализовать их.
Подскажи есть ли альтернативные варианты или может способы улучшить мой подход?

А сами подзадачи и master prompt мы получим на подготовительном этапе.
```

# Генерация запросов к LLM в виде файлов

```md
Отлично тогда продолжим на основе твоего совета.
Описание домашнего задания есть в "homework-1.md".
Изучи домашнее задание, разберись какой код нужен (язык python, venv и прямой запуск из консоли) и предложи вариант разбития на подзадачи. Потом  сформируй для каждой подзадачи promt на основе твоего совета и как договаривались создай для каждой подзадачи markdown файл в папке "tasks" Master prompt тоже сгенерируй и положи как master-prompt.md в главную папку проекта. Мы все будем заносить в git и публиковать в github. Убедись, что наши переменные окружения и ключ телеграмма не попадет в github. Т.е. это должно быть где-то в инструкциях master prompt-а.
```

# Задача 1 - структура проекта

```md
Прочитай файл tasks/01-project-setup.md и реализуй все требования из него.
Создай все указанные файлы в корне проекта.
```

Результат - [PR - 02 - setup project structure](https://github.com/CroixANI/lls-course-homework-1-bot/pull/1)

# Задача 2 - LLM клиент

```md
Прочитай файл tasks/02-llm-client.md.
В проекте уже есть config.py (экспортирует OLLAMA_BASE_URL и OLLAMA_MODEL).
Реализуй ollama_client.py согласно требованиям.
```

Результат - [PR - 03 - implement ollama client](https://github.com/CroixANI/lls-course-homework-1-bot/pull/2)

# Задача 3 - Bot

```md
Прочитай файл tasks/03-bot-core.md.
В проекте уже есть:
- config.py с TELEGRAM_TOKEN
- ollama_client.py с функцией ask_llm(user_message: str) -> str
Реализуй bot.py согласно требованиям.
```

Результат - [PR - 04 - implement bot core logic](https://github.com/CroixANI/lls-course-homework-1-bot/pull/3)

# Задача 3 - Bot - ошибка запуска бота

```md
я запускаю в консоле команду "python3 bot.py" и получаю ошибку
Traceback (most recent call last):   File
"/Users/anichiporovich/Documents/github/claude/llm-course/homework-1-bot/bot.py"
, line
46
, in
<module>
main
()
~~~~
^^
   File
"/Users/anichiporovich/Documents/github/claude/llm-course/homework-1-bot/bot.py"
, line
37
, in
main

изучи причину ошибки и предложи решение
```

Результат - [PR - 05 - fix issue with running bot.py by adjusting the telegram bot dependency](https://github.com/CroixANI/lls-course-homework-1-bot/pull/4)

# Задача 3 - Bot - ошибка - бот не отвечает

```md
Я запустил "python3 bot.py". Ошибок нет. 
Я написал боту в Телеграме "Привет. Кто ты?" и увидел в консоле следующее
2026-04-09 23:32:19,702 - httpx - INFO - HTTP Request: POST https://api.telegram.org/bot.../getUpdates "HTTP/1.1 200 OK" 2026-04-09 23:32:19,705 - __main__ - INFO - Сообщение от Aleksandr Nichiporovich: Привет. Кто ты? 2026-04-09 23:32:19,881 - httpx - INFO - HTTP Request: POST https://api.telegram.org/bot.../sendChatAction "HTTP/1.1 200 OK" 2026-04-09 23:32:22,372 - httpx - INFO - HTTP Request: POST http://localhost:11434/api/chat "HTTP/1.1 200 OK" 2026-04-09 23:32:22,438 - httpx - INFO - HTTP Request: POST https://api.telegram.org/bot.../sendMessage "HTTP/1.1 200 OK"

Но бот мне ответил ошибкой 
⚠️ Не удалось получить ответ от LLM. Убедитесь, что Ollama запущена.

Я в другой консоле сделал "ollama run qwen3:0.6b"

Подскажи как исправить ошибку. хочу чтобы бот в телеграме мне отвечал.
```

Результат - [PR - 06 - fix issue when bot responded with errors even though ollama run](https://github.com/CroixANI/lls-course-homework-1-bot/pull/5)

# Задача 4 - Дополнительные фичи

```md
Прочитай файл tasks/04-bonus-features.md.
Текущее состояние проекта:
- config.py: загружает TELEGRAM_TOKEN, OLLAMA_BASE_URL, OLLAMA_MODEL
- ollama_client.py: async def ask_llm(user_message: str) -> str
- bot.py: работающий Telegram-бот с polling
Внеси изменения согласно требованиям, не нарушая существующую логику.
```

Результат - [PR - 07 - add additional features: log file, start command and etc](https://github.com/CroixANI/lls-course-homework-1-bot/pull/6)

# Задача 5 - README.md

```md
Прочитай файл tasks/05-readme.md.
Напиши README.md для проекта Telegram-бот с локальной LLM.
Используй структуру и требования из файла задачи.
Не включай в README реальные токены или секреты.
```

Результат - [PR - 08 - add README.md](https://github.com/CroixANI/lls-course-homework-1-bot/pull/7)
