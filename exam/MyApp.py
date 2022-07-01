import sys
# import mysql.connector
from PySide2 import QtCore, QtWidgets, QtSql, QtGui
from PySide2.QtSql import QSqlTableModel
from PySide2.QtWidgets import QTableView

import exam.ui.clientsList
from exam.ui.case_form_about import Ui_Form
from exam.ui.clientsList import Ui_MainWindow


class CasesIntro(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_clients.clicked.connect(self.onPushButtonClientsClicked)
        # self.clientsList = ClientsListWindow()
        self.clients = ClientsWindow()

    def onPushButtonClientsClicked(self):
        self.clients.show()

# class ClientsListWindow(QtWidgets.QMainWindow):
#         def __init__(self, parent=None):
#             super().__init__(parent)
#
#             self.ui = Ui_MainWindow()
#             self.ui.setupUi(self)


class ClientsWindow(QtWidgets.QMainWindow):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.initSQLModel()

        def initSQLModel(self):
            self.setWindowTitle("Клиенты")
            self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName('db.cases')
            self.db.open()

            self.model = QSqlTableModel()
            self.model.setTable('clients')
            self.model.select()

            self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'Наименование')
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'Контактное лицо')
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'Телефон')
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'e-mail')

            self.view = QTableView
            self.view.setModel(self.model)
            self.view.setColumnWidth(1, 150)
            self.view.setColumnWidth(2, 150)
            self.view.setColumnWidth(3, 70)
            self.view.setColumnWidth(4, 70)

            self.box = QtWidgets.QVBoxLayout
            self.box.addWidget(self.view)

            self.pushButtonAddClient = QtWidgets.QPushButton('Добавить клиента')
            self.pushButtonAddClient.clicked.connect(self.addClient)
            self.box.addWidget(self.pushButtonAddClient)

            self.pushButtonSaveClient = QtWidgets.QPushButton('Сохранить данные')
            self.pushButtonSaveClient.clicked.connect(self.saveClient)
            self.box.addWidget(self.pushButtonsaveClient)

        def addClient(self):
           self.model.insertRow(self.model.rowCount())

        def saveClient(self):
           self.model.submitAll()


        # self.clients.show()
#
#
# class EditableSQLModel(QtSql.QSqlTableModel):
#     def __init(self, parent=None):
#         super(EditableSQLModel, self).__init__(parent)
#
#     def data(self, item, role):
#         if role == QtCore.Qt.BackgroundRole:
#             if item.row() % 2:
#                 return QtGui.QColor(QtCore.Qt.lightGray)
#         return QtSql.QSqlTableModel.data(self, item, role)
#
#
# class ClientsWindow(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         #todo подключить БД и получать список клиентов (без других данных таблицы clients
#
#
# class ClientsListForm(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = exam.ui.clientsList.Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         self.initSQLModel()
#
#         self.ui.pushButtonAddClient.clicked.connect(self.onPushButtonClientAddClicked)
#
#     def initSQLModel(self):
#         self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
#         self.db.setDatabaseName('cases.db')
#         self.model = EditableSQLModel()
#         self.model.setTable('clients')
#
#         self.model.select()
#         self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'Наименование')
#         self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'Контактное лицо')
#         self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'Телефон')
#         self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'e-mail')
#
#         # self.ui.listViewClients.setModel(self.model)
#         # self.ui.listViewClients.setColumnHidden(0, True)
#         # self.ui.listViewClients.horizontalHeader().setSectionsMovable(True)
#         # self.ui.listViewClients.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
#
#     def onPushButtonClientAddClicked(self):
#         index = self.model.rowCount()
#         self.model.insertRows(index, 1)
#         self.model.setData(self.model.index(index, 1), self.ui.lineEdit.text())
#         self.model.setData(self.model.index(index, 2), self.ui.lineEdit_2.text())
#         self.model.setData(self.model.index(index, 4), self.ui.lineEdit_3.text())
#         self.model.setData(self.model.index(index, 3), self.ui.dateEdit.text())
#         self.model.submitAll()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = CasesIntro()
    myapp.show()

    app.exec_()
