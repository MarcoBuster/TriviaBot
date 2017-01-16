from bot import bot
from json import dumps as j


class Question:
    def __init__(self, question_id):
        self.question_id = question_id

    def get_question(self, user):
        return user.getstr("q" + str(self.question_id))

    def get_answers(self, user):
        return (
            user.getstr("q" + str(self.question_id) + "a1"),
            user.getstr("q" + str(self.question_id) + "a2"),
            user.getstr("q" + str(self.question_id) + "a3"),
            user.getstr("q" + str(self.question_id) + "a4")
        )


class Game:
    def __init__(self, chat, user):
        self.chat = chat
        self.user = user

    def send(self, question=None):
        if question is None:
            self.message_id = bot.api.call('sendMessage', dict(
                chat_id=self.chat.id,
                text="",
                parse_mode="HTML",
                reply_markup=j(
                    dict(inline_keyboard=[
                        [{"text": "WIP", "callback_data": "WIP"}]])))).message_id
        else:
            answers = question.get_answers(self.user)

            bot.api.call('editMessageText', dict(
                chat_id=self.chat.id,
                message_id=self.message_id,
                text="",
                parse_mode="HTML",
                reply_markup=j(
                    dict(inline_keyboard=[
                        [{"text": answers[0], "callback_data": "a@0"}, {"text": answers[1], "callback_data": "a@1"}],
                        [{"text": answers[2], "callback_data": "a@2"}, {"text": answers[3], "callback_data": "a@3"}]
                    ]))))
