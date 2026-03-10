import sqlite3

def connect():
    return sqlite3.connect("data/tasks.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()