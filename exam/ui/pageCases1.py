# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pageCases1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WindowCases(object):
    def setupUi(self, WindowCases):
        if not WindowCases.objectName():
            WindowCases.setObjectName(u"WindowCases")
        WindowCases.resize(856, 688)
        self.addRow = QAction(WindowCases)
        self.addRow.setObjectName(u"addRow")
        self.addColumn = QAction(WindowCases)
        self.addColumn.setObjectName(u"addColumn")
        self.centralwidget = QWidget(WindowCases)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableViewClients = QTableView(self.centralwidget)
        self.tableViewClients.setObjectName(u"tableViewClients")
        self.tableViewClients.setStyleSheet(u"")
        self.tableViewClients.setFrameShape(QFrame.StyledPanel)
        self.tableViewClients.setFrameShadow(QFrame.Plain)
        self.tableViewClients.setLineWidth(2)
        self.tableViewClients.setMidLineWidth(3)
        self.tableViewClients.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableViewClients.setDragEnabled(True)
        self.tableViewClients.setAlternatingRowColors(True)
        self.tableViewClients.setSortingEnabled(True)
        self.tableViewClients.horizontalHeader().setVisible(True)
        self.tableViewClients.horizontalHeader().setCascadingSectionResizes(True)
        self.tableViewClients.horizontalHeader().setMinimumSectionSize(100)
        self.tableViewClients.horizontalHeader().setDefaultSectionSize(100)
        self.tableViewClients.verticalHeader().setMinimumSectionSize(20)

        self.verticalLayout.addWidget(self.tableViewClients)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonSave = QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setStyleSheet(u"background-color: rgb(212, 212, 255);")

        self.horizontalLayout.addWidget(self.pushButtonSave)

        self.pushButtonDel = QPushButton(self.centralwidget)
        self.pushButtonDel.setObjectName(u"pushButtonDel")
        self.pushButtonDel.setFont(font)
        self.pushButtonDel.setStyleSheet(u"background-color: rgb(212, 212, 255);")

        self.horizontalLayout.addWidget(self.pushButtonDel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        WindowCases.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(WindowCases)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 856, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        WindowCases.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(WindowCases)
        self.statusbar.setObjectName(u"statusbar")
        WindowCases.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.addRow)
        self.menu.addAction(self.addColumn)

        self.retranslateUi(WindowCases)

        QMetaObject.connectSlotsByName(WindowCases)
    # setupUi

    def retranslateUi(self, WindowCases):
        WindowCases.setWindowTitle(QCoreApplication.translate("WindowCases", u"MainWindow", None))
        self.addRow.setText(QCoreApplication.translate("WindowCases", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.addColumn.setText(QCoreApplication.translate("WindowCases", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u043b\u043e\u043d\u043a\u0443", None))
        self.pushButtonSave.setText(QCoreApplication.translate("WindowCases", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButtonDel.setText(QCoreApplication.translate("WindowCases", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("WindowCases", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
    # retranslateUi

