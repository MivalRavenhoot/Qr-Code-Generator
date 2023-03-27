# QR Code Generator Telegram Bot

This is a Python Telegram Bot that allows users to generate QR codes for any given text string. The bot uses the Telegram Bot API and the qrcode library to generate QR codes in PNG format.

## Usage
To use the bot, simply start a chat with it on Telegram and follow the steps below:

- Send the ``` /start ``` command to the bot to receive a welcome message and instructions.
- Send the ``` /help ``` command to the bot to receive instructions on how to use the bot.
- Type the text you want to convert into a QR code and send it to the bot. The bot will generate a QR code and send it back to you as a PNG image, along with the original text you requested.

## Installation
To run this bot on your local machine, you will need to have Python 3 installed along with the following libraries:

1) ```telegram```
2) ```qrcode```

To install these libraries, you can use pip:

Copy code
```pip install telegram``` and ```pip install qrcode``` .
You will also need to create a file named ``` bot_token.txt ``` in the same directory as the code, containing your Telegram Bot API token.

## Code
The code is written in Python 3 and uses the telegram and qrcode libraries to generate QR codes and communicate with the Telegram Bot API. The code consists of four functions:

- QR(text): This function generates a QR code image in PNG format for the given text string using the qrcode library.
- start(update, context): This function sends a welcome message to the user when they send the /start command to the bot.
- help(update, context): This function sends instructions to the user when they send the /help command to the bot.
- qr_generator(update, context): This function generates a QR code image for the text string sent by the user, sends a message with the original text string, and sends the QR code image as a PNG file to the user.

The code uses the ```ApplicationBuilder``` class from the ```telegram.ext``` library to create a Telegram bot object with the given API token, and then adds three handlers to the bot object:

CommandHandler('start', start): This handler listens for the /start command and executes the start function when it is received.
CommandHandler('help', help): This handler listens for the /help command and executes the help function when it is received.
MessageHandler(filters.TEXT & (~filters.COMMAND), qr_generator): This handler listens for any text message that is not a command and executes the qr_generator function when it is received.
The bot is then set to run in polling mode using the run_polling() method.
