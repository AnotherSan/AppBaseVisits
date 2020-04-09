import sqlite3
import sys
from PyQt5 import QtWidgets
import App

connection = sqlite3.connect("LaterrsAndNot.db")
cursor = connection.cursor()

class BaseApp(QtWidgets.QMainWindow, App.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле App.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BaseApp()
    window.show()
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

    def addToTable(tableNumber):
        values = ()
        if tableNumber == 1:
            time = input("Time\n> ")
            tryConvert(time)
            date = input("Date\n> ")
            tryConvert(date)
            type = input("Type\n> ")
            number = input("Number\n> ")
            tryConvert(number)
            values = (time, date, type, number)
        else:
            number = input("Number\n> ")
            tryConvert(number)
            firstName = input("FirstName\n> ")
            secondName = input("SecondName\n> ")
            office =  input("Office\n> ")
            if len(office.split(' ')) != 2:
                raise MyException("Неверный тип данных")
            tryConvert(office.split(' ')[0])
            values = (number, firstName, secondName, office)
        sql = """INSERT OR IGNORE INTO Control (Time, Date, Type, Number)
            VALUES
            (?, ?, ?, ?) """
        if tableNumber == 2:
            sql = """INSERT OR IGNORE INTO Workers (Number, FirstName, SecondName, Office)
                VALUES
                (?, ?, ?, ?) """
        cursor.execute(sql, values)
        connection.commit()


    def tryConvert(value):
        try:
            value = int(value)
        except:
            raise MyException("Неверный тип данных")


    def deleteFromTable(tableNumber):
        number = input("Number\n> ")
        tryConvert(number)
        if tableNumber == 1:
            cursor.execute("""DELETE FROM Control WHERE Number = ?""", [number])
        else:
            cursor.execute("""DELETE FROM Workers WHERE Number = ?""", [number])
        connection.commit()


    def findFromTable(tableNumber):
        number = input("Number\n> ")
        tryConvert(number)
        row = ()
        if tableNumber == 1:
            row = cursor.execute("""SELECT * FROM Control WHERE Number = ?""", [number]).fetchone()
        else:
            row = cursor.execute("""SELECT * FROM Workers WHERE Number = ?""", [number]).fetchone()
        printRow(row, tableNumber)


    def printRow(row, tableNumber):
        if tableNumber == 1:
            print("Time: " + str(row[0]) + "; Date: " + str(row[1]) + "; Type: " + str(row[2]) + "; Number: " + str(row[3]))
        else:
            print("Number: " + str(row[0]) + "; FirstName: " + str(row[1]) + "; SecondName: " + str(row[2]) + "; Office: " + str(row[3]))


    def displayTable(tableNumber):
        table = ()
        if tableNumber == 1:
            table = cursor.execute("""SELECT * FROM Control""").fetchall()
        else:
            table = cursor.execute("""SELECT * FROM Workers""").fetchall()
        for index in range(0, len(table)):
            printRow(table[index], tableNumber)


    def updateTable(tableNumber):
        number = input("Number\n> ")
        tryConvert(number)
        if tableNumber == 1:
            time = input("Time\n> ")
            tryConvert(time)
            date = input("Date\n> ")
            tryConvert(date)
            type = input("Type\n> ")
            newNumber = input("Number\n> ")
            tryConvert(newNumber)
            sql = """
                UPDATE Control
                SET Time = ?, Date = ?, Type = ?, Number = ?
                WHERE Number = ?
                 """
            values = (time, date, type, newNumber, number)
            cursor.execute(sql, values)
        else:
            newNumber = input("Number\n> ")
            tryConvert(number)
            firstName = input("FirstName\n> ")
            secondName = input("SecondName\n> ")
            office =  input("Office\n> ")
            if len(office.split(' ')) != 2:
                raise MyException("Неверный тип данных")
            tryConvert(office.split(' ')[0])
            sql = """
                UPDATE  Workers
                SET Number = ?, FirstName = ?, SecondName = ?, Office = ?
                WHERE Number = ?
                """
            values = (newNumber, firstName, secondName, office, number)
            cursor.execute(sql, values)
        connection.commit()


    while True:
        tableNumber = int(input("С какой таблицей работать?\n1 - Control\n2 - Workers\n> "))
        actNumber = int(input("1 - добавить\n2 - удалить\n3 - изменить\n4 - найти\n5 - вывести всю базу\n> "))
        if actNumber == 1:
            addToTable(tableNumber)
        if actNumber == 2:
            deleteFromTable(tableNumber)
        if actNumber == 3:
            updateTable(tableNumber)
        if actNumber == 4:
            findFromTable(tableNumber)
        if actNumber == 5:
            displayTable(tableNumber)
    cursor.close()
    class MyException(Exception):
        pass