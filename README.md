# Openweather-telegram-bot
Бот, отправляющий информацию о погоде в настоящее время.\
/weather City, Country Code. Например: "/weather Moscow, RU".

## Запуск


Клонирование репозитория:

```bash
git clone https://github.com/enoughtless/openweather_bot.git openweather_bot
cd openweather_bot
```

Создание и активация виртуального окружения:

```bash
python3 -m venv venv
# Для linux
source venv/bin/activate
# Для windows
source venv\Scripts\activate.bat
```

BOT_TOKEN нужно получить у @BotFather, а API_TOKEN на сайте openweathermap.

```bash
echo "BOT_TOKEN = ""
API_TOKEN = """ > .env
```

Обновление pip, установка зависимостей и запуск:
```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 bot/__main__.py
```