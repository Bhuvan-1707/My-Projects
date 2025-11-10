from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(0,0,250,250)
    b.move(50,20)
    w.setWindowTitle("My first Program")
    w.show()
    sys.exit(app.exec())

def main():
    window()

main()

def window(QtWidget):
    def __init__(self,parent = QtWidget):
        super().__init__()
        self.label = QLabel(self)
        self.widget = QWidget(self)
        