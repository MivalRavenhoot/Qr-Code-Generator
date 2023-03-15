from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import qrcode

# Qrcode generation function in png format
def QR(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("url_qrcode.png")

#bot telegram basic commands
async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the QR generator bot!\nSend /help to see the usage")

async def help(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Usage:\nwrite the string you want to convert into a QR code image")

async def qr_generator(update, context):
    QR(update.message.text)
    with open('url_qrcode.png', 'rb') as qr_image:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=qr_image)

#telegram bot start and token validation
if __name__ == '__main__':
    with open("bot_token.txt", "r", encoding="utf8") as token:
        bot = ApplicationBuilder().token(token.readline()).build()

#User message management and command recognition
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), qr_generator)

    bot.add_handler(CommandHandler('start', start))
    bot.add_handler(CommandHandler('help', help))
    bot.add_handler(message_handler)

    bot.run_polling()
