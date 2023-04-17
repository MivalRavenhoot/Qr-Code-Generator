from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from QR import QR

# telegram bot start command handler
async def start(update, context) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the QR generator bot!\nSend /help to see the usage")

# telegram bot help command handler
async def help(update, context) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Usage:\nwrite the string you want to convert into a QR code image")

# telegram bot user string printer
async def printing(update, context, text) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'You requested the following string: "{text}"\n\nThis is the generated QR code image:')

# telegram bot qr code image sender function
async def qr_generator(update, context) -> None:
    QR(update.message.text)
    await printing(update, context, update.message.text)

    with open('qrcode.png', 'rb') as qr_image:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=qr_image)

# telegram bot start and token validation
if __name__ == '__main__':
    with open("bot_token.txt", "r", encoding="utf8") as token:
        bot = ApplicationBuilder().token(token.readline()).build()

# user messages management and command recognition
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), qr_generator)

    bot.add_handler(CommandHandler('start', start))
    bot.add_handler(CommandHandler('help', help))
    bot.add_handler(message_handler)
    bot.run_polling()
