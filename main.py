from aiogram import Bot, Dispatcher, executor, types

from TOKENS import TOKEN, API_KEY
from get_weather import get_weather
from print_weather import print_weather

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot)

LANG: str = "ru"


@dp.message_handler(commands=["start"])
async def welcome_message(message: types.Message):
    await message.answer(
        'Привет!\n'
        'Я могу подсказать тебе погоду.\n'
        'Чтобы узнать погоду в нужном тебе городе введи:\n'
        '"/weather City, Country Code".\n'
        'Например: "/weather Moscow, RU".\n'
    )


@dp.message_handler(commands=["weather"])
async def send_weather(message: types.Message):
    request_city: str = message.text[8:]
    weather_dict: dict = get_weather(API_KEY, request_city, LANG)
    await message.answer(print_weather(weather_dict))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
