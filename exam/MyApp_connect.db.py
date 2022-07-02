import sys
import pyodbc
from mysql.connector import Error

from PySide2 import QtCore, QtWidgets, QtSql, QtGui
from PySide2.QtSql import QSqlTableModel
from PySide2.QtWidgets import QTableView

from ui.page_1 import Ui_MainWindow
from ui.pageCases1 import Ui_WindowCases


class Page1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonCases.clicked.connect(self.onPushButtonCasesClicked)

    def onPushButtonCasesClicked(self):
        self.cases = Cases()
        self.cases.show()


class Cases(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_WindowCases()
        self.ui.setupUi(self)

        self.initDB()

        # self.initUi()

        self.initTableViewModel()

        # self.model = QtSql.QSqlRelationalTableModel()
        # self.model.setTable('litigation.cases')
        # self.model.setRelation(3, QtSql.QSqlRelation('litigation.tasks', 'CaseID', 'TaskDateTime'))
        # self.model.select()
        # self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

    # def initUi(self):
    #     cw = QtWidgets.QWidget()
    #
    #     self.tableView = QtWidgets.QTableView()
    #
    #     l = QtWidgets.QVBoxLayout()
    #     l.addWidget(self.tableView)
    #
    #     cw.setLayout(l)
    #     self.setCentralWidget(cw)

    def initTableViewModel(self):
        sim = QtGui.QStandardItemModel()
        self.cursor.execute('SELECT CaseNumber, Court, ClaimantID, DoerID FROM litigation.cases')
        lst = self.cursor.fetchall()
        for elem in lst:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))

        sim.appendRow([item1, item2, item3, item4])
        sim.setHorizontalHeaderLabels(['Номер дела','Суд', 'Истец', 'Исполнитель'])

        self.ui.tableViewClients.setModel(sim)

    def initDB(self):
        server = 'vpngw.avalon.ru'
        db = 'DevDB2022_KimAY'
        user = 'tsqllogin'
        pasw = 'Pa$$w0rd'
        self.con = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; '
            'SERVER=' + server +
            ';DATABASE=' + db +
            ';UID=' + user +
            ';PWD=' + pasw)
        self.cursor = self.con.cursor()
        self.cursor.execute('SELECT CaseNumber, Court, ClaimantID, DoerID FROM litigation.cases')
        # self.cursor.execute('SELECT * FROM litigation.cases')
        print(self.cursor.fetchall())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Page1()
    myapp.show()

    app.exec_()