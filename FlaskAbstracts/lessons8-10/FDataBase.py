import sqlite3
from math import floor as m_floor
from time import time

class FDataBase:
    def __init__(self, db: sqlite3.Connection):
        self.__db = db
        self.__cur = db.cursor()
        
    
    def getMenu(self):
        sq = """SELECT *  FROM mainmenu"""
        try:
            self.__cur.execute(sq)
            result = self.__cur.fetchall()
            if result: return result
        except:
            print('Ошибка чтения из БД')
        return []
    
    
    def addPost(self, title, text):
        try:
            tm = m_floor(time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД "+str(e))
            return False
        return True
    
    
    def getPost(self, post_id):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE id = {post_id} LIMIT 1")
            result = self.__cur.fetchone()
            if result:
                return result
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД "+str(e))
        return (False, False)
    
    
    def getPostsAnonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, text FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД "+str(e))

        return []