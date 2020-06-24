from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3

class UpdateLate(QDialog):
    def __init__(self, *args, **kwargs):
        super(UpdateLate, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText("Изменить")
        self.setWindowIcon(QIcon("icon/updateL.png"))
        self.setWindowTitle("Изменить работника")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchWorker)
        self.updateinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.updateinput.setValidator(self.onlyInt)
        self.updateinput.setPlaceholderText("№")

        self.updateRol = ""
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Имя")
        self.countinput = QLineEdit()
        self.countinput.setPlaceholderText("Колличество")
        self.updateBtn = QPushButton()
        self.updateBtn.setText("Изменить")
        self.updateBtn.clicked.connect(self.updateWorker)

        layout = QVBoxLayout()
        layout.addWidget(self.updateinput)
        layout.addWidget(self.QBtn)
        layout.addWidget(self.nameinput)
        layout.addWidget(self.countinput)
        layout.addWidget(self.updateBtn)
        self.setLayout(layout)

        self.nameinput.hide()
        self.countinput.hide()
        self.updateBtn.hide()

    def updateWorker(self):
        print(self.updateRol)
        name = self.nameinput.text()
        count = self.countinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE Late "
                           "SET name = ?, count=?"
                           "WHERE roll = ?",
                           (name, count, str(self.updateRol)))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Работник изменен')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Не удалось изменить работника')

    def searchWorker(self):
        self.updateRol = self.updateinput.text()
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        result = self.c.execute("SELECT * from Late WHERE roll=" + str(self.updateRol))
        row = result.fetchone()
        self.conn.commit()
        self.c.close()
        self.conn.close()

        if row is not None:
            self.setFixedWidth(300)
            self.setFixedHeight(250)
            self.updateinput.hide()
            self.QBtn.hide()
            self.nameinput.show()
            self.countinput.show()
            self.updateBtn.show()
        else:
            QMessageBox.warning(QMessageBox(), 'Error', 'Работник не найден.')