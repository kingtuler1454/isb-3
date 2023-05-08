from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox, QLabel, QFileDialog
import sys
import os

class Window(QMainWindow):

   
   
    def __init__(self) -> None:
        """"create a window object"""
        super(Window, self).__init__()
        self.label_bob = QLabel(self)
        self.label_bob.move(445, 60)
        self.label_bob.setText("Hello, my name is Bob and i your helper\nPlease,chose:\n1)GenKeys\n2)Encryption\n3)Decryption")
        self.label_bob.setFont(QFont('Times', 10))
        
        self.label_bob.adjustSize()
        

def application() -> None:
    """"Start aplication mainwindow"""
    app = QApplication(sys.argv)
    window = Window()
    window.setObjectName("MainWindow")

    window.setWindowIcon(QtGui.QIcon('phon.jpg'))
    window.setMinimumSize(800,600)
    window.setMaximumSize(800,600)
    window.setWindowTitle("Номенклатура")

    window.setStyleSheet("#MainWindow{border-image:url(phon.jpg)}")  # 3e753b

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    application()