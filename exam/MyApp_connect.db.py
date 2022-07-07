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
        self.ui.pushButtonDel.clicked.connect(self.onPushButtonDelClicked)

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
        self.ui.tableViewCases.setModel(self.sim)

        # выделение строки
        self.ui.tableViewCases.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # self.ui.tableViewCases.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # установка размеров столбцов
        self.ui.tableViewCases.setColumnWidth(0, 80)
        self.ui.tableViewCases.setColumnWidth(1, 200)
        self.ui.tableViewCases.setColumnWidth(2, 150)
        self.ui.tableViewCases.setColumnWidth(3, 200)
        self.ui.tableViewCases.resizeRowsToContents()
        # setAligment(QtCore.Qt.AlignHCenter)

        # установка ширины основного окна
        self.centralWidget().setMinimumWidth(self.ui.tableViewCases.columnWidth(0) +
                                             self.ui.tableViewCases.columnWidth(1) +
                                             self.ui.tableViewCases.columnWidth(2) +
                                             self.ui.tableViewCases.columnWidth(3) +
                                             self.ui.tableViewCases.columnWidth(4) +
                                             self.ui.tableViewCases.columnWidth(5) + 50)


    # Кнопка сохранения данных в БД - ОНА НЕ СРАБАТЫВАЕТ, НИЧЕГО НЕ СОХРАНЯЕТСЯ.
    # Ниже в классе Employees попыталась сделать через другую модель (не QItemModel, а SQLTableModel).
    # Были такие примеры на лекциях. Но я не понимаю, почему можно использовать совершенно разные модели из разных
    # классов (первый из QtGui - расширяет возможности графического интерфейса, а второй - QtSQL).
    # Второй вариант через QtSQL у меня не то, что не сохраняет, а еще даже и не выводит данные в приложение,
    # только печатает в консоли

    def onPushButtonSaveClicked(self):
        index = self.ui.tableViewCases.currentIndex()
        value = self.sim.itemData(index)[0]
        self.sim.setData(index, value)
        self.sim.submit()
        print(value)
        # self.ui.tableViewCases.update()
        self.cursor.execute('UPDATE litigation.cases'
                            f'SET Court = {str(value)}')
        self.cursor.commit()
        self.con.commit()

    def onPushButtonDelClicked(self):
        reply = QtWidgets.QMessageBox.question(self, 'Удалить строку?',
                                       "Вы действительно хотите удалить строку?",
                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                       QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.sim.removeRow(self.ui.tableViewCases.currentIndex().row())


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


"""Представление сотрудников"""


class Employees(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindowEmp()
        self.ui.setupUi(self)

        self.initDB()

        self.initTVModelEmp()

        self.ui.pushbuttonAddRow.clicked.connect(self.onPushButtonAddRow)
        self.ui.pushbuttonAddColumn.clicked.connect(self.onPushButtonAddColumn)
        self.ui.pushbuttonDelRow.clicked.connect(self.onPushButtonDelRow)
        self.ui.pushbuttonDelColumn.clicked.connect(self.onPushButtonDelColumn)
        #
        # self.ui.actionSave.triggered.connect(self.saveTriggered)
        # self.ui.ActionCopy.triggered.connect(self.copyTriggered)

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

    def initTVModelEmp(self):
        # создание модели
        self.simE = QtGui.QStandardItemModel()

        # запрос данных из БД
        self.cursor.execute('SELECT * FROM staff.employees')
        data = self.cursor.fetchall()
        # print(data)

        # передача данных в модель
        for elem in data:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))
            self.simE.appendRow([item1, item2, item3, item4])

        # установление заголовков столбцов модели
        self.simE.setHorizontalHeaderLabels(['№', 'Фамилия', 'Имя', 'Должность'])

        # установка модели на tableView
        self.ui.tableViewEmp.setModel(self.simE)

        # выделение строки
        self.ui.tableViewEmp.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        # self.ui.tableViewCases.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # установка размеров столбцов
        self.ui.tableViewEmp.setColumnWidth(0, 20)
        self.ui.tableViewEmp.setColumnWidth(1, 130)
        self.ui.tableViewEmp.setColumnWidth(2, 130)
        self.ui.tableViewEmp.setColumnWidth(3, 100)
        self.ui.tableViewEmp.resizeRowsToContents()
        self.ui.tableViewEmp.setColumnHidden(0, True)
        # setAligment(QtCore.Qt.AlignHCenter)

        # установка ширины основного окна
        self.centralWidget().setMinimumWidth(self.ui.tableViewEmp.columnWidth(0) +
                                             self.ui.tableViewEmp.columnWidth(1) +
                                             self.ui.tableViewEmp.columnWidth(2) +
                                             self.ui.tableViewEmp.columnWidth(3) + 200)

    def onPushButtonAddRow(self):
        self.simE.insertRow(self.simE.rowCount(), [])

    def onPushButtonAddColumn(self):
        self.simE.insertColumn(self.simE.columnCount(), [])

    def onPushButtonDelRow(self):
        self.simE.removeRow(self.ui.tableViewEmp.currentIndex().row())

    def onPushButtonDelColumn(self):
        print(self.ui.tableViewEmp.currentIndex().column())
        self.simE.removeColumn(self.ui.tableViewEmp.currentIndex().column())

    # def onPushButtonSaveClicked(self):
    #     index = self.ui.tableViewEmp.currentIndex()
    #     value = self.simE.itemData(index)[0]
    #     self.simE.setData(index, value)
    #     self.simE.submit()
    #     print(value)
    #     # self.ui.tableViewCases.update()
    #     self.cursor.execute('UPDATE litigation.cases'
    #                         f'SET Court = {str(value)}')
    #     self.cursor.commit()
    #     self.con.commit()
    #



    # # слоты для меню
    # @QtCore.Slot()
    # def addRowTriggered(self):
    #     self.simE.insertRow(self.simE.rowCount(), [])
    #
    # @QtCore.Slot()
    # def addColumnTriggered(self):
    #     self.simE.insertColumn(self.simE.rowCount(), [])

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


#### ВАРИАНТ С QSL #####
# """"Представление сотрудников"""
# """Переопределение параметров модели"""
#
#
# class EditableSQLModel(QtSql.QSqlTableModel):
#     def __init__(self, parent=None):
#         super(EditableSQLModel, self).__init__(parent)
#
#     def data(self, item, role):
#         if role == QtCore.Qt.BackgroundRole:
#             if item.row() % 2:
#                 return QtGui.QColor(QtCore.Qt.blue)


# class Employees(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.ui = Ui_MainWindowEmp()
#         self.ui.setupUi(self)
#
#         self.initDB()
#
#         self.initSQLModel()
#
#     """Подключение к БД"""
#
#     def initDB(self):
#         server = 'vpngw.avalon.ru'
#         db = 'DevDB2022_KimAY'
#         user = 'tsqllogin'
#         pasw = 'Pa$$w0rd'
#         self.con = pyodbc.connect(
#             'DRIVER={ODBC Driver 17 for SQL Server}; '
#             'SERVER=' + server +
#             ';DATABASE=' + db +
#             ';UID=' + user +
#             ';PWD=' + pasw)
#         self.cursor = self.con.cursor()
#
#     """Создание модели для отображения данных о сотрудниках из БД в tableView"""
#
#     def initSQLModel(self):
#
#         """создание модели"""
#         self.empModel = EditableSQLModel()
#         # self.empModel = QtSql.QSqlTableModel() - ВАРИАНТ БЕЗ ПЕРЕОПРЕДЕЛЕНИЯ МОДЕЛИ
#         self.empModel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
#
#         """Подключение к таблице с данными для отображения в модели"""
#         self.empModel.setTable('[staff].[employees]')
#         print(self.cursor.execute('SELECT * from [staff].[employees]').fetchall())
#         self.empModel.select()
#
#         self.empModel.setHeaderData(0, QtCore.Qt.Horizontal, 'id')
#         self.empModel.setHeaderData(1, QtCore.Qt.Horizontal, 'Фамилия')
#         self.empModel.setHeaderData(2, QtCore.Qt.Horizontal, 'Имя')
#         self.empModel.setHeaderData(3, QtCore.Qt.Horizontal, 'Должность')
#
#         self.ui.tableViewEmp.setModel(self.empModel)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Page1()
    myapp.show()

    app.exec_()