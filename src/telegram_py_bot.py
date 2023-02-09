from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from qr_code_generator import QR

async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the QR generator bot!\nSend /help to see the usage")

async def help(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Usage:\nwrite the string you want to convert into a QR code image")

async def qr(update, context):
    QR(update.message.text)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('url_qrcode.png', 'rb'))

if __name__ == '__main__':
    with open("bot_token.txt", "r", encoding="utf8") as token:
        bot = ApplicationBuilder().token(token.readline()).build()

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), qr)

    bot.add_handler(CommandHandler('start', start))
    bot.add_handler(CommandHandler('help', help))
    bot.add_handler(message_handler)

    bot.run_polling()