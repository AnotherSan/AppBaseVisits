from PyQt5.QtCore import pyqtSignal, QObject

class BaseSignals(QObject):
    haveBase = pyqtSignal()