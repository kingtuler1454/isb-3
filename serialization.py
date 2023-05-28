from cryptography.hazmat.primitives.serialization import load_pem_private_key,load_pem_public_key
from cryptography.hazmat.primitives import serialization 
import os
import yaml

    

    

class Serialization:
    def __init__(self,public_key,privat_key,encrypted_symmetric_key) -> None:
        self.name_public_key='\\public_key.pem'
        self.name_private_key='\\private_key.pem'
        self.name_sym_key='\\sym_key.txt'
        self.name_secret_text='\\secret_text.yaml'
        self.public_key=public_key
        self.privat_key=privat_key
        self.encrypted_symmetric_key=encrypted_symmetric_key


    def serialiaztion_public_key(self,public_key_path):
        """сериализация открытого ключа в файл"""
        public_pem=public_key_path +  self.name_public_key
        with open(public_pem, 'wb') as public_out:
            public_out.write(self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
  

    def serialization_private_key(self,secret_key_path):
        """сериализация закрытого ключа в файл"""
        private_pem = secret_key_path + self.name_private_key
        with open(private_pem, 'wb',) as private_out:
            private_out.write(self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
    
    
    def serialization_sum_key(self,symmetric_key_path):
        """сериализация ключа симмеричного алгоритма в файл"""
        symmetric_file = symmetric_key_path + self.name_sym_key
        with open(symmetric_file, 'wb') as key_file:
            key_file.write(self.encrypted_symmetric_key)   


    def deserialization_sym_key(self,symmetric_key_path):
        """десериализация симметричного ключа в файл"""
        symmetric_file =symmetric_key_path + self.name_sym_key
        with open(symmetric_file, mode='rb') as key_file:
            public_key= key_file.read()
        return public_key


    def deserialization_private_key(self,secret_key_path):
        """десериализация закрытого ключа в файл"""
        private_pem = secret_key_path + self.name_private_key
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        private_key = load_pem_private_key(private_bytes, password=None)
        return private_key


    def deserialization_public_key(self,public_key_path):
        """ десериализация открытого ключа"""
        public_pem=public_key_path +  self.name_public_key
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
        d_public_key = load_pem_public_key(public_bytes)


    def deserialization_shipher_file(self, encrypted_file_path ):
        """десериализация шифрованного файла"""
        encrypted_file = encrypted_file_path +self.name_secret_text
        with open(encrypted_file) as _file:
            content_encrypted = yaml.safe_load(_file)
        return content_encrypted
