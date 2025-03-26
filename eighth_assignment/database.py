import sqlite3

class Database:
    def setup_database(self):
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            position TEXT,
            salary REAL,
            hire_date TEXT
                       )
        ''')

        conn.commit()
        conn.close()