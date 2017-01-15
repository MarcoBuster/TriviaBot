import sqlite3
from languages import it

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY NOT NULL, state STRING, language STRING)')


class User:
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    def __init__(self, user, language=None, state='home'):
        self.id = user.id
        self.name = user.name
        self.username = user.username
        if language is None:
            c.execute('INSERT OR IGNORE INTO users VALUES(?, ?, ?)', (self.id, state, language,))
            c.execute('UPDATE OR IGNORE users SET state=? WHERE id=?', (state, self.id,))
            conn.commit()
            return

        c.execute('INSERT OR IGNORE INTO users VALUES(?, ?, ?)', (self.id, state, language,))
        c.execute('UPDATE OR IGNORE users SET language=?, state=? WHERE id=?', (language, state, self.id,))
        conn.commit()

    @property
    def exists(self):
        c.execute('SELECT language FROM users WHERE id=?', (self.id,))
        row = c.fetchone()
        if not row or row[0] is None:
            return False
        else:
            return True

    def language(self, new_language=None):
        if new_language is None:
            c.execute('SELECT language FROM users WHERE id=?', (self.id,))
            row = c.fetchone()
            if not row:
                return False
            else:
                return row[0]
        else:
            c.execute('UPDATE OR IGNORE users SET language=? WHERE id=?', (new_language, self.id))
            conn.commit()

    def state(self, new_state=None):
        if new_state is None:
            c.execute('SELECT state FROM users WHERE id=?', (self.id,))
            row = c.fetchone()
            if not row:
                return False
            else:
                return row[0]
        else:
            c.execute('UPDATE OR IGNORE users SET state=? WHERE id=?', (new_state, self.id))
            conn.commit()

    def getstr(self, str_code):
        lang = self.language()
        if lang == 'IT':
            return it.get(str_code)


class Callback:
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    def __init__(self, update):
        self.update = update.callback_query
        self.id = self.update.id
        self.query = self.update.data
        self.sender = self.update.sender
        self.message = self.update.message
        self.chat = self.message.chat

        if self.chat is None:
            self.isInline = True
        else:
            self.isInline = False
