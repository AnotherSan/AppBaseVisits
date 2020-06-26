import sqlite3
from sqlite3 import Error
#Тест создания соединения с DB
def create_connection(path):
    try:
        connection = sqlite3.connect(path)
        return ("0")
    except Error:
        return ("1")
#Тесты создания таблицы
def create_TableW(path):
    try:
        connection=sqlite3.connect(path)
        c = connection.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS Workers(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,branch TEXT,sem INTEGER,mobile INTEGER,address TEXT)")
        connection.commit()
        c.close()
        connection.close()
        return ("0")
    except Error:
        return ("1")

def create_TableL(path):
    try:
        connection=sqlite3.connect(path)
        c = connection.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS Late(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,count INTEGER)")
        connection.commit()
        c.close()
        connection.close()
        return ("0")
    except Error:
        return ("1")
#Тесты проверки функции поиска
def check_Select(path, query):
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        return ("0")
    except Error:
        return ("1")



