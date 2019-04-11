# Installation for rasberry pi controlled telegram bot
# sudo pip install python-telegram-bot==12.0.0b1 --upgrade
# sudo pip install emoji --upgrade
# https://www.webfx.com/tools/emoji-cheat-sheet/

import os
import serial
import io
#Serial interaction  with  Circuit Playground
ser = serial.Serial('/dev/ttyACM0', timeout=1, baudrate=115200)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))


MY_TOKEN ='Insert your Token here'

#Insert questions and answers
questions = []
question1 = ["Mikä vuorovaikutus pitää Kuun Maan kiertoradalla? a) Keskipakoisvoima, b) Painovoima","b"]
question2 = ["Valovuosi on suuri a) etäisyyden yksikkö,  b) ajan yksikö", "a"]
question3 = ["Minkä suureen yksikkö on Newton?", "voima"]

questions.append(question1)
questions.append(question2)
questions.append(question3)

current_question = -1

from telegram.ext import Updater
updater = Updater(token=MY_TOKEN, use_context = True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

from emoji import emojize
cake = emojize("yummy :cake:", use_aliases=True)
thumbsup = emojize(":thumbsup:", use_aliases=True)
disappointed = emojize(":disappointed:", use_aliases=True)
ok_hand = emojize(":ok_hand:", use_aliases=True)

def start(update, context):
    global current_question
    current_question = -1
    context.bot.send_message(chat_id=update.message.chat_id, text="Olen Bottisi! Haluatko läksynkuulustelun (K/E)?")
    ser.write(b'0')

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def reply(update, context):
    global current_question
    if current_question == -1:
        if update.message.text.upper() == 'K':
            context.bot.send_message(chat_id=update.message.chat_id, text='Aloitetaan läksyn kuulustelu!')
            current_question += 1
            context.bot.send_message(chat_id=update.message.chat_id, text=questions[current_question][0])
    
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text=disappointed)
            context.bot.send_message(chat_id=update.message.chat_id, text='Ryhdy sitten opiskelemaan!')
        
        
           
    elif update.message.text.lower() == questions[current_question][1]:
            current_question += 1
            context.bot.send_message(chat_id=update.message.chat_id, text=thumbsup)
            ser.write(b'1')
            if (current_question < 3):
                context.bot.send_message(chat_id=update.message.chat_id, text=questions[current_question][0])
            else:
                context.bot.send_message(chat_id=update.message.chat_id, text='Olet läpäissyt testin!')
                #ser.write(b'2')
                context.bot.send_message(chat_id=update.message.chat_id, text=ok_hand)
                context.bot.send_message(chat_id=update.message.chat_id, text='Aloita testi uudelleen komennolla /start')
                ser.write(b'2')
                #current_question = 0
                
                
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Väärä vastaus!")
        context.bot.send_message(chat_id=update.message.chat_id, text=questions[current_question][0])
        ser.write(b'-1')
            #context.bot.send_message(chat_id=update.message.chat_id, text='YES!')
            #context.bot.send_message(chat_id=update.message.chat_id, text=cake)
    
    #context.bot.send_message(chat_id=update.message.chat_id, text=thumbsup)
    
    #elif update.message.text == thumbsup:
        #context.bot.send_message(chat_id=update.message.chat_id, text='Onnittelut!')
        


from telegram.ext import MessageHandler, Filters
reply_handler = MessageHandler(Filters.text, reply)
dispatcher.add_handler(reply_handler)

updater.start_polling()
