from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3

class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Удалить")
        self.setWindowIcon(QIcon("icon/trash.png"))
        self.setWindowTitle("Удалить работника")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deleteWorker)
        layout = QVBoxLayout()
        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("№")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deleteWorker(self):
        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from Workers WHERE roll="+str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Работник удален')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Не удалось удалить работника')