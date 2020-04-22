import sys
from PyQt5 import QtWidgets
from GuiApp import App
from GuiApp import Control
from GuiApp import Workers
from GuiApp import GuiSignal

class BaseApp(QtWidgets.QMainWindow, App.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        