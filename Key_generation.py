from cryptography.hazmat.primitives.asymmetric import rsa
import os


class  Key_generation:
    def __init__(self,bit) -> None:
        self.bit=bit


    def generation_key_symmetric(self):
        """генерация ключа симметричного алгоритма шифрования"""
        return  os.urandom(int(int(self.bit)/8))


    def generation_private_key(self):
        """генерация пары ключей для асимметричного алгоритма шифрования или приватный ключ"""
        return rsa.generate_private_key(public_exponent=65537,key_size=2048 )
    
    def generation_public_key(self,keys):
        """генерация открытого ключа"""
        return keys.public_key()