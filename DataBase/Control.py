import re
from Tests import ControlException


class Control:
    _type = ''
    _date=''
    _number = None
    _time=''


    def __init__(self, type: str = '', number: int = 1, date: str = '', time: str = ''):
        self.SetType(type=type)
        self.SetNumber(number=number)
        self.SetDate(date=date)
        self.SetTime(time=time)

    def __str__(self) -> str:
        return "Type:" + self._type

    def __eq__(self, other):
        if type(other) != Control:
            return False
        return self._type == other._type

    def SetType(self, type: str):
        try:
            self._type = self._PrepareString(s=type)
        except TypeError:
            raise ControlException(code=1, msg='Bad Type for Title')

    def GetType(self) -> str:
        return self._type

    def SetTime(self,time:str):
        try:
            self._time=self._PrepareString(s=time)
        except TypeError:
            raise ControlException(code=1, msg='Bad Type for Title')

    def GetTime(self) -> str:
        return self._time

    def SetDate(self, date: str):
        try:
            self._date = self._PrepareString(s=date)
        except TypeError:
            raise ControlException(code=1, msg='Bad Type for Title')

    def GetTime(self) -> str:
        return self._time

    def _PrepareString(self, s: str)-> str:
        if type(s) != str:
            raise TypeError()
        return re.sub('[ \t]+', ' ', s).strip().title()

    def SetNumber(self, number: int):
        try:
            self._number = self._PrepareInt(number, 44, 32)
        except TypeError:
            raise ControlException(0, 'Year Have Bad Type')
        except ValueError:
            raise ControlException(10000000000000, 'Year Have Bad Value')

    def GetNumber(self) -> int:
        return self._number

    def _PrepareInt(self, value: int, a: int, b: int) -> int:
        if type(value) != int:
            raise TypeError()
        if value < a or value > b:
            raise ValueError()
        return value