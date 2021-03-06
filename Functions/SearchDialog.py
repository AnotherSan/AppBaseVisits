from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText("Поиск")
        self.setWindowIcon(QIcon("icon/search.png"))
        self.setWindowTitle("Поиск")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchWorker)
        layout = QVBoxLayout()
        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("№")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchWorker(self):
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from Workers WHERE roll="+str(searchrol))
            row = result.fetchone()
            serachresult = "№ : "+str(row[0])+'\n'+"Имя : "+str(row[1])+'\n'+"Отдел : "+str(row[2])+'\n'+"Время : "+str(row[3])+'\n'+"Адрес : "+str(row[5])
            QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Работник не найден.')