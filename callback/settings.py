from api import *
from bot import bot


def process(update):
    callback = Callback(update)
    user = User(callback.sender)

    if callback.isInline:
        return

    if 'l@' in callback.query:
        user.language(callback.query.replace('l@', ''))
        bot.api.call('editMessageText',
                     dict(chat_id=callback.chat.id,
                          message_id=callback.message.message_id,
                          text=user.getstr('start')))
