from telegram.ext import ApplicationBuilder, CommandHandler
from commands import handlers_map
from config import BOT_TOKEN

app = ApplicationBuilder().token(BOT_TOKEN).build()

for handler_name, handler_func in handlers_map.items():
    app.add_handler(CommandHandler(handler_name, handler_func))

if __name__ == "__main__":
    app.run_polling()
