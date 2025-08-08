from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import log_command, today_command
from config import BOT_TOKEN

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("log", log_command))
app.add_handler(CommandHandler("today", today_command))

if __name__ == "__main__":
    app.run_polling()
