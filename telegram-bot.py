import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          MessageHandler, filters)
from chatgpt_client import request_chat_gpt

load_dotenv("ks.env")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
TELEGRAM_API_TOKEN = os.getenv("WIPITO_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = request_chat_gpt(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()
