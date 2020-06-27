from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sqlite3

class InsertLate(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertLate, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText("Добавить")
        self.setWindowIcon(QIcon("icon/Late.png"))
        self.setWindowTitle("Добавить работника")
        self.setFixedWidth(300)
        self.setFixedHeight(250)
        self.QBtn.clicked.connect(self.addWorker)

        layout = QVBoxLayout()
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Имя")
        layout.addWidget(self.nameinput)

        self.countinput = QLineEdit()
        self.countinput.setPlaceholderText("Колличество")
        layout.addWidget(self.countinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addWorker(self):
        name = self.nameinput.text()
        count=self.countinput.text()

        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO Late (name,count) VALUES (?,?)",(name,count))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Работник добавлен в базу')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Не удалось добавить работника')