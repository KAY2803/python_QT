# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyWidgetP2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(647, 453)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonLT = QPushButton(self.centralwidget)
        self.pushButtonLT.setObjectName(u"pushButtonLT")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLT.sizePolicy().hasHeightForWidth())
        self.pushButtonLT.setSizePolicy(sizePolicy)
        self.pushButtonLT.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButtonLT)

        self.pushButton_RT = QPushButton(self.centralwidget)
        self.pushButton_RT.setObjectName(u"pushButton_RT")
        sizePolicy.setHeightForWidth(self.pushButton_RT.sizePolicy().hasHeightForWidth())
        self.pushButton_RT.setSizePolicy(sizePolicy)
        self.pushButton_RT.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButton_RT)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.pushButtonCenter = QPushButton(self.centralwidget)
        self.pushButtonCenter.setObjectName(u"pushButtonCenter")
        self.pushButtonCenter.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.pushButtonCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonLB = QPushButton(self.centralwidget)
        self.pushButtonLB.setObjectName(u"pushButtonLB")
        self.pushButtonLB.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_2.addWidget(self.pushButtonLB)

        self.pushButton_RB = QPushButton(self.centralwidget)
        self.pushButton_RB.setObjectName(u"pushButton_RB")
        self.pushButton_RB.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_2.addWidget(self.pushButton_RB)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.pushButtonGetInfo = QPushButton(self.centralwidget)
        self.pushButtonGetInfo.setObjectName(u"pushButtonGetInfo")
        self.pushButtonGetInfo.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.pushButtonGetInfo)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")

        self.horizontalLayout_3.addWidget(self.dial)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout.addWidget(self.lcdNumber)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_4.addWidget(self.plainTextEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 647, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonLT.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButton_RT.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButtonCenter.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.pushButtonLB.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u043e/\u041d\u0438\u0437", None))
        self.pushButton_RB.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043e/\u041d\u0438\u0437", None))
        self.pushButtonGetInfo.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u043a\u043d\u0430", None))
    # retranslateUi

