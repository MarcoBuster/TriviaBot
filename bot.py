from config import *
from callback import settings
from api import User

import botogram
import botogram.objects.base
import sqlite3
from json import dumps as j

bot = botogram.create(TOKEN)
conn = sqlite3.connect('users.db')


# noinspection PyClassHasNoInit
class CallbackQuery(botogram.objects.base.BaseObject):
    required = {
        "id": str,
        "from": botogram.User,
        "data": str,
    }
    optional = {
        "inline_message_id": str,
        "message": botogram.Message,
    }
    replace_keys = {
        "from": "sender"
    }


botogram.Update.optional["callback_query"] = CallbackQuery


@bot.command("start")
def start(chat, message):
    user = User(message.sender)
    if not user.exists:
        text = '<b>Welcome, {n}!</b>\nFirst, <b>select a language</b>'.format(n=user.name)
        bot.api.call('sendMessage',
                     dict(chat_id=chat.id,
                          text=text,
                          parse_mode="HTML",
                          reply_markup=j(
                              dict(inline_keyboard=[
                                  [{"text": "🇮🇹 Italian", "callback_data": "l@IT"}]]))))
    else:
        message.reply('Benvenuto! La tua lingua è ' + user.language())


# noinspection PyShadowingNames,PyUnusedLocal,PyUnusedLocal
def process_callback(bot, chains, update):
    settings.process(update)

bot.register_update_processor("callback_query", process_callback)

if __name__ == "__main__":
    bot.run()
