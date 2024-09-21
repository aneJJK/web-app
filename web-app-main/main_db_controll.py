import sqlite3

class DB_Controller:
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self, db_name) -> None:
        self.db_name = db_name
    
    def open(self):
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    
    def init_table(self):
        self.open()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS ticket (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            by TEXT, name TEXT, date TEXT, city TEXT, class TEXT, adult TEXT, children TEXT)''')
        self.close()

    def get_data(self):
        self.open()
        self.cursor.execute(
            '''SELECT * FROM ticket'''
            )
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def add_data(self, data):
        print(data)
        self.open()
        self.cursor.execute('''INSERT INTO ticket (by, name, date, city, class, adult, children) VALUES (?, ?, ?, ?, ?, ?, ?)''', data)
        self.conn.commit()
        self.close()

    def close(self):
        self.cursor.close()
        self.conn.close()

db = DB_Controller('question.db')
db.init_table()