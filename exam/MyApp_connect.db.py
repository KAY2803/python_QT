import pyodbc
from PySide2 import QtWidgets, QtSql, QtCore, QtGui
from PySide2.QtSql import QSqlQuery

from ui.pageCases1 import Ui_WindowCases
from ui.page_1 import Ui_MainWindow


class Page1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonCases.clicked.connect(self.onPushButtonCasesClicked)
        self.ui.pushButtonEmp.clicked.connect(self.onPushButtonEmpClicked)

    def onPushButtonCasesClicked(self):
        self.cases = Cases()
        self.cases.show()

    def onPushButtonEmpClicked(self):
        self.emp = Employees()
        self.emp.show()


class Cases(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initDB()

        self.ui = Ui_WindowCases()
        self.ui.setupUi(self)

        self.initTableViewModel()

        self.ui.pushButtonSave.clicked.connect(self.onPushButtonSaveClicked)

        # self.model = QtSql.QSqlRelationalTableModel()
        # self.model.setTable('litigation.cases')
        # self.model.setRelation(3, QtSql.QSqlRelation('litigation.tasks', 'CaseID', 'TaskDateTime'))
        # self.model.select()
        # self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

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

    def initTableViewModel(self):
        self.sim = QtGui.QStandardItemModel()
        self.cursor.execute('SELECT DISTINCT LC.CaseNumber, LC.Court, PP.PersonName, LC.Claims, LT.TaskDateTime, SE.LastName '
                            'FROM litigation.cases as LC '
                            'LEFT JOIN parties.case_participants as PCP '
                            'ON LC.id = PCP.CaseID '
                            'LEFT JOIN parties.persons as PP '
                            'ON PCP.PersonID = PP.id '
                            'LEFT JOIN staff.employees as SE '
                            'ON LC.DoerID = SE.id '
                            'JOIN litigation.tasks as LT '
                            'on LC.id = LT.CaseID')
        data = self.cursor.fetchall()
        # print(data)

        for elem in data:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))
            item5 = QtGui.QStandardItem(str(elem[4]))
            item6 = QtGui.QStandardItem(str(elem[5]))
            self.sim.appendRow([item1, item2, item3, item4, item5, item6])
        self.sim.setHorizontalHeaderLabels(['Номер дела', 'Суд', 'Истец', 'Требования', 'Дата заседания', 'Исполнитель'])
        self.ui.tableViewClients.setModel(self.sim)
        self.ui.tableViewClients.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableViewClients.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # self.ui.tableViewClients.selectionModel().currentChanged.connect(self.changecell)

    # def changecell(self, cell):
    #     self.ui.tableViewClients.commitData(self.ui.centralwidget)

    def onPushButtonSaveClicked(self):
        index = self.ui.tableViewClients.currentIndex()
        value = self.sim.itemData(index)[0]
        self.sim.setData(index, value)
        self.sim.submit()
        # self.ui.tableViewClients.update()
        self.cursor.execute('UPDATE litigation.cases'
                            f'SET Court = {str(value)}')
        self.cursor.commit()
        self.con.commit()


class Employees(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initDB()

        self.initUi()

        self.initListViewModel()

    def initUi(self):
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.window = QtWidgets.QTableView()
        self.window.setWindowTitle('Сотрудники')

        # self.setMinimumSize(500, 700)
        # self.setMaximumSize(500, 700)


        # self.model = QtSql.QSqlRelationalTableModel()
        # self.model.setTable('litigation.cases')
        # self.model.setRelation(3, QtSql.QSqlRelation('litigation.tasks', 'CaseID', 'TaskDateTime'))
        # self.model.select()
        # self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

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

    def initListViewModel(self):
        self.lm = QtSql.QSqlQueryModel(parent=self.window)
        self.lm.setHeaderData(1, QtCore.Qt.Horizontal, 'Фамилия')
        self.cursor.execute('SELECT LastName from [staff].[employees]')
        data = self.cursor.fetchall()
        print(data)

        self.window.setModel(self.lm)


        # self.model = QtSql.QSqlTableModel()
        # self.model.setTable('litigation.cases')

        # self.model.select()
        # self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'Номер дела')
        # self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'Суд')
        # self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'Истец')
        # self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'Требования')
        # self.model.setHeaderData(4, QtCore.Qt.Horizontal, 'Дата заседания')
        # self.model.setHeaderData(5, QtCore.Qt.Horizontal, 'Исполнитель')

        # index = self.model.rowCount()
        # query = QSqlQuery()
        # query.exec_('select * from litigation.cases')
        # query.exec_('SELECT LC.CaseNumber, LC.Court, PP.PersonName, LC.Claims, LT.TaskDateTime, SE.LastName '
        #            'FROM litigation.cases as LC '
        #            'LEFT JOIN parties.case_participants as PCP '
        #            'ON LC.id = PCP.CaseID '
        #            'LEFT JOIN parties.persons as PP '
        #            'ON PCP.PersonID = PP.id '
        #            'LEFT JOIN staff.employees as SE '
        #            'ON LC.DoerID = SE.id '
        #            'JOIN litigation.tasks as LT '
        #            'on LC.id = LT.CaseID')

        # for elem in query:
        #     item1 = QtSql.QSqlQuery.value(self, 1)
        #     item2 = QtSql.QSqlQuery.value(self, 2)
        #     item3 = QtSql.QSqlQuery.value(self, 3)
        #     item4 = QtSql.QSqlQuery.value(self, 4)
        #     item5 = QtSql.QSqlQuery.value(self, 5)
        #     item6 = QtSql.QSqlQuery.value(self, 6)
        #     print(item1, item2, item3, item4, item5, item6)item6

        # print(query.value('CaseNumber'))

        # self.model.setData(self.model.index(index, 1), item1)
        # self.model.setData(self.model.index(index, 2), item2)
        # self.model.setData(self.model.index(index, 3), item3)
        # self.model.setData(self.model.index(index, 4), item4)
        # self.model.setData(self.model.index(index, 5), item5)
        # self.model.setData(self.model.index(index, 6), item6)

        # self.ui.tableViewClients.setModel(self.model)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Page1()
    myapp.show()

    app.exec_()