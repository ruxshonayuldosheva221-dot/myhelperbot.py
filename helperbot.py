from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Assalomu alekum! Murojaatingizni bu yerga yozib qoldiring, tez orada javob beramiz. Iltimos, sabrli bo'ling!"
    )

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    admin_id = "7092846654"
    context.bot.send_message(chat_id=admin_id, text=f"Yangi murojaat: {user_message}")
    update.message.reply_text("Murojaatingiz qabul qilindi!")

def main():
    TOKEN = os.getenv("TOKEN")
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
