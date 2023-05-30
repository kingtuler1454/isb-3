from cryptography.hazmat.primitives.asymmetric import rsa
import os


class Key_generation:
    def __init__(self, bit) -> None:
        """генерация ключа симметричного алгоритма шифрования"""
        self.bit = bit

    def generation_key_symmetric(self) -> bytes:
        """генерация ключа симметричного алгоритма шифрования"""
        return os.urandom(self.bit)

    def generation_private_key(self):
        """генерация пары ключей для асимметричного алгоритма шифрования или приватный ключ"""
        return rsa.generate_private_key(public_exponent=65537, key_size=2048)

    def generation_public_key(self, keys):
        """генерация открытого ключа"""
        return keys.public_key()
