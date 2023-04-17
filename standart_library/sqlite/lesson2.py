# Подключение к БД, создание и удаление таблиц

import sqlite3 as sq

# Рекомендуемые расширения для баз данных:
# *.db, *.db3, *.sqlite, *.sqlite3
# Список типов полей:
# NULL – значение NULL;
# INTEGER – целочисленный тип (занимает от 1 до 8 байт);
# REAL – вещественный тип (8 байт в формате IEEE);
# TEXT – строковый тип (в кодировке данных базы, обычно UTF-8);
# BLOB (двоичные данные, хранятся «как есть», например, для небольших изображений).

# Первый способ работы с базой данных (рекомендуется)
with sq.connect('data.db') as connection:
    cursor = connection.cursor() # Cursor object
    # Удаление таблицы
    cursor.execute("""DROP TABLE IF EXISTS users""")
    # Создание таблицы
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        age INTEGER,
        score INTEGER
        )""")
    

# Второй способ работы с базой данных (не рекомендуется)
# connection = sq.connect('first_base.db') # Connection object
# cursor = connection.cursor() # Cursor object
# cursor.execute("")
# connection.close()