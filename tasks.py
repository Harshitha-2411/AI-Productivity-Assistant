import sqlite3

def connect():
    return sqlite3.connect("tasks.db", check_same_thread=False)

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

def add_task(task):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(task,status) VALUES(?,?)",
        (task,"pending")
    )

    conn.commit()
    conn.close()

def get_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    conn.close()

    return rows

def complete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status='completed' WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()

create_table()