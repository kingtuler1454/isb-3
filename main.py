from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox, QLabel, QFileDialog
import sys
import os

class Window(QMainWindow):

    def  button_first_field_click(self):
        self.field_path_1 = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.field_first.setText(self.field_path_1)

    def  button_second_field_click(self):
        self.field_path_2 = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.field_second.setText(self.field_path_2)

    def  button_third_field_click(self):
        self.field_path_3 = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.field_third.setText(self.field_path_3)

    def button_genkey_click(self):
        self.label_bob.clear()
        self.label_bob.setText("Task 1: Generation Keys")
        self.label_bob.adjustSize()
        
        
        self.button_genkey.hide()
        self.button_encryption.hide()
        self.button_decryption.hide()
        
        self.field_first.show()
        self.field_second.show()
        self.field_third.show()
        self.button_OK.show()
        self.button_first_field.show()
        self.button_second_field.show()
        self.button_third_field.show()
        
        
        self.field_first.setPlaceholderText("Path for encrypted key")
        self.field_second.setPlaceholderText("Path for public key")
        self.field_third.setPlaceholderText("Path for private key")
   
   
    def __init__(self) -> None:
        """"create a window object"""
        super(Window, self).__init__()
        self.label_bob = QLabel(self)
        self.button_genkey = QtWidgets.QPushButton(self)
        self.button_encryption = QtWidgets.QPushButton(self)
        self.button_decryption = QtWidgets.QPushButton(self)
        self.button_first_field=QtWidgets.QPushButton(self)
        self.button_second_field=QtWidgets.QPushButton(self)
        self.button_third_field=QtWidgets.QPushButton(self)
        self.button_OK=QtWidgets.QPushButton(self)
        self.field_first = QtWidgets.QLineEdit(self)
        self.field_second = QtWidgets.QLineEdit(self)
        self.field_third = QtWidgets.QLineEdit(self)
        
        
        self.field_first.hide()
        self.field_second.hide()
        self.field_third.hide()
        self.button_OK.hide()
        self.button_first_field.hide()
        self.button_second_field.hide()
        self.button_third_field.hide()
        
        self.label_bob.setText("Hello, my name is Bob and i your helper\nPlease,chose:\n1)GenKeys\n2)Encryption\n3)Decryption")
        self.button_genkey.setText("1)GenKeys")
        self.button_encryption.setText("2)Encryption")
        self.button_decryption.setText("2)Decryption")
        self.button_first_field.setText("Choose")
        self.button_second_field.setText("Choose")
        self.button_third_field.setText("Choose")
        self.button_OK.setText("OK")
        
        
       
       
        self.field_first.setFixedSize(150,20)
        self.field_second.setFixedSize(150,20)
        self.field_third.setFixedSize(150,20)
        
        self.label_bob.setFont(QFont('Times', 10))
        

        self.label_bob.move(445, 58)
        self.button_genkey.move(445, 150) 
        self.button_encryption.move(525, 150) 
        self.button_decryption.move(605, 150) 
        self.field_first.move(445, 72) 
        self.field_second.move(445, 95) 
        self.field_third.move(445, 118) 
        self.button_first_field.move(600,72)
        self.button_second_field.move(600,95)
        self.button_third_field.move(600,118)
        self.button_OK.move(520,150)
        
        self.label_bob.adjustSize()
        self.button_genkey.adjustSize()
        self.button_encryption.adjustSize()
        self.button_decryption.adjustSize()
        self.button_first_field.adjustSize()
        self.button_second_field.adjustSize()
        self.button_third_field.adjustSize()
        self.button_OK.adjustSize()
        
        
        self.button_genkey.clicked.connect(self.button_genkey_click)
        self.button_first_field.clicked.connect(self.button_first_field_click)
        self.button_second_field.clicked.connect(self.button_second_field_click)
        self.button_third_field.clicked.connect(self.button_third_field_click)
        
        
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