'''
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
'''

import logging
import requests
import json
import time
from CosmoCorps.Price import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

f =  open('temp.json', 'r')
months: dict = json.load(f)
order_months = list(months.keys())
current = order_months[2]

print(order_months)
print(months)

element_obj: elements = elements()
id_list = []

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(x, update):
    """Send a message when the command /start is issued."""
    id_list.append(update.message.chat.id)
    name = str(update.message.chat.first_name)
    text = "Holla {}, welcome to Corporates of the Cosmos. \n\n" \
           "You'll recieve price updates for all elements, compounds and companies on this handle.\n\n" \
           "Gear up for your Celestial Business Trip ;)".format(name)
    update.message.reply_text(text)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(x, update):
    try:
        """Echo the user message."""
        text = "Invalid Response, Please Try Again"
        input = str(update.message.text)
        if input[1] == " ":
            pop, val = input.split(" ")
            try:
                pop = int(pop)
                val = int(val)
                name = str(update.message.chat.first_name)
                text = "POP: {}\n\nQTY: {}\n\nThankyou {}, recorded successfully :)".format(pop, val, name)
            except:
                pass
        update.message.reply_text(text)
    except:
        pass


def error(context, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def trig(x, update):
    print('activated')
    global current, months, element_obj
    month = months[current]
    text = current + '\n\n\n'
    for each in month.values():
        for inx, ch in each.items():
            element_obj.incur_change(inx, ch)
    text += element_obj.get_formatted_price()
    telepost(text)
    current = order_months[order_months.index(current) + 1]

def telepost(message='test', ids=id_list):
    for each in ids:
        url = "https://api.telegram.org/bot917438859:AAGgn74dJ06LIpmP3d7WhECn8ss8XNJQIRE/sendMessage?chat_id={}&text={}".format(
            each, message)
        requests.post(url)
        time.sleep(0.04)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("917438859:AAGgn74dJ06LIpmP3d7WhECn8ss8XNJQIRE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("trig", trig))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()