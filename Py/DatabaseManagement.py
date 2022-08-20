from socket import create_connection
import sqlite3
import Debug.Debug as Debug
from sqlite3 import Error

class database:

    def __init__(self):
        db_file = r"./database.db"
        self.conn = sqlite3.connect(db_file)

        self.timeTable = """CREATE TABLE IF NOT EXISTS time(
            id integer PRIMARY KEY,
            name text NOT NULL,
            date text NOT NULL,
            savedTime text NOT NULL
        );
        """

    def create_table(self):
        try:
            c= self.conn.cursor()
            c.execute(self.timeTable)
        except Error as e:
            print(e)

    def insert_time(self, name, date, savedTime):
        sql = '''INSERT INTO time(name, date, savedTime)
                 VALUES(?,?,?) '''
        cur = self.conn.cursor()
        time = (name, date, savedTime)
        cur.execute(sql,time)
        self.conn.commit()
        return cur.lastrowid