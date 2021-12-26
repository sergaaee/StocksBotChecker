import sqlite3
from config import database_path


class DB:
    def __init__(self):
        self.con = sqlite3.connect(database=database_path)
        self.cur = self.con.cursor()


