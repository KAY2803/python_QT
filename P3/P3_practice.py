import time
import psutil
import requests
from PySide2 import QtCore, QtWidgets
from P3.practice_form_design import Ui_Form


class QThreadPractice(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initUi()
        self.initThreads()

    def initThreads(self):
        # поток для таймера
        self.timerThread = TimerThread()

        self.timerThread.started.connect(self.timerThreadStarted)
        self.timerThread.finished.connect(self.timerThreadFinished)
        self.timerThread.timerSignal.connect(self.timerThreadTimersignal)

        # поток для проверки доступности сайта
        self.urlThread = CheckUrlThread()
        self.urlThread.urlSignal.connect(self.checkUrlThreadUrlSignal)


    def initUi(self):
        self.ui.pushButtonStartTimer.clicked.connect(self.onPushButtonStartClicked)
        self.ui.pushButtonStopTimer.clicked.connect(self.onPushButtonStopClicked)

        self.ui.pushButtonUrlCheckStart.clicked.connect(self.onPushButtonUrlCheckStart)
        self.ui.pushButtonUrlCheckStop.clicked.connect(self.onPushButtonUrlCheckStop)


    def onPushButtonStartClicked(self):
        try:
            self.timerThread.timeCount = self.ui.spinBoxTimerCount.value()
            self.timerThread.start()
        except ValueError:
            self.ui.spinBoxTimerCount.setValue(0)
            QtWidgets.QMessageBox.warning(self, 'Ошибка!', 'Таймер поддерживает только целочисленные значения')

    def onPushButtonStopClicked(self):
        self.timerThread.status = False
        QtWidgets.QMessageBox.about(self, 'Завершено', 'Отсчет окончен')


    def onPushButtonUrlCheckStart(self):
        self.urlThread.setUrl(self.ui.lineEditURL.text())
        self.urlThread.setTimer(self.ui.spinBoxUrlCheckTime.value())
        self.urlThread.start()

    def onPushButtonUrlCheckStop(self):
        self.urlThread.status = False
        QtWidgets.QMessageBox.about(self, 'Завершено', 'Проверка окончена')


# Thread slots timer

    def timerThreadStarted(self):
        self.ui.pushButtonStartTimer.setEnabled(False)
        self.ui.pushButtonStopTimer.setEnabled(True)
        self.ui.spinBoxTimerCount.setEnabled(False)

    def timerThreadFinished(self):
        self.ui.pushButtonStartTimer.setEnabled(True)
        self.ui.pushButtonStopTimer.setEnabled(False)
        self.ui.spinBoxTimerCount.setEnabled(True)
        self.ui.spinBoxTimerCount.setValue(0)
        self.ui.lineEditTimerEnd.setText('0')
        QtWidgets.QMessageBox.about(self, 'Успешно', 'Отсчет закончен')

    def timerThreadTimersignal(self, emit_value):
        self.ui.lineEditTimerEnd.setText(str(emit_value))

# Thread slots url

    def checkUrlThreadUrlSignal(self, emit_value):
        self.ui.plainTextEditUrlCheckLog.setPlainText(f'{time.ctime()}: статус код {emit_value}')


class TimerThread(QtCore.QThread):
    timerSignal = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timeCount = None

    def run(self):
        self.status = True

        while self.status:
            if self.timeCount < 1:
                break
            time.sleep(1)
            self.timeCount -= 1
            self.timerSignal.emit(self.timeCount)


class CheckUrlThread(QtCore.QThread):
    urlSignal = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.url = None
        self.timer = None
        self.status = None

    def setUrl(self, url):
        self.url = url

    def setTimer(self, timer):
        self.timer = timer

    def run(self):
        self.status = True

        while self.status:
            response = requests.get(self.url)
            self.urlSignal.emit(response.status_code)
            time.sleep(self.timer)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = QThreadPractice()
    myapp.show()

    app.exec_()
