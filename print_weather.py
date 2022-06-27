from parse_weather import parse_weather


def print_weather(weather_json: dict) -> str:
    weather: dict = parse_weather(weather_json)
    return '\n'.join([f'{key}: {value}.' for key, value in weather.items()])
