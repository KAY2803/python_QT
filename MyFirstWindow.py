import sys

from PySide2 import QtWidgets

class MyFirstWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self):

        main_layout = QtWidgets.QVBoxLayout()

        btn = QtWidgets.QPushButton("Кнопка")
        lbl = QtWidgets.QLabel("Текст")
        main_layout.addWidget(btn)
        main_layout.addWidget(lbl)

        self.setLayout(main_layout)

        # bin = QtWidgets.QPushButton("Кнопка")
        # bin.setText("Кнопка")
        # bin.move(30, 30)

# MAINWINDOW
# class MyWidgets(QtWidgets.QMainWindow):
#
#     def __init__(self, parent=None)
#         super().__init__(parent)
#
#         self.fileMenu = self.MenuBar().addMenu('File')
#         self.fileMenu.addAction('Open')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyFirstWindow()
    myWindow.show()

    sys.exit(app.exec_())