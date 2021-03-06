from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3

class UpdateDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(UpdateDialog, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText("Изменить")
        self.setWindowIcon(QIcon("icon/update.png"))
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
        self.branchinput = QComboBox()
        self.branchinput.addItem("Комерческий отдел")
        self.branchinput.addItem("Отдел логистики")
        self.branchinput.addItem("Отдел кадров")
        self.branchinput.addItem("Отдел маркетинга")
        self.branchinput.addItem("Служба безопасности")
        self.branchinput.addItem("Производственный отдел")
        self.seminput = QLineEdit()
        self.seminput.setPlaceholderText("Время")
        self.seminput.setInputMask('99 99')
        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Номер")
        self.mobileinput.setInputMask('9 999 9999999')
        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Адрес")
        self.updateBtn = QPushButton()
        self.updateBtn.setText("Изменить")
        self.updateBtn.clicked.connect(self.updateWorker)

        layout = QVBoxLayout()
        layout.addWidget(self.updateinput)
        layout.addWidget(self.QBtn)
        layout.addWidget(self.nameinput)
        layout.addWidget(self.branchinput)
        layout.addWidget(self.seminput)
        layout.addWidget(self.mobileinput)
        layout.addWidget(self.addressinput)
        layout.addWidget(self.updateBtn)
        self.setLayout(layout)

        self.nameinput.hide()
        self.branchinput.hide()
        self.seminput.hide()
        self.mobileinput.hide()
        self.addressinput.hide()
        self.updateBtn.hide()

    def updateWorker(self):
        print(self.updateRol)
        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.text()
        mobile = self.mobileinput.text()
        address = self.addressinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("UPDATE Workers "
                           "SET name = ?, branch = ?, sem = ?, Mobile = ?, address = ?"
                           "WHERE roll = ?",
                           (name, branch, sem, mobile, address, str(self.updateRol)))
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
        result = self.c.execute("SELECT * from Workers WHERE roll=" + str(self.updateRol))
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
            self.branchinput.show()
            self.seminput.show()
            self.mobileinput.show()
            self.addressinput.show()
            self.updateBtn.show()
        else:
            QMessageBox.warning(QMessageBox(), 'Error', 'Работник не найден.')


