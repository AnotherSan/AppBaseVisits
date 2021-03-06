from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sqlite3

class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText("Добавить")
        self.setWindowIcon(QIcon("icon/add.png"))
        self.setWindowTitle("Добавить работника")
        self.setFixedWidth(300)
        self.setFixedHeight(250)
        self.QBtn.clicked.connect(self.addWorker)

        layout = QVBoxLayout()
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Имя")
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("Комерческий отдел")
        self.branchinput.addItem("Отдел логистики")
        self.branchinput.addItem("Отдел кадров")
        self.branchinput.addItem("Отдел маркетинга")
        self.branchinput.addItem("Служба безопасности")
        self.branchinput.addItem("Производственный отдел")
        layout.addWidget(self.branchinput)

        self.seminput = QLineEdit()
        self.seminput.setPlaceholderText("Время")
        self.seminput.setInputMask('99 99')
        layout.addWidget(self.seminput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Номер")
        self.mobileinput.setInputMask('9 999 9999999')
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Адрес")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addWorker(self):
        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.text()
        mobile = self.mobileinput.text()
        address = self.addressinput.text()

        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO Workers (name,branch,sem,mobile,address) VALUES (?,?,?,?,?)",(name,branch,sem,mobile,address))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Работник добавлен в базу')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Не удалось добавить работника')