from PyQt5 import QtWidgets
import sys
from GuiApp import MainGui
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainGui.BaseApp()
    window.show()
    app.exec_()  # и запускаем приложение
if __name__ == '__main__':
    main()