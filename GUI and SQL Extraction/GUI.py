import sys
from PyQt5.QtWidgets import*
from PyQt5 import QtCore
from ITS import querySql

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

        #Create combobox
        self.combobox = QComboBox(self)

        item_list = ["Select Chapter", "Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Chapter 6",
                     "Chapter 7", "Chapter 8", "Chapter 9", "Chapter 10", "Chapter 11", "Chapter 12"]
        self.combobox.addItems(item_list)

        self.combobox.move(20,20)
        self.combobox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Continue', self)
        self.button.move(20, 80)

        self.button.clicked.connect(self.clicked)
        self.show()

        #Closing Question Window
        self.Qwin = Window2()
        self.Qwin.close()

    # Show question when the button is clicked
    def clicked(self):
        content = self.combobox.currentText()
        self.Qwindow(content)


    def Qwindow(self, content):
        self.Qwin = Window2()

        # Create a button in question Window
        self.Qwin.button1 = QPushButton('Back to chapter select', self.Qwin)
        self.Qwin.button1.resize(200, 40)
        self.Qwin.button1.move(20, 250)

        self.Qwin.Label = QLabel(querySql(content))
        self.Qwin.label.setAlignment(QtCore.Qt.AlignCenter)

        # button1 goes back to main window
        self.Qwin.button1.clicked.connect(self.initUI)
        self.Qwin.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())