from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QFont, QPixmap
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QMessageBox,
    QLabel,
    QFileDialog,
    QInputDialog,
)
import os
import sys

from key_generation import Key_generation
from serialization import Serialization
from deserialization import Deserialization
from chipher import Chipher
from padding import Padding


class Window(QMainWindow):
    """Класс для создания графического интерфейса"""

    def hide_field(self) -> None:
        """Скрывает колонки и кнопки для прописи файлов"""
        self.field_first.hide()
        self.field_second.hide()
        self.field_third.hide()
        self.field_fourth.hide()
        self.button_OK.hide()
        self.button_first_field.hide()
        self.button_second_field.hide()
        self.button_third_field.hide()
        self.button_fourth_field.hide()

    def show_field(self) -> None:
        """Показывает колонки и кнопки для прописи файлов"""
        self.field_first.show()
        self.field_second.show()
        self.field_third.show()
        self.button_OK.show()
        self.button_first_field.show()
        self.button_second_field.show()
        self.button_third_field.show()
        if self.chose_task != 1:
            self.field_fourth.show()
            self.button_fourth_field.show()

    def hide_menu(self) -> None:
        """прячет меню основных заданий"""
        self.button_task1.hide()
        self.button_task2.hide()
        self.button_task3.hide()

    def show_menu(self):
        """показывает меню основных заданий"""
        self.button_task1.show()
        self.button_task2.show()
        self.button_task3.show()
        self.label_bob.clear()
        self.label_bob.setText(
            "Hello, my name is Bob and i your helper\nPlease,chose:\n1)GenKeys\n2)Encryption\n3)Decryption"
        )
        self.label_bob.adjustSize()

    def set_design(self) -> None:
        """устанавливает основной дизайн"""
        self.label_bob.setText(
            "Hello, my name is Bob and i your helper\nPlease,chose:\n1)GenKeys\n2)Encryption\n3)Decryption"
        )
        self.button_task1.setText("1)GenKeys")
        self.button_task2.setText("2)Encryption")
        self.button_task3.setText("2)Decryption")
        self.button_first_field.setText("Choose")
        self.button_second_field.setText("Choose")
        self.button_third_field.setText("Choose")
        self.button_fourth_field.setText("Choose")
        self.button_OK.setText("OK")
        self.field_first.setFixedSize(150, 20)
        self.field_second.setFixedSize(150, 20)
        self.field_third.setFixedSize(150, 20)
        self.field_fourth.setFixedSize(150, 20)
        self.label_bob.setFont(QFont("Times", 10))
        self.label_bob.move(445, 58)
        self.button_task1.move(445, 150)
        self.button_task2.move(525, 150)
        self.button_task3.move(605, 150)
        self.field_first.move(445, 72)
        self.field_second.move(445, 95)
        self.field_third.move(445, 118)
        self.field_fourth.move(445, 141)
        self.button_first_field.move(600, 72)
        self.button_second_field.move(600, 95)
        self.button_third_field.move(600, 118)
        self.button_fourth_field.move(600, 141)
        self.button_OK.move(520, 165)
        self.label_bob.adjustSize()
        self.button_task1.adjustSize()
        self.button_task2.adjustSize()
        self.button_task3.adjustSize()
        self.button_first_field.adjustSize()
        self.button_second_field.adjustSize()
        self.button_third_field.adjustSize()
        self.button_fourth_field.adjustSize()
        self.button_OK.adjustSize()

    def button_field_click1(self, number: int):
        self.field_first.clear()
        self.path_field1 = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.field_first.setText(self.path_field1)
        self.field_first.adjustSize()

    def button_field_click2(self, number: int):
        self.field_second.clear()
        self.path_field2 = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.field_second.setText(self.path_field2)
        self.field_second.adjustSize()

    def button_field_click3(self, number: int):
        self.field_third.clear()
        self.path_third = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.field_third.setText(self.path_field3)
        self.field_third.adjustSize()

    def button_field_click4(self, number: int):
        self.field_fourth.clear()
        self.path_field4 = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        self.field_fourth.setText(self.path_field4)
        self.field_fourth.adjustSize()

    def button_OK_click(self) -> None:
        """Функция которая создаёт объекты из дугих классов в зависимости от выбранного задания"""
        if self.chose_task == 1:
            Object_genkey = Key_generation(self.bit)
            symmetric_key = Object_genkey.generation_key_symmetric()
            private_key = Object_genkey.generation_private_key()
            public_key = Object_genkey.generation_public_key(private_key)
            Object_serialization = Serialization(public_key, private_key, symmetric_key)
            try:
                Object_serialization.serialiaztion_public_key(self.path_field1)
                Object_serialization.serialization_private_key(self.path_field2)
                Object_serialization.serialization_sum_key(self.path_field3)
            except FileNotFoundError:
                QMessageBox.about(self, "Внимание", "Проверьте введённые данные")
        elif self.chose_task == 2:
            Object_deserialization = Deserialization()
            try:
                symmetric_key = Object_deserialization.deserialization_sym_key(
                    self.path_field3
                )
                private_key = Object_deserialization.deserialization_private_key(
                    self.path_field2
                )
                public_key = private_key.public_key()
                Object_chipher = Chipher(public_key, symmetric_key, private_key)
                d_symmetric_key = Object_chipher.decrypted_symmetric_key()
                Object_padding = Padding(self.path_field1, self.bit)
                padded_text = Object_padding.padding()
                Object_chipher.encrypted_text_symmetric_algorithm(
                    d_symmetric_key, padded_text, self.path_field4
                )
            except FileNotFoundError:
                QMessageBox.about(self, "Внимание", "Проверьте введённые данные")
        else:
            Object_deserialization = Deserialization()
            symmetric_key = Object_deserialization.deserialization_sym_key(
                str(self.field_third.text())
            )
            private_key = Object_deserialization.deserialization_private_key(
                str(self.field_second.text())
            )
            public_key = private_key.public_key()
            Object_chipher = Chipher(public_key, symmetric_key, private_key)
            d_symmetric_key = Object_chipher.decrypted_symmetric_key()
            content_encrypted = Object_deserialization.deserialization_shipher_file()
            dc_text = Object_chipher.decrypted_text()
            Object_padding = Padding(str(self.field_first.text()), self.bit)
            Object_padding.depadding(dc_text, str(self.field_fourth.text()))
        QMessageBox.about(self, "Внимание", "Успешно")
        self.field_first.clear()
        self.field_second.clear()
        self.field_third.clear()
        self.field_fourth.clear()
        self.hide_field()
        self.show_menu()

    def button_task1_click(self) -> None:
        """функция которая выводит информацию для работы задания 1"""
        self.chose_task = 1
        self.show_field()
        self.hide_menu()
        self.label_bob.clear()
        self.label_bob.setText("Task 1: Generation Keys")
        self.label_bob.adjustSize()
        self.field_first.setPlaceholderText("public_key_path")
        self.field_second.setPlaceholderText("private_key_path")
        self.field_third.setPlaceholderText("symmetric_key_path")

    def button_task2_click(self) -> None:
        """функция которая выводит информацию для работы задания 2"""
        self.chose_task = 2
        self.show_field()
        self.hide_menu()
        self.label_bob.clear()
        self.label_bob.setText("Task 2: Encrypt data")
        self.label_bob.adjustSize()
        self.field_first.setPlaceholderText("initial_file_path")
        self.field_second.setPlaceholderText("secret_key_path")
        self.field_third.setPlaceholderText("symmetric_key_path")
        self.field_fourth.setPlaceholderText("encrypted_file_path")

    def button_task3_click(self) -> None:
        """функция которая выводит информацию для работы задания 3"""
        self.chose_task = 3
        self.show_field()
        self.hide_menu()
        self.label_bob.clear()
        self.label_bob.setText("Task 3: Decrypt data")
        self.label_bob.adjustSize()
        self.field_first.setPlaceholderText("encrypted_file_path")
        self.field_second.setPlaceholderText("private_key_path")
        self.field_third.setPlaceholderText("symmetric_key_path")
        self.field_fourth.setPlaceholderText("decrypted_file_path")

    def __init__(self) -> None:
        """ "create a window object"""
        super(Window, self).__init__()
        self.label_bob = QLabel(self)
        self.button_task1 = QtWidgets.QPushButton(self)
        self.button_task2 = QtWidgets.QPushButton(self)
        self.button_task3 = QtWidgets.QPushButton(self)
        self.button_first_field = QtWidgets.QPushButton(self)
        self.button_second_field = QtWidgets.QPushButton(self)
        self.button_third_field = QtWidgets.QPushButton(self)
        self.button_fourth_field = QtWidgets.QPushButton(self)
        self.button_OK = QtWidgets.QPushButton(self)
        self.field_first = QtWidgets.QLineEdit(self)
        self.field_second = QtWidgets.QLineEdit(self)
        self.field_third = QtWidgets.QLineEdit(self)
        self.field_fourth = QtWidgets.QLineEdit(self)
        self.path_field1 = (
            self.path_field2
        ) = self.path_field3 = self.path_field4 = os.getcwd()
        self.chose_task = 1
        self.hide_field()
        self.set_design()
        self.button_task1.clicked.connect(self.button_task1_click)
        self.button_task2.clicked.connect(self.button_task2_click)
        self.button_task3.clicked.connect(self.button_task3_click)
        self.button_first_field.clicked.connect(self.button_field_click1)
        self.button_second_field.clicked.connect(self.button_field_click2)
        self.button_third_field.clicked.connect(self.button_field_click3)
        self.button_fourth_field.clicked.connect(self.button_field_click4)
        self.button_OK.clicked.connect(self.button_OK_click)
        self.bit = "0"
        while self.bit != "128" and self.bit != "192" and self.bit != "256":
            text, ok = QInputDialog.getText(
                self, "Input Dialog", "Enter 128 or 192 or 256 bit:"
            )
            if ok:
                self.bit = text
        self.bit = int(int(text) / 8)