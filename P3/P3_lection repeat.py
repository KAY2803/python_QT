import time

from PySide2 import QtWidgets, QtCore, QtGui


class MyApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initThreads()

    def initThreads(self):
        self.timerThread = TimerThread()
        # self.timerThread.start() - чтобы запускался сразу при открытии приложения

        self.timerThread.started.connect(self.timerThreadStarted)
        self.timerThread.finished.connect(self.timerThreadFinished)
        self.timerThread.timersignal.connect(self.timerThreadTimersignal)

    def initUi(self):
        # ui
        # self.setFixedSize(300, 200)
        self.lineEditStart = QtWidgets.QLineEdit()
        self.lineEditStart.setPlaceholderText('Введите количество секунд')

        self.pushButtonStart = QtWidgets.QPushButton()
        self.pushButtonStart.setText('Старт')
        # self.pushButtonStart.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
        #                                    QtWidgets.QSizePolicy.Policy.Expanding)

        self.pushButtonStop = QtWidgets.QPushButton()
        self.pushButtonStop.setText('Стоп')
        # self.pushButtonStop.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
        #                                   QtWidgets.QSizePolicy.Policy.Expanding)
        self.pushButtonStop.setEnabled(False)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditStart)
        layout.addWidget(self.pushButtonStart)
        layout.addWidget(self.pushButtonStop)
        # layout.addSpacerItem(QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Policy.Expanding,
        #                                            QtWidgets.QSizePolicy.Policy.Expanding))

        self.setLayout(layout)

        # widgets signals
        self.pushButtonStart.clicked.connect(self.onPushButtonStartClicked)
        self.pushButtonStop.clicked.connect(self.onPushButtonStopClicked)

    # widgets slots
    def onPushButtonStartClicked(self):
        try:
            self.timerThread.timeCount = int(self.lineEditStart.text())
            self.timerThread.start()
        except ValueError:
            self.lineEditStart.setText('')
            QtWidgets.QMessageBox.warning(self, 'Ошибка!', 'Таймер поддерживает только целочисленные значения')

    def onPushButtonStopClicked(self):
        # self.timerThread.terminate() - не совсем корректно использовать, т.к. он убивает поток полностью в любой момент времени
    # советуют использовать флаги - см в run self.status
        self.timerThread.status = False


    # Thread slots
    def timerThreadStarted(self):
        self.pushButtonStart.setEnabled(False)
        self.pushButtonStop.setEnabled(True)
        self.lineEditStart.setEnabled(False)

    def timerThreadFinished(self):
        self.pushButtonStart.setEnabled(True)
        self.pushButtonStop.setEnabled(False)
        self.lineEditStart.setEnabled(True)
        self.lineEditStart.setText('')
        QtWidgets.QMessageBox.about(self, 'Успешно', 'Отсчет закончен')

    def timerThreadTimersignal(self, emit_value):
        self.lineEditStart.setText(emit_value)


class TimerThread(QtCore.QThread):
    # создаем свой сигнал через атрибут класса (пользовательский сигнал). Наименование любое
    timersignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timeCount = None

    def run(self):
        self.status = True
        if self.timeCount is None:
            self.timeCount = 10

        # for i in range(self.timeCount, 0, -1): - передаем данные из потока
        #     #print(i)
        #     self.timersignal.emit(str(i))
        #     time.sleep(1)

        while self.status: # реализация кнопки стоп
            if self.timeCount < 1:
                break
            time.sleep(1)
            self.timeCount -= 1
            self.timersignal.emit(str(self.timeCount))

    # def showEvent(self, event:QtGui.QShowEvent) -> None:
    #     print(self.width())
    #     print(self.height())
    #
    #     self.setFixedSize(self.width(), self.height())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = MyApp()
    myapp.show()

    app.exec_()