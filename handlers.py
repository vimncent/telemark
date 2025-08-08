from telegram import Update
from telegram.ext import ContextTypes
from logger import store_event
from utils import parse_log_message
from datetime import datetime

async def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    raw_msg = " ".join(context.args)
    event = parse_log_message(raw_msg, update)
    store_event(event)
    await update.message.reply_text(f"Logged: {event['text']}")

async def today_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Today's logs feature is not implemented yet.")
