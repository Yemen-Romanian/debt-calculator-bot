import os

from handlers import COMMAND_HANDLERS
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.environ["TG_TOKEN"]

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    for key, value in COMMAND_HANDLERS.items():
        app.add_handler(CommandHandler(key, value))
    app.run_polling()

if __name__ == '__main__':
    main()