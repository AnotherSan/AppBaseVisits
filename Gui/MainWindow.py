from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
from Functions import GuiSignal
from Gui import GuiTab
#Gui основного окна
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS Workers(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,branch TEXT,sem INTEGER,mobile INTEGER,address TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS Late(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,count INTEGER)")
        self.c.close()
        self.setWindowIcon(QIcon("icon/document.png"))
        self.setWindowTitle("Контроль посещений")
        self.setMinimumSize(900, 700)
        self.table_widget= GuiTab.Tabs(self)
        self.setCentralWidget(self.table_widget)
        self.table_widget.show()
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
#Панель кнопок
        btn_ac_adduser = QAction(QIcon("icon/add.png"), "Добавить", self)
        btn_ac_adduser.triggered.connect(lambda: GuiSignal.insert(self.table_widget.tabs.currentIndex()))
        btn_ac_adduser.setStatusTip("Добавить")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon("icon/refresh.png"),"Обновить",self)
        btn_ac_refresh.triggered.connect(lambda: self.loaddata(self.table_widget.tabs.currentIndex()))
        btn_ac_refresh.setStatusTip("Обновить")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/search.png"), "Поиск", self)
        btn_ac_search.triggered.connect(lambda: GuiSignal.search(self.table_widget.tabs.currentIndex()))
        btn_ac_search.setStatusTip("Поиск")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("icon/trash.png"), "Удалить", self)
        btn_ac_delete.triggered.connect(lambda: GuiSignal.delete(self.table_widget.tabs.currentIndex()))
        btn_ac_delete.setStatusTip("Удалить")
        toolbar.addAction(btn_ac_delete)

        btn_ac_update = QAction(QIcon("icon/update.png"), "Редактировать", self)
        btn_ac_update.triggered.connect(lambda: GuiSignal.updateTable(self.table_widget.tabs.currentIndex()))
        btn_ac_update.setStatusTip("Редактировать")
        toolbar.addAction(btn_ac_update)
#Подгрузка данных с таблицы
    def loaddata(self, index):
        if index == 0:
            self.connection = sqlite3.connect("database.db")
            query = "SELECT * FROM Workers"
            result = self.connection.execute(query)
            self.table_widget.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.table_widget.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.table_widget.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.connection.close()
        else:
            self.connection = sqlite3.connect("database.db")
            query = "SELECT * FROM Late"
            result = self.connection.execute(query)
            self.table_widget.tableWidget1.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.table_widget.tableWidget1.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.table_widget.tableWidget1.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.connection.close()

#Отрисовка таблица
    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)