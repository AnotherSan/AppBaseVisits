from PyQt5.QtWidgets import *
import sqlite3
#Вкладки таблицы
class Tabs(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.addTab(self.tab1, "Посещения")
        self.tabs.addTab(self.tab2, "Опоздания")
        self.tabs.addTab(self.tab3, "Правила")
        self.tabs.addTab(self.tab4, "Начальство")
        self.tabs.addTab(self.tab5, "Контакты")

        self.getTab1()
        self.getTab2()
        self.getTab3()
        self.getTab4()
        self.getTab5()

    def getTab1(self):
        self.tab1.layout = QVBoxLayout(self)
        self.tableWidget = QTableWidget()
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("№", "Имя", "Отдел", "Время", "Номер", "Адрес"))
        self.tab1.layout.addWidget(self.tableWidget)
        self.tab1.setLayout(self.tab1.layout)

    def getTab2(self):
        self.tab2.layout = QVBoxLayout(self)
        self.tableWidget1 = QTableWidget()
        self.tableWidget1.setAlternatingRowColors(True)
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget1.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget1.horizontalHeader().setStretchLastSection(True)
        self.tableWidget1.verticalHeader().setVisible(False)
        self.tableWidget1.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget1.verticalHeader().setStretchLastSection(False)
        self.tableWidget1.setHorizontalHeaderLabels(("№", "Имя", "Колличество"))
        self.tab2.layout.addWidget(self.tableWidget1)
        self.tab2.setLayout(self.tab2.layout)

    def getTab3(self):
        self.tab3.layout = QVBoxLayout(self)
        self.tableWidget2 = QTableWidget()
        self.tableWidget2.setAlternatingRowColors(True)
        self.tableWidget2.setColumnCount(2)
        self.tableWidget2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget2.verticalHeader().setVisible(False)
        self.tableWidget2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget2.verticalHeader().setStretchLastSection(False)
        self.tableWidget2.setHorizontalHeaderLabels(("Начало смены", "Конец смены"))
        self.connection = sqlite3.connect("database.db")
        query = "SELECT * FROM Rulls"
        result = self.connection.execute(query)
        for row_number, row_data in enumerate(result):
            self.tableWidget2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget2.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()
        self.tab3.layout.addWidget(self.tableWidget2)
        self.tab3.setLayout(self.tab3.layout)

    def getTab4(self):
        self.tab4.layout = QVBoxLayout(self)
        self.tableWidget3 = QTableWidget()
        self.tableWidget3.setAlternatingRowColors(True)
        self.tableWidget3.setColumnCount(2)
        self.tableWidget3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget3.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget3.verticalHeader().setVisible(False)
        self.tableWidget3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget3.verticalHeader().setStretchLastSection(False)
        self.tableWidget3.setHorizontalHeaderLabels(("Имя", "Кабинет"))
        self.connection = sqlite3.connect("database.db")
        query = "SELECT * FROM Boss"
        result = self.connection.execute(query)
        for row_number, row_data in enumerate(result):
            self.tableWidget3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget3.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()
        self.tab4.layout.addWidget(self.tableWidget3)
        self.tab4.setLayout(self.tab4.layout)

    def getTab5(self):
        self.tab5.layout = QVBoxLayout(self)
        self.tableWidget4 = QTableWidget()
        self.tableWidget4.setAlternatingRowColors(True)
        self.tableWidget4.setColumnCount(4)
        self.tableWidget4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget4.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget4.verticalHeader().setVisible(False)
        self.tableWidget4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget4.verticalHeader().setStretchLastSection(False)
        self.tableWidget4.setHorizontalHeaderLabels(("Название", "Телефон", "Email", "Адрес"))
        self.connection = sqlite3.connect("database.db")
        query = "SELECT * FROM Contacts"
        result = self.connection.execute(query)
        for row_number, row_data in enumerate(result):
            self.tableWidget4.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget4.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()
        self.tab5.layout.addWidget(self.tableWidget4)
        self.tab5.setLayout(self.tab5.layout)
        self.tabs.setGeometry(0, 35, 880, 650)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

