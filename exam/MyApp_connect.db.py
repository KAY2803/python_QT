import sys
import pyodbc

from PySide2 import QtWidgets, QtSql, QtCore, QtGui
from PySide2.QtSql import QSqlQuery

from ui.pageCases1 import Ui_WindowCases
from ui.page_1 import Ui_MainWindow
from ui.emp import Ui_MainWindowEmp


"""Начальная страница приложения. Позволяет выбрать представление информации в виде судебных дел либо сотрудников"""


class Page1(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonCases.clicked.connect(self.onPushButtonCasesClicked)
        self.ui.pushButtonEmp.clicked.connect(self.onPushButtonEmpClicked)

    """Кнопки на начальной странице приложения "Дела", "Сотрудники" """

    def onPushButtonCasesClicked(self):
        self.cases = Cases()
        self.cases.show()

    def onPushButtonEmpClicked(self):
        self.emp = Employees()
        self.emp.show()

    """Переопределение события закрытия окна"""

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно?",
                                               "Вы действительно хотите закрыть окно?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


"""Представление судебных дел"""


class Cases(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initDB()

        self.ui = Ui_WindowCases()
        self.ui.setupUi(self)

        self.initTVModelCases()

        self.ui.pushButtonSave.clicked.connect(self.onPushButtonSaveClicked)
        self.ui.addRow.triggered.connect(self.addRowTriggered)
        self.ui.addColumn.triggered.connect(self.addColumnTriggered)

        # self.model = QtSql.QSqlRelationalTableModel()
        # self.model.setTable('litigation.cases')
        # self.model.setRelation(3, QtSql.QSqlRelation('litigation.tasks', 'CaseID', 'TaskDateTime'))
        # self.model.select()
        # self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

    """Подключение к БД"""

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

    """Создание модели для отображения данных о судебных делах из БД в tableView"""

    def initTVModelCases(self):
        # создание модели
        self.sim = QtGui.QStandardItemModel()

        # запрос данных из БД
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

        # передача данных в модель
        for elem in data:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))
            item5 = QtGui.QStandardItem(str(elem[4]))
            item6 = QtGui.QStandardItem(str(elem[5]))
            self.sim.appendRow([item1, item2, item3, item4, item5, item6])

        # установление заголовков столбцов модели
        self.sim.setHorizontalHeaderLabels(['Номер дела', 'Суд', 'Истец', 'Требования', 'Дата заседания', 'Исполнитель'])

        # установка модели на tableView
        self.ui.tableViewClients.setModel(self.sim)

        # выделение строки
        self.ui.tableViewClients.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # self.ui.tableViewClients.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # установка размеров столбцов
        self.ui.tableViewClients.setColumnWidth(0, 80)
        self.ui.tableViewClients.setColumnWidth(1, 200)
        self.ui.tableViewClients.setColumnWidth(2, 150)
        self.ui.tableViewClients.setColumnWidth(3, 200)
        self.ui.tableViewClients.resizeRowsToContents()
        # setAligment(QtCore.Qt.AlignHCenter)

        # установка ширины основного окна
        self.centralWidget().setMinimumWidth(self.ui.tableViewClients.columnWidth(0) +
                                             self.ui.tableViewClients.columnWidth(1) +
                                             self.ui.tableViewClients.columnWidth(2) +
                                             self.ui.tableViewClients.columnWidth(3) +
                                             self.ui.tableViewClients.columnWidth(4) +
                                             self.ui.tableViewClients.columnWidth(5) + 50)


    # Кнопка сохранения данных в БД - ОНА НЕ СРАБАТЫВАЕТ, НИЧЕГО НЕ СОХРАНЯЕТСЯ.
    # Ниже в классе Employees попыталась сделать через другую модель (не QItemModel, а SQLTableModel).
    # Были такие примеры на лекциях. Но я не понимаю, почему можно использовать совершенно разные модели из разных
    # классов (первый из QtGui - расширяет возможности графического интерфейса, а второй - QtSQL).
    # Второй вариант через QtSQL у меня не то, что не работает, а еще даже и не выводит данные в приложение,
    # только печатает в консоли

    def onPushButtonSaveClicked(self):
        index = self.ui.tableViewClients.currentIndex()
        value = self.sim.itemData(index)[0]
        self.sim.setData(index, value)
        self.sim.submit()
        print(value)
        # self.ui.tableViewClients.update()
        self.cursor.execute('UPDATE litigation.cases'
                            f'SET Court = {str(value)}')
        self.cursor.commit()
        self.con.commit()

    # слоты для меню
    @QtCore.Slot()
    def addRowTriggered(self):
        self.sim.insertRow(self.sim.rowCount(), [])

    @QtCore.Slot()
    def addColumnTriggered(self):
        self.sim.insertColumn(self.sim.rowCount(), [])

    """Переопределение события закрытия окна"""
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно?",
                                               "Вы действительно хотите закрыть окно?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


""""Представление сотрудников"""


"""Переопределение параметров модели"""


class EditableSQLModel(QtSql.QSqlTableModel):
    def __init__(self, parent=None):
        super(EditableSQLModel, self).__init__(parent)

    def data(self, item, role):
        if role == QtCore.Qt.BackgroundRole:
            if item.row() % 2:
                return QtGui.QColor(QtCore.Qt.blue)


"""Представление сотрудников"""


class Employees(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindowEmp()
        self.ui.setupUi(self)

        self.initDB()

        self.initSQLModel()

    """Подключение к БД"""

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

    """Создание модели для отображения данных о сотрудниках из БД в tableView"""

    def initSQLModel(self):

        """создание модели"""
        self.empModel = EditableSQLModel()
        # self.empModel = QtSql.QSqlTableModel() - ВАРИАНТ БЕЗ ПЕРЕОПРЕДЕЛЕНИЯ МОДЕЛИ
        self.empModel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)

        """Подключение к таблице с данными для отображения в модели"""
        self.empModel.setTable('[staff].[employees]')
        print(self.cursor.execute('SELECT * from [staff].[employees]').fetchall())
        self.empModel.select()

        self.empModel.setHeaderData(0, QtCore.Qt.Horizontal, 'id')
        self.empModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Фамилия')
        self.empModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Имя')
        self.empModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Должность')

        self.ui.tableViewEmp.setModel(self.empModel)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Page1()
    myapp.show()

    app.exec_()