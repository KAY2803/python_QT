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
        MainWindowEmp.resize(489, 415)
        self.actionSave = QAction(MainWindowEmp)
        self.actionSave.setObjectName(u"actionSave")
        self.ActionCopy = QAction(MainWindowEmp)
        self.ActionCopy.setObjectName(u"ActionCopy")
        self.centralwidget = QWidget(MainWindowEmp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBoxMenu = QGroupBox(self.centralwidget)
        self.groupBoxMenu.setObjectName(u"groupBoxMenu")
        self.groupBoxMenu.setAcceptDrops(True)
        self.groupBoxMenu.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBoxMenu.setFlat(False)
        self.groupBoxMenu.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushbuttonAddRow = QPushButton(self.groupBoxMenu)
        self.pushbuttonAddRow.setObjectName(u"pushbuttonAddRow")
        self.pushbuttonAddRow.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.pushbuttonAddRow)

        self.pushbuttonAddColumn = QPushButton(self.groupBoxMenu)
        self.pushbuttonAddColumn.setObjectName(u"pushbuttonAddColumn")
        self.pushbuttonAddColumn.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.pushbuttonAddColumn)

        self.pushbuttonDelRow = QPushButton(self.groupBoxMenu)
        self.pushbuttonDelRow.setObjectName(u"pushbuttonDelRow")
        self.pushbuttonDelRow.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.pushbuttonDelRow)

        self.pushbuttonDelColumn = QPushButton(self.groupBoxMenu)
        self.pushbuttonDelColumn.setObjectName(u"pushbuttonDelColumn")
        self.pushbuttonDelColumn.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout.addWidget(self.pushbuttonDelColumn)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBoxMenu)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setAcceptDrops(False)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.tableViewEmp = QTableView(self.centralwidget)
        self.tableViewEmp.setObjectName(u"tableViewEmp")

        self.horizontalLayout.addWidget(self.tableViewEmp)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindowEmp.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindowEmp)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 489, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindowEmp.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindowEmp)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowEmp.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.ActionCopy)

        self.retranslateUi(MainWindowEmp)

        QMetaObject.connectSlotsByName(MainWindowEmp)
    # setupUi

    def retranslateUi(self, MainWindowEmp):
        MainWindowEmp.setWindowTitle(QCoreApplication.translate("MainWindowEmp", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindowEmp", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.ActionCopy.setText(QCoreApplication.translate("MainWindowEmp", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.groupBoxMenu.setTitle(QCoreApplication.translate("MainWindowEmp", u"\u041c\u0435\u043d\u044e", None))
        self.pushbuttonAddRow.setText(QCoreApplication.translate("MainWindowEmp", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.pushbuttonAddColumn.setText(QCoreApplication.translate("MainWindowEmp", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None))
        self.pushbuttonDelRow.setText(QCoreApplication.translate("MainWindowEmp", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a\u0443", None))
        self.pushbuttonDelColumn.setText(QCoreApplication.translate("MainWindowEmp", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindowEmp", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u044f", None))
    # retranslateUi

