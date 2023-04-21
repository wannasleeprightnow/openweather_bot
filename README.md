# Telegram_weather_bot
Бот, отправляющий информацию о погоде в настоящее время.
## Принцип работы
Бот делает запрос в openweathermap API, парсит полученную информацию и отправляет пользователю.
## Используемые технологии
 - Взаимодействие с Telegram реализовано при помощи модуля aiogram; 
 - Получение запросов при помощи модуля requests;
## Запуск
Создать бота и получить токен у @BotFather; поместить его в переменную TOKEN в файле TOKENS.
```
mkdir openweather_telegram_bot
cd openweather_telegram_bot
git clone https://github.com/enoughtless/openweather_telegram_bot .
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
