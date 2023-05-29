from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
)
from cryptography.hazmat.primitives import serialization
import os
import yaml


class Serialization:
    """Класс для сериализации объектов"""

    def __init__(self, public_key, private_key, encrypted_symmetric_key) -> None:
        """Инициализация элемента, на вход берём приватный ключ, открытый ключ и ключ симм."""
        self.name_public_key = "\\public_key.pem"
        self.name_private_key = "\\private_key.pem"
        self.name_sym_key = "\\sym_key.txt"
        self.name_secret_text = "\\secret_text.yaml"
        self.public_key = public_key
        self.private_key = private_key
        self.encrypted_symmetric_key = encrypted_symmetric_key

    def serialiaztion_public_key(self, public_key_path) -> None:
        """сериализация открытого ключа в файл"""
        public_pem = public_key_path + self.name_public_key
        with open(public_pem, "wb") as public_out:
            public_out.write(
                self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )

    def serialization_private_key(self, secret_key_path) -> None:
        """сериализация закрытого ключа в файл"""
        private_pem = secret_key_path + self.name_private_key
        with open(
            private_pem,
            "wb",
        ) as private_out:
            private_out.write(
                self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )

    def serialization_sum_key(self, symmetric_key_path) -> None:
        """сериализация ключа симмеричного алгоритма в файл"""
        symmetric_file = symmetric_key_path + self.name_sym_key
        with open(symmetric_file, "wb") as key_file:
            key_file.write(self.encrypted_symmetric_key)