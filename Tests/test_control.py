from unittest import TestCase
from Tests import ControlException
from DataBase import Control


class TestControl(TestCase):
    def test_SetTime(self):
        control = Control(time='21:07', date='2020.01.03')
        self.assertRaises(ControlException, control.SetTime, ('-1'))
        self.assertRaises(ControlException, control.SetTime, ('25:04'))

    def test_SetDate(self):
        control = Control(time='08:15', date='2001.05.02')
        self.assertRaises(ControlException, control.SetDate, ('1985.23.87'))
        self.assertRaises(ControlException, control.SetDate, ('0.0.0'))
        self.assertRaises(ControlException, control.SetDate, ('3000.98.21'))
        self.assertRaises(ControlException, control.SetDate, ('-1'))
        self.assertRaises(ControlException, control.SetDate, ('0'))

    def test_GetTime(self):
        control = Control(time='08:15', date='3000.04.23')
        self.assertEqual('08:15', control.GetTime())

    def test_GetDate(self):
        control = Control(time='25:06', date='2019.03.15')
        self.assertEqual('', control.GetDate())