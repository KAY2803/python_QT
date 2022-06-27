import sys
import time

from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QApplication

from ui.MyWidgetP2 import Ui_MainWindow


class MyWidgetP2Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonLT.clicked.connect(self.onpushbuttonclicked)
        self.ui.pushButton_RT.clicked.connect(self.onpushbuttonclicked)
        self.ui.pushButtonLB.clicked.connect(self.onpushbuttonclicked)
        self.ui.pushButton_RB.clicked.connect(self.onpushbuttonclicked)
        self.ui.pushButtonCenter.clicked.connect(self.onpushbuttonclicked)
        self.ui.pushButtonGetInfo.clicked.connect(self.onpushbuttonGetInfoclicked)
        self.ui.pushButtonGetInfo.setShortcut('ctrl+i')


    #### SLOTS ####

    @QtCore.Slot()
    def onpushbuttonclicked(self):
        x = 0
        y = 0
        width_ = QApplication.screenAt(self.pos()).size().width()
        height_ = QApplication.screenAt(self.pos()).size().height()
        sender = self.sender().text()
        buttons = {
            'Лево/Верх': [x, y],
            'Право/Верх': [width_ - self.width(), y],
            'Лево/Низ': [x, height_ - self.height()],
            'Право/Низ': [width_ - self.width(), height_ - self.height()],
            'Центр': [(width_ - self.width())/2, (height_ - self.height())/2]
        }
        x, y = buttons.get(sender)
        self.move(x, y)

    @QtCore.Slot()
    def onpushbuttonGetInfoclicked(self):
        self.ui.plainTextEdit.setPlainText(
            f'{"-" * 20}\n'
            f'Количество экранов: {len(QtWidgets.QApplication.screens())}\n'
            f'Текущее основное окно: {QtWidgets.QApplication.primaryScreen().name()}\n'
            f'Разрешение экрана: {QtWidgets.QApplication.primaryScreen().name()} '
                f'{QtWidgets.QApplication.primaryScreen().size().width()},'
                f'{QtWidgets.QApplication.primaryScreen().size().height()}\n'
            f'Окно {QtWidgets.QApplication.primaryScreen().name()} находится на экране '
                f'{QtWidgets.QApplication.screenAt(self.pos()).name()}\n'
            f'Размеры окна: ширина {self.width()}, длина {self.height()}\n'
            f'Минимальные размеры окна: ширина {self.minimumWidth()}, длина {self.minimumHeight()}\n'
            f'Текущие координаты окна: {self.pos().x()}, {self.pos().y()}\n'
            f'Координаты центра приложения: {self.pos().x() + self.pos().x()/2}, {self.pos().y() + self.pos().y()/2}\n'
            f'{"-" * 20}'
        )



    #### EVENTS ####

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: окно демонстрируется')

    def hideEvent(self, event: QtGui.QHideEvent) -> None:
        self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: окно свернуто')

    def changeEvent(self, event: QtCore.QEvent) -> None:
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: окно минимального размера')
            elif self.isMaximized():
                self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: размер окна максимален ')
        if self.isActiveWindow():
                self.ui.plainTextEdit.appendPlainText(f'{time.ctime()}: окно активировано')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyWidgetP2Window()
    myapp.show()

    app.exec_()