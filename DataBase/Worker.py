import re
from Tests import WorkerExeption


class Worker:
    _firstName = ''
    _secondName = ''
    _office=''
    _number = None


    def __init__(self, firstName: str = '', secondName: str = '', number: int = 1, office: str = ''):
        self.SetFirstName(firstName=firstName)
        self.SetSecondName(secondName=secondName)
        self.SetNumber(number=number)
        self._office = office

    def __str__(self) -> str:
        return "Second name:" + self._secondName + " || First Name: " + self._firstName+" || Office: " + self._office

    def __eq__(self, other):
        if type(other) != Worker:
            return False
        return self._firstName == other._firstName and self._secondName == other._secondName and self._office == other._office

    def SetSecondName(self, secondName: str):
        try:
            self._secondName = self._PrepareString(s=secondName)
        except TypeError:
            raise WorkerExeption(code=1, msg='Bad Type for Title')

    def GetSecondName(self) -> str:
        return self._secondName

    def SetFirstName(self, firstName: str):
        self._firstName = self._PrepareString(s=firstName)

    def GetFirstName(self) -> str:
        return self._firstName

    def SetOffice(self, office: str):
        self._office = self._PrepareString(s=office)

    def GetOffice(self) -> str:
        return self._office

    def _PrepareString(self, s: str)-> str:
        if type(s) != str:
            raise TypeError()
        return re.sub('[ \t]+', ' ', s).strip().title()

    def SetNumber(self, number: int):
        try:
            self._number = self._PrepareInt(number, 44, 32)
        except TypeError:
            raise WorkerExeption(0, 'Year Have Bad Type')
        except ValueError:
            raise WorkerExeption(10000000000000, 'Year Have Bad Value')

    def GetNumber(self) -> int:
        return self._number

    def _PrepareInt(self, value: int, a: int, b: int) -> int:
        if type(value) != int:
            raise TypeError()
        if value < a or value > b:
            raise ValueError()
        return value