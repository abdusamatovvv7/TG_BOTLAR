import sqlite3

class Work_Database:
    def __init__(self, database):
        self.database = database #ombor.db
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()




    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE user (
            telegram_id INTEGER,
            username,
            fullname

        )
        """)    


    def insert_user(self, telegram_id, username, fullname):
        self.cursor.execute(f"""
        INSERT INTO users
        VALUES (?, ?, ?)""", (telegram_id, username, fullname))
        self.connection.commit()    