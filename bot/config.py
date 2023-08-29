from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = getenv("BOT_TOKEN")
API_TOKEN: str = getenv("API_TOKEN")