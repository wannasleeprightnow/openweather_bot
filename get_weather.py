import requests


def get_weather(API_KEY: str, request_city: str, LANG: str) -> dict:
    url: str = f"https://api.openweathermap.org/data/2.5/weather?q={request_city}&appid={API_KEY}&lang={LANG}&units=metric"

    response: dict = dict(requests.get(url).json())

    return "Произошла ошибка.\nПроверьте корректность ввода города и кода страны." if response["cod"] == "404" \
        else response
