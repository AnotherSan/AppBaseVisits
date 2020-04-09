# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Workers.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Workers(object):
    def setupUi(self, Workers):
        Workers.setObjectName("Workers")
        Workers.resize(372, 304)
        self.verticalLayout = QtWidgets.QVBoxLayout(Workers)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Workers)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Workers)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(Workers)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Workers)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(Workers)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Workers)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(Workers)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.spinBox = QtWidgets.QSpinBox(Workers)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)

        self.retranslateUi(Workers)
        QtCore.QMetaObject.connectSlotsByName(Workers)

    def retranslateUi(self, Workers):
        _translate = QtCore.QCoreApplication.translate
        Workers.setWindowTitle(_translate("Workers", "Form"))
        self.label.setText(_translate("Workers", "Введите имя"))
        self.label_2.setText(_translate("Workers", "Введите фамилию"))
        self.label_3.setText(_translate("Workers", "Введите название офиса"))
        self.label_4.setText(_translate("Workers", "Введите ID"))
