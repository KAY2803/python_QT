# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindowEmp(object):
    def setupUi(self, MainWindowEmp):
        if not MainWindowEmp.objectName():
            MainWindowEmp.setObjectName(u"MainWindowEmp")
        MainWindowEmp.resize(455, 601)
        self.centralwidget = QWidget(MainWindowEmp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableViewEmp = QTableView(self.centralwidget)
        self.tableViewEmp.setObjectName(u"tableViewEmp")

        self.horizontalLayout.addWidget(self.tableViewEmp)

        MainWindowEmp.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindowEmp)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 455, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindowEmp.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindowEmp)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowEmp.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindowEmp)

        QMetaObject.connectSlotsByName(MainWindowEmp)
    # setupUi

    def retranslateUi(self, MainWindowEmp):
        MainWindowEmp.setWindowTitle(QCoreApplication.translate("MainWindowEmp", u"MainWindow", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindowEmp", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
    # retranslateUi

