import sqlite3
import random
import string

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS questions(id INTEGER PRIMARY KEY NOT NULL, '
          'question TEXT, answers TEXT, correct TEXT)')


class Game:
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    def __init__(self, chat, user, message):
        self.chat = chat
        self.message = message
        self.user = user

        self.id = ''.join(random.choice(string.digits) for _ in range(8))

        c.execute('SELECT * FROM questions WHERE id=?', (self.id,))
        row = c.fetchone()
        self.question = row[0]
        self.answers = list(row[1])
        self.correct = row[2]
