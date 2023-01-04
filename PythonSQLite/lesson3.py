# Команды SELECT и INSERT

# INSERT – добавление записи в таблицу;
# SELECT – выборка данных из таблиц 
# (в том числе и при создании сводной выборки из нескольких таблиц).

# Синтаксис
# INSERT INTO <table_name> (<column_name1>, <column_name2>, ...) VALUES (<value1>, <value2>, …)
# INSERT INTO <table_name> VALUES (<value1>, <value2>, …)

# SELECT col1, col2, … FROM <table_name>
# SELECT col1, col2, … FROM <table_name> WHERE <условие>
# В условии могут быть следующие выражения: = или ==, >, <, >=, <=, !=, BETWEEN

# Составные условия
# AND – условное И: exp1 AND exp2. Истинно, если одновременно истинны exp1 и exp2.
# OR – условное ИЛИ: exp1 OR exp2. Истинно, если истинно exp1 или exp2 или оба выражения.
# NOT – условное НЕ: NOT exp. Преобразует ложное условие в истинное и, наоборот, истинное – в ложное.
# IN – вхождение во множество значений: col IN (val1, val2, …)
# NOT IN – не вхождение во множество значений: col NOT IN (val1, val2, …)

# Сортировка ORDER BY
# SELECT * FROM <table_name> WHERE <условие> ORDER BY <столбец по которому будет сортировка>
# Если в конце запроса указать флаг DESC то сортировка будет выполнена по убыванию
# а если указать флаг ASC то по возрастанию

# Ограничение выборки LIMIT
# В команде SELECT используется еще один оператор – LIMIT, который записывает в самом конце и имеет следующие синтаксисы:
# LIMIT <max> [OFFSET offset]
# LIMIT <offset, max>

import sqlite3 as sq

with sq.connect('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE score > 100 ORDER BY score ASC LIMIT 5")
    # result = cursor.fetchall()
    result = cursor.fetchone()
    result1 = cursor.fetchmany(2)
    print(result)
    print(result1)
    
    # for result in cursor:
    #     print(result)