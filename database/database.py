import sqlite3


class Database:
    def __init__(self):
        self.database = sqlite3.connect('translate.db', check_same_thread=False)

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False):
        with self.database as db:
            cursor = db.cursor()
            cursor.execute(sql, args)
            if commit:
                result = db.commit()
            if fetchone:
                result = cursor.fetchone()
            if fetchall:
                result = cursor.fetchall()
            return result

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS history(
        history_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        src TEXT,
        dest TEXT,
        original_text TEXT,
        translated_text TEXT
        )'''
        self.manager(sql, commit=True)

    def save_data(self, user_id, src, dest, original_text, translated_text):
        sql = '''
        INSERT INTO history(user_id, src, dest, original_text, translated_text)
        VALUES(?, ?, ?, ?, ?)'''
        self.manager(sql, user_id, src, dest, original_text, translated_text, commit=True)

    def select_data(self, user_id):
        sql = '''
        SELECT user_id, src, dest, original_text, translated_text FROM history WHERE name = (?);
        '''
        self.manager(sql, user_id, fetchall=True, commit=True)
