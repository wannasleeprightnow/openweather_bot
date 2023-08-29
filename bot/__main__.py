import logging

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler
)

from handlers import (
    start_help_handler, 
    weather_handler
)

from config import BOT_TOKEN

COMMAND_HANDLERS = {
    "start": start_help_handler,
    "help": start_help_handler,
    "weather": weather_handler
}

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))
    application.run_polling()
    

if __name__ == "__main__":
    main()