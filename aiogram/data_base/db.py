import sqlite3

class DataBase:
    def __init__(self, db_name='base.db'):
        self.__connection = sqlite3.connect(db_name)
        self.__cursor = self.__connection.cursor()
        print('Data base connected succesfuly')
    
    def create_db(self):
        """Вспомогательная функция для создания таблиц БД"""
        sq = """CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)"""
        self.__connection.cursor().execute(sq)
        # Вызываем метод commit, чтобы изменения применились к текущей БД
        self.__connection.commit()
        # Закрывам установленное соединение.
        self.__connection.close()

    async def add_product(self, state):
        async with state.proxy() as data:
            try:
                self.__cursor.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
                self.__connection.commit()
            except sqlite3.Error as e:
                print("Ошибка записи в БД "+str(e))
            
    def get_products(self):
        try:
            self.__cursor.execute('SELECT * FROM menu')
            res = self.__cursor.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print("Ошибка получения записей из БД "+str(e))
        return []
    
    def delete_product(self, product_name):
        try:
            self.__cursor.execute(f'DELETE FROM menu WHERE name="{product_name}"')
            self.__connection.commit()
        except sqlite3.Error as e:
            print("Ошибка удаления записи из БД "+str(e))
    
    def close_db(self):
        self.__connection.close
        print('Data base closed')
