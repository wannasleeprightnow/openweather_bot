import requests

from exceptions import DataNotFound
from config import API_TOKEN


async def get_weather(request_city: str) -> dict:
    url: str = f"https://api.openweathermap.org/data/2.5/weather?q={request_city}&appid={API_TOKEN}&lang=ru&units=metric"

    response: dict = dict(requests.get(url).json())

    return response


async def parse_weather(raw_weather: dict) -> dict[str, str]:
    parsed_weather: dict = {
        "Город": f'{raw_weather.get("name")}',
        "Погода": f'{raw_weather.get("weather")[0].get("description")}',
        "Температура": f'{round(raw_weather.get("main").get("temp"))}°c, \
    ощущается как {round(raw_weather.get("main").get("feels_like"))}°c',
        "Видимость": f'{raw_weather.get("visibility")}м',
        "Влажность": f'{raw_weather.get("main").get("humidity")}%',
        "Давление": f'{round((raw_weather.get("main").get("pressure")) / 1.333)}мм. рт. ст',
        "Облачность": f'{raw_weather.get("clouds").get("all")}%',
        "Ветер": f'{round(raw_weather.get("wind").get("speed"))}м/с'
    }

    return parsed_weather


async def print_weather(parsed_weather: dict) -> str:
    printable_weather: str = '\n'.join([f'{key}: {value}.' for key, value in parsed_weather.items()])
    printable_weather = printable_weather.replace("None", "неизвестно")

    return printable_weather


async def weather(request_city: str) -> str:

    response_weather: dict = await get_weather(request_city)
    if response_weather["cod"] != "200":
        raise DataNotFound
    
    parsed_weather = await parse_weather(response_weather)
    printable_weather = await print_weather(parsed_weather)

    return printable_weather
