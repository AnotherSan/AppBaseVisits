import socket
import sqlite3

connection = sqlite3.connect("DataBase/LaterrsAndNot.db")
cursor = connection.cursor()

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()


class MyException(Exception):
    pass


def get_data(description):
    conn.send(description.encode())
    result = conn.recv(2056)
    return result


def try_convert(value):
    try:
        value = int(value)
    except:
        raise MyException("Неверный тип данных")


def add_to_table(table_number):
    values = ()
    if table_number == 1:
        time = get_data("Time\n> ")
        try_convert(time)
        date = get_data("Date\n> ")
        try_convert(date)
        type = get_data("Type\n> ")
        number = get_data("Number\n> ")
        try_convert(number)
        values = (time, date, type, number)
    else:
        number = get_data("Number\n> ")
        try_convert(number)
        first_name = get_data("FirstName\n> ")
        second_name = get_data("SecondName\n> ")
        office = get_data("Office\n> ")
        if len(office.split(' ')) != 2:
            raise MyException("Неверный тип данных")
        try_convert(office.split(' ')[0])
        values = (number, first_name, second_name, office)
    sql = """INSERT OR IGNORE INTO Control (Time, Date, Type, Number)
        VALUES
        (?, ?, ?, ?) """
    if table_number == 2:
        sql = """INSERT OR IGNORE INTO Workers (Number, FirstName, SecondName, Office)
            VALUES
            (?, ?, ?, ?) """
    cursor.execute(sql, values)
    connection.commit()


def delete_from_table(table_number):
    number = get_data("Number\n> ")
    try_convert(number)
    if table_number == 1:
        cursor.execute("""DELETE FROM Control WHERE Number = ?""", [number])
    else:
        cursor.execute("""DELETE FROM Workers WHERE Number = ?""", [number])
    connection.commit()


def find_from_table(table_number):
    number = get_data("Number\n> ")
    try_convert(number)
    row = ()
    if table_number == 1:
        row = cursor.execute("""SELECT * FROM Control WHERE Number = ?""", [number]).fetchone()
    else:
        row = cursor.execute("""SELECT * FROM Workers WHERE Number = ?""", [number]).fetchone()
    print_row(row, table_number)


def print_row(row, table_number):
    if table_number == 1:
        print("Time: " + str(row[0]) + "; Date: " + str(row[1]) + "; Type: " + str(row[2]) + "; Number: " + str(
            row[3]))
    else:
        print("Number: " + str(row[0]) + "; FirstName: " + str(row[1]) + "; SecondName: " + str(
            row[2]) + "; Office: " + str(row[3]))


def display_table(table_number):
    table = ()
    if table_number == 1:
        table = cursor.execute("""SELECT * FROM Control""").fetchall()
    else:
        table = cursor.execute("""SELECT * FROM Workers""").fetchall()
    for index in range(0, len(table)):
        print_row(table[index], table_number)


def update_table(table_number):
    number = get_data("Number\n> ")
    try_convert(number)
    if table_number == 1:
        time = get_data("Time\n> ")
        try_convert(time)
        date = get_data("Date\n> ")
        try_convert(date)
        type = get_data("Type\n> ")
        new_number = get_data("Number\n> ")
        try_convert(new_number)
        sql = """
            UPDATE Control
            SET Time = ?, Date = ?, Type = ?, Number = ?
            WHERE Number = ?
             """
        values = (time, date, type, new_number, number)
        cursor.execute(sql, values)
    else:
        new_number = get_data("Number\n> ")
        try_convert(number)
        first_name = get_data("FirstName\n> ")
        second_name = get_data("SecondName\n> ")
        office = get_data("Office\n> ")
        if len(office.split(' ')) != 2:
            raise MyException("Неверный тип данных")
        try_convert(office.split(' ')[0])
        sql = """
            UPDATE  Workers
            SET Number = ?, FirstName = ?, SecondName = ?, Office = ?
            WHERE Number = ?
            """
        values = (new_number, first_name, second_name, office, number)
        cursor.execute(sql, values)
    connection.commit()


while True:
    conn, addr = sock.accept()
    tableNumber = int(get_data("С какой таблицей работать?\n1 - Control\n2 - Workers\n> "))
    print("DONE")
    actNumber = int(get_data("1 - добавить\n2 - удалить\n3 - изменить\n4 - найти\n5 - вывести всю базу\n> "))
    if actNumber == 1:
        add_to_table(tableNumber)
    if actNumber == 2:
        delete_from_table(tableNumber)
    if actNumber == 3:
        update_table(tableNumber)
    if actNumber == 4:
        find_from_table(tableNumber)
    if actNumber == 5:
        display_table(tableNumber)

conn.close()