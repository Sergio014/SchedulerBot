import sqlite3

conn = sqlite3.connect('tasks.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        telegram_id INTEGER PRIMARY KEY,
        username TEXT
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY,
        description TEXT,
        user_id INTEGER,
        hour INTEGER NULL,
        minute INTEGER NULL,
        FOREIGN KEY(user_id) REFERENCES users(telegram_id)
    );
''')


# Commit the changes and close the connection
conn.commit()
conn.close()
