import sqlite3 as sq

with sq.connect('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_clone (
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        age INTEGER,
        score INTEGER
        )""")
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for name, sex, age, score in result:
        cursor.execute(f"INSERT INTO users_clone VALUES ('{name}', {sex}, {age}, {score})")
        