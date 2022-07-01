import sys
# import mysql.connector
from PySide2 import QtCore, QtWidgets, QtSql, QtGui
from PySide2.QtSql import QSqlTableModel
from PySide2.QtWidgets import QTableView

from exam.ui.page_1 import Ui_MainWindow
from exam.ui.page.cases import Ui_WindowCases


class Page1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonCasesclicked.connect(self.onPushButtonCasesClicked)

    def onPushButtonCasesClicked(self):
        self.clients.show()


class ClientsWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_WindowCases()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Page1()
    myapp.show()

    app.exec_()