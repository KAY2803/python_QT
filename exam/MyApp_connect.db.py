import pyodbc
from PySide2 import QtWidgets, QtSql, QtCore, QtGui
from PySide2.QtSql import QSqlQuery

from ui.pageCases1 import Ui_WindowCases
from ui.page_1 import Ui_MainWindow
from ui.emp import Ui_MainWindowEmp

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

        self.initTVModelCases()

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

    def initTVModelCases(self):
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

        self.ui.tableViewClients.setColumnWidth(0, 80)
        self.ui.tableViewClients.setColumnWidth(1, 200)
        self.ui.tableViewClients.setColumnWidth(2, 150)
        self.ui.tableViewClients.setColumnWidth(3, 200)
        self.ui.tableViewClients.resizeRowsToContents()

        self.centralWidget().setMinimumWidth(self.ui.tableViewClients.columnWidth(0) +
                                             self.ui.tableViewClients.columnWidth(1) +
                                             self.ui.tableViewClients.columnWidth(2) +
                                             self.ui.tableViewClients.columnWidth(3) +
                                             self.ui.tableViewClients.columnWidth(4) +
                                             self.ui.tableViewClients.columnWidth(5) + 50)

        # self.ui.tableViewClients.horizontalHeader().setStretchLastSection(True)
        # self.ui.tableViewClients.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

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

    # def changeEvent(self, event: QtCore.QEvent) -> None:


class EditableSQLModel(QtSql.QSqlTableModel):
    def __init__(self, parent=None):
        super(EditableSQLModel, self).__init__(parent)

    def data(self, item, role):
        if role == QtCore.Qt.BackgroundRole:
            if item.row() % 2:
                return QtGui.QColor(QtCore.Qt.blue)


class Employees(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindowEmp()
        self.ui.setupUi(self)

        self.initDB()

        self.initSQLModel()

        # self.initUi()


    # def initUi(self):
    #     self.window = QtWidgets.QWidget()
    #     self.window.setWindowTitle('Сотрудники')
    #
    #     self.vbox = QtWidgets.QVBoxLayout()
    #     self.tv = QtWidgets.QTableView()
    #     self.vbox.addWidget(self.tv)
    #
    #     self.window.setLayout(self.vbox)


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

    def initSQLModel(self):
        self.empModel = EditableSQLModel()
        # self.empModel = QtSql.QSqlTableModel()
        self.empModel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.empModel.setTable('[staff].[employees]')
        print(self.cursor.execute('SELECT * from [staff].[employees]').fetchall())
        self.empModel.select()

        self.empModel.setHeaderData(0, QtCore.Qt.Horizontal, 'id')
        self.empModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Фамилия')
        self.empModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Имя')
        self.empModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Должность')

        self.ui.tableViewEmp.setModel(self.empModel)

        # self.cursor.execute('SELECT LastName from [staff].[employees]')
        # data = self.cursor.fetchall()
        # print(data)
        # self.tv.setModel(self.empModel)


        # index = self.empModel.rowCount()
        # self.empModel.setData(self.empModel.index(index, 0), data[0][0])
        # self.empModel.setData(self.empModel.index(index, 0), data[1][0])
        # for elem in data:
        #     print(elem)
            # item1, item2 = elem[0], elem[1]
        # print(item1, item2)


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