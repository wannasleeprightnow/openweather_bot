from telegram import Update
from telegram.ext import ContextTypes

from weather import weather
from exceptions import DataNotFound


async def start_help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Привет!\n'
        'Я могу подсказать тебе погоду.\n'
        'Чтобы узнать погоду в нужном тебе городе введи:\n'
        '"/weather City, Country Code".\n'
        'Например: "/weather Moscow, RU".\n'
    )


async def weather_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        request_city = update.message.text.split(" ")[1]
        await update.message.reply_text(await weather(request_city))
    except IndexError:
        await update.message.reply_text("Произошла ошибка. Введены неверные данные.")
    except DataNotFound:
        await update.message.reply_text("Произошла ошибка. Попробуйте позже.")


