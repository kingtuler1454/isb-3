from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
)
from cryptography.hazmat.primitives import serialization
import os
import yaml


class Deserialization:
    """Класс для десериализации файлов"""

    def __init__(self) -> None:
        """Инициализация элемента,для удобства пропишем окончания файлов"""
        self.name_public_key = "\\public_key.pem"
        self.name_private_key = "\\private_key.pem"
        self.name_sym_key = "\\sym_key.txt"
        self.name_secret_text = "\\secret_text.yaml"

    def deserialization_sym_key(self, symmetric_key_path: str) -> bytes:
        """Десериализация симметричного ключа в файл, на вход берём путь до ключа сим."""
        symmetric_file = symmetric_key_path + self.name_sym_key
        with open(symmetric_file, mode="rb") as key_file:
            public_key = key_file.read()
        return public_key

    def deserialization_private_key(self, secret_key_path: str) -> bytes:
        """десериализация закрытого ключа в файл, на вход берём путь до приватного ключа"""
        private_pem = secret_key_path + self.name_private_key
        with open(private_pem, "rb") as pem_in:
            private_bytes = pem_in.read()
        private_key = load_pem_private_key(private_bytes, password=None)
        return private_key

    def deserialization_public_key(self, public_key_path: str) -> bytes:
        """десериализация открытого ключа, на вход берём путь до открытого ключа"""
        public_pem = public_key_path + self.name_public_key
        with open(public_pem, "rb") as pem_in:
            public_bytes = pem_in.read()
        d_public_key = load_pem_public_key(public_bytes)
        return d_public_key

    def deserialization_shipher_file(self, encrypted_file_path: str) -> str:
        """десериализация шифрованного файла, на вход берём путь до текстового файла"""
        encrypted_file = encrypted_file_path + self.name_secret_text
        with open(encrypted_file) as _file:
            content_encrypted = yaml.safe_load(_file)
        return content_encrypted
