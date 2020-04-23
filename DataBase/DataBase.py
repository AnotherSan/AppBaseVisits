import sqlite3
from DataBase import Worker

class DataBase:
    _db = None
    _cursor = None

    def __init__(self, LaterrsAndNot: str):
        self._db = sqlite3.connect(LaterrsAndNot)
        self._cursor = self._db.cursor()

    def AddWorker(self, worker: Worker):
        query = "Insert Into Workers (FirstName, SecondName, Office)" \
                "Values (?, ?, ?)"
        self._cursor.execute(query, [Worker.GetFirstName(), Worker.GetSecondName(),
                                     Worker.GetOffice(), ''])
        self._db.commit()

    def GetAllWorker(self) -> list:
        self._cursor.execute("Select * From Worker")
        ls = []
        for row in self._cursor.fetchall():
            worker = Worker(firstName=row[1], secondName=row[2],
                            office=row[3])
            ls.append(Worker)
        return ls

    def SimpleFilter(self, field: str, value: str) -> Worker:
        query = "Select FirstName, SecondName, Office From Worker " \
                "Where " + field + " = '" + value + "'"
        self._cursor.execute(query)
        row = self._cursor.fetchone()
        if row is None:
            raise Exception()
        worker = Worker(firstName=row[0], secondName=row[1], office=row[2])
        return worker