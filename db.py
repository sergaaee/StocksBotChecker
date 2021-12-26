import datetime
import sqlite3
from config import database_path


class DB:
    def __init__(self):
        self.con = sqlite3.connect(database=database_path)
        self.cur = self.con.cursor()

    def close(self):
        self.con.close()


class User:
    def __init__(self, user_id: int, date: datetime.datetime):
        self._user_id = user_id
        self._date = date

    def add_table(self):
        table = 'users'
        q = f'''insert into {table} (user_id, date)  values({self._user_id, self._date})'''
        db = DB()
        db.cur.execute()

