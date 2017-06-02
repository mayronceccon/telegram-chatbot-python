#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def settings(bot, update):
    """
        Configure the messages language using a custom keyboard.
    """
    # Languages message
    msg = "Please, choose a language:\n"
    msg += "en_US - English (US)\n"
    msg += "pt_BR - Português (Brasil)\n"

    # Languages menu
    languages_keyboard = [
        [telegram.KeyboardButton('en_US - English (US)')],
        [telegram.KeyboardButton('pt_BR - Português (Brasil)')]
    ]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(languages_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

    # Sends message with languages menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)


updater = Updater(os.environ['BOT_API_TOKEN'])

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('settings', settings))

updater.start_polling()
updater.idle()