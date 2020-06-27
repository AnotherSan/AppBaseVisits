from Functions import InsertDialog
from Functions import SearchDialog
from Functions import DeleteDialog
from Functions import UpdateDialog
from Functions import InsertLate
from Functions import UpdateLate
from Functions import DeleteL
from Functions import SearchL
#Сигналы от кнопок
def insert(index):
    if index == 0:
        dlg = InsertDialog.InsertDialog()
    elif index == 1:
        dlg = InsertLate.InsertLate()
    dlg.exec_()

def delete(index):
    if index == 0:
        dlg = DeleteDialog.DeleteDialog()
    elif index == 1:
        dlg = DeleteL.DeleteL()
    dlg.exec_()

def search(index):
    if index == 0:
        dlg = SearchDialog.SearchDialog()
    elif index == 1:
        dlg = SearchL.SearchL()
    dlg.exec_()

def updateTable(index):
    if index == 0:
        dlg = UpdateDialog.UpdateDialog()
    elif index == 1:
        dlg = UpdateLate.UpdateLate()
    dlg.exec_()
