from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox, QLabel, QFileDialog, QInputDialog
import os
import sys
from Key_generation import Key_generation
from serialization import Serialization
class Window(QMainWindow):

    def hide_field(self):
        self.field_first.hide()
        self.field_second.hide()
        self.field_third.hide()
        self.field_fourth.hide()
        self.button_OK.hide()
        self.button_first_field.hide()
        self.button_second_field.hide()
        self.button_third_field.hide()
        self.button_fourth_field.hide()


    def set_design(self):
        self.label_bob.setText("Hello, my name is Bob and i your helper\nPlease,chose:\n1)GenKeys\n2)Encryption\n3)Decryption")
        self.button_task1.setText("1)GenKeys")
        self.button_task2.setText("2)Encryption")
        self.button_task3.setText("2)Decryption")
        self.button_first_field.setText("Choose")
        self.button_second_field.setText("Choose")
        self.button_third_field.setText("Choose")
        self.button_fourth_field.setText("Choose")
        self.button_OK.setText("OK")

        self.field_first.setFixedSize(150,20)
        self.field_second.setFixedSize(150,20)
        self.field_third.setFixedSize(150,20)
        self.field_fourth.setFixedSize(150,20)
        self.label_bob.setFont(QFont('Times', 10))
        self.label_bob.move(445, 58)
        self.button_task1.move(445, 150) 
        self.button_task2.move(525, 150) 
        self.button_task3.move(605, 150) 
        self.field_first.move(445, 72) 
        self.field_second.move(445, 95) 
        self.field_third.move(445, 118) 
        self.field_fourth.move(445, 141) 
        self.button_first_field.move(600,72)
        self.button_second_field.move(600,95)
        self.button_third_field.move(600,118)
        self.button_fourth_field.move(600,141)       
        self.button_OK.move(520,165)
        self.label_bob.adjustSize()
        self.button_task1.adjustSize()
        self.button_task2.adjustSize()
        self.button_task3.adjustSize()
        self.button_first_field.adjustSize()
        self.button_second_field.adjustSize()
        self.button_third_field.adjustSize()
        self.button_fourth_field.adjustSize()
        self.button_OK.adjustSize()


    def button_field_click(self, number:int):
        self.array_field[number]=QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")

    # 1   if  number==0:    self.field_third.setText(self.array_field[number])
    #     elif number==2:    self.field_third.setText(self.array_field[number])
    #     elif number==3:    self.field_third.setText(self.array_field[number])
    #     elif number==4:    self.field_third.setText(self.array_field[number])
        

    def button_task1_click(self):
        
        Object_genkey= Key_generation(self.bit)
        symmetric_key=Object_genkey.generation_key_symmetric()
        private_key=Object_genkey.generation_private_key()
        public_key=Object_genkey.generation_public_key(private_key)
        Object_serialization=Serialization( public_key,private_key,symmetric_key)
        try:
            Object_serialization.serialiaztion_public_key( self.array_path_field[0])
            Object_serialization.serialization_private_key( self.array_path_field[1])
            Object_serialization.serialization_sum_key( self.array_path_field[2])
        except FileNotFoundError :
             QMessageBox.about(self, "Внимание", "Проверьте введённые данные")
 





    def __init__(self) -> None:
        """"create a window object"""
        super(Window, self).__init__()
        self.label_bob = QLabel(self)
        self.button_task1 = QtWidgets.QPushButton(self)
        self.button_task2 = QtWidgets.QPushButton(self)
        self.button_task3 = QtWidgets.QPushButton(self)
        self.button_first_field=QtWidgets.QPushButton(self)
        self.button_second_field=QtWidgets.QPushButton(self)
        self.button_third_field=QtWidgets.QPushButton(self)
        self.button_fourth_field=QtWidgets.QPushButton(self)
        self.button_OK=QtWidgets.QPushButton(self)

        self.field_first = QtWidgets.QLineEdit(self)
        self.field_second = QtWidgets.QLineEdit(self)
        self.field_third = QtWidgets.QLineEdit(self)
        self.field_fourth = QtWidgets.QLineEdit(self)
        self.array_path_field=['','','','']
        self.chose_task=1
        
        self.hide_field()
        self.set_design()

        self.button_task1.clicked.connect(self.button_task1_click)
        self.button_first_field.clicked.connect(self.button_field_click,0)
        self.button_second_field.clicked.connect(self.button_field_click,1)
        self.button_third_field.clicked.connect(self.button_field_click,2)
        self.button_fourth_field.clicked.connect(self.button_field_click,3)
        # self.button_OK.clicked.connect(self.button_OK_click)
        # self.button_encryption.clicked.connect(self.button_encryption_click)
        # self.button_decryption.clicked.connect(self.button_decryption_click)

        self.bit='0'
        while    self.bit!='128' and self.bit!='192' and     self.bit!='256' :
            text, ok = QInputDialog.getText(self, 'Input Dialog','Enter 128 or 192 or 256 bit:')
            if ok:
                self.bit=str(text)
                print(self.bit)


def application() -> None:
    """"Start aplication mainwindow"""
    app = QApplication(sys.argv)
    window = Window()
    window.setObjectName("MainWindow")


    window.setMinimumSize(800,600)
    window.setMaximumSize(800,600)


    window.setStyleSheet("#MainWindow{border-image:url(phon.png)}")  # 3e753b

    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    application()