from telegram import Update
from telegram.ext import CallbackContext

async def hello_command_handler(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello!')

COMMAND_HANDLERS = {
    "hello": hello_command_handler
}