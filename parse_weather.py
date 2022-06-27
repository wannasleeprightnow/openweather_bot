def parse_weather(weather_json: dict) -> dict[str: str]:
    weather: dict = {
        "Город": f'{weather_json.get("name")}',
        "Погода": f'{weather_json.get("weather")[0].get("description")}',
        "Температура": f'{round(weather_json.get("main").get("temp"))}°c, \
ощущается как {round(weather_json.get("main").get("feels_like"))}°c',
        "Видимость": f'{weather_json.get("visibility")}м',
        "Влажность": f'{weather_json.get("main").get("humidity")}%',
        "Давление": f'{round((weather_json.get("main").get("pressure")) / 1.333)}мм. рт. ст',
        "Облачность": f'{weather_json.get("clouds").get("all")}%',
        "Ветер": f'{round(weather_json.get("wind").get("speed"))}м/с'
    }
    return weather
