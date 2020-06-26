import unittest
from Tests import TestConection
path='C:/Users/Человек/PycharmProjects/WorkersDataBase/database.db'
class MyTestCase(unittest.TestCase):
    def test_conection(self):
        self.assertEqual(TestConection.create_connection(path),"0")
        self.assertEqual(TestConection.create_connection('C:/Users/Человек/PycharmProjects/WorkersDataBase'),"1")
        self.assertEqual(TestConection.create_connection(" "), "1")
        self.assertEqual(TestConection.create_TableW(path),"0")
        self.assertEqual(TestConection.create_TableL(path),"0")
        self.assertEqual(TestConection.check_Select(path,"SELECT * from Workers"),"0")
        self.assertEqual(TestConection.check_Select(path, "SELECT * from Worker"), "1")
        self.assertEqual(TestConection.check_Select(path, "SELECT * from Late"), "0")

if __name__ == '__main__':
    unittest.main()
