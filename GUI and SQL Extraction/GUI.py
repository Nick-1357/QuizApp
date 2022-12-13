import sys
import re
from io import BytesIO

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import *
# import matplotlib as mpl
# from fontTools.subset import svg
# from matplotlib import pyplot as plt
# from matplotlib.backends.backend_agg import FigureCanvasAgg
from PyQt5 import QtCore, QtGui
from ITS import (querySql, addUser)


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login Form')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        addUser(self.lineEdit_username, self.lineEdit_password)
        self.setLayout(layout)

    def check_password(self):
        self.app = App()
        self.app.initUI()
        self.close()


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Question Finder'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 130
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create combobox
        self.combobox = QComboBox(self)

        item_list = ["Select Chapter", "Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Chapter 6",
                     "Chapter 7", "Chapter 8", "Chapter 9", "Chapter 10", "Chapter 11", "Chapter 12"]
        self.combobox.addItems(item_list)

        self.combobox.move(20, 20)
        self.combobox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Continue', self)
        self.button.move(20, 80)

        self.button.clicked.connect(self.clicked)
        self.show()

        # Closing Question Window
        self.Qwin = Window2()
        self.Qwin.close()

    # Show question when the button is clicked
    def clicked(self):
        content = self.combobox.currentText()
        self.Qwin.Qwindow(content)


class Window2(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Question Window'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def Qwindow(self, content):
        # Create a button in question Window
        self.button1 = QPushButton('Back to chapter select', self)
        self.button1.resize(200, 40)
        self.button1.move(20, 250)

        # Show the question as a label in the window
        text = querySql(content)
        self.label = QLabel(text, self)
        self.label.adjustSize()
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # button1 goes back to main window
        self.app = App()
        self.button1.clicked.connect(self.app.initUI)
        self.show()
        self.app.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginForm()
    ex.show()

    sys.exit(app.exec_())
