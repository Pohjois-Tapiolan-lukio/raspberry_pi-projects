# Installation for rasberry pi controlled telegram bot
# sudo pip install python-telegram-bot==12.0.0b1 --upgrade
# sudo pip install emoji --upgrade

MY_TOKEN ='ISERT YOUR TOKEN'


from telegram.ext import Updater
updater = Updater(token=MY_TOKEN, use_context = True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

from emoji import emojize
cake = emojize("yummy :cake:", use_aliases=True)
thumbsup = emojize(":thumbsup:", use_aliases=True)

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
        context.bot.send_message(chat_id=update.message.chat_id, text=cake)
        context.bot.send_message(chat_id=update.message.chat_id, text=thumbsup)
    elif update.message.text == thumbsup:
        context.bot.send_message(chat_id=update.message.chat_id, text='OK')
        


from telegram.ext import MessageHandler, Filters
reply_handler = MessageHandler(Filters.text, reply)
dispatcher.add_handler(reply_handler)

updater.start_polling()
