#Installation:
# sudo pip install python-telegram-bot==12.0.0b1 --upgrade
#Example script for Telegram bot
MY_TOKEN ='insert your telegram token!'


from telegram.ext import Updater
updater = Updater(token=MY_TOKEN, use_context = True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
   context.bot.send_message(chat_id=update.message.chat_id, text="Olen Bottisi!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

'''
def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
'''

def reply(update, context):
    if update.message.text == 'K':
        context.bot.send_message(chat_id=update.message.chat_id, text='YES!')

from telegram.ext import MessageHandler, Filters
reply_handler = MessageHandler(Filters.text, reply)
dispatcher.add_handler(reply_handler)

updater.start_polling()
