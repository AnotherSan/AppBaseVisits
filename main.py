from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,sqlite3
from Functions import InsertDialog
from Functions import SearchDialog
from Functions import DeleteDialog
from Functions import UpdateDialog
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS Workers(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,branch TEXT,sem INTEGER,mobile INTEGER,address TEXT)")
        self.c.close()
        file_menu = self.menuBar().addMenu("&File")
        self.setWindowIcon(QIcon("icon/document.png"))
        self.setWindowTitle("Контроль посещений")
        self.setMinimumSize(800, 600)
        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("№", "Имя", "Отдел", "Время", "Номер","Адрес"))
        self.tableWidget1 = QTableWidget()
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        btn_ac_adduser = QAction(QIcon("icon/add.png"), "Добавить работника", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Добавить работника")
        toolbar.addAction(btn_ac_adduser)
        btn_ac_refresh = QAction(QIcon("icon/refresh.png"),"Обновить",self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Обновить таблицу")
        toolbar.addAction(btn_ac_refresh)
        btn_ac_search = QAction(QIcon("icon/search.png"), "Поиск", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Поиск работника")
        toolbar.addAction(btn_ac_search)
        btn_ac_delete = QAction(QIcon("icon/trash.png"), "Удалить", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Удалить работника")
        toolbar.addAction(btn_ac_delete)
        btn_ac_update = QAction(QIcon("icon/document.png"), "Редактировать", self)
        btn_ac_update.triggered.connect(self.updateTable)
        btn_ac_update.setStatusTip("Редактировать")
        toolbar.addAction(btn_ac_update)
        adduser_action = QAction(QIcon("icon/add.png"),"Добавить работника", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)
        searchuser_action = QAction(QIcon("icon/search.png"), "Поиск", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)
        deluser_action = QAction(QIcon("icon/trash.png"), "Удалить", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)
        uppuser_action = QAction(QIcon("icon/document.png"), "Редактировать", self)
        uppuser_action.triggered.connect(self.updateTable)
        file_menu.addAction(uppuser_action)

    def loaddata(self):
        self.connection = sqlite3.connect("database.db")
        query = "SELECT * FROM Workers"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()

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

    def insert(self):
        dlg = InsertDialog.InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog.DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog.SearchDialog()
        dlg.exec_()
    def updateTable(self):
        dlg=UpdateDialog.UdateDialog()
        dlg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.loaddata()
    sys.exit(app.exec_())