#Входные параметры:
#1) путь к шифруемому текстовому файлу (очевидно, что файл должен быть достаточно объемным);
#2) путь к закрытому ключу ассиметричного алгоритма;
#3) путь к зашированному ключу симметричного алгоритма;
#4) путь, по которому сохранить зашифрованный текстовый файл;

#2.1. Расшифровать симметричный ключ.
#2.2. Зашифровать текст симметричным алгоритмом и сохранить по указанному пути.

import os
import argparse
#import algorithms
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives import padding as padding2
import yaml
from Task1 import key_generation_func

def encrypt_data(initial_file_path: str, secret_key_path: str, symmetric_key_path: str, encrypted_file_path: str) -> None:
    # :param initial_file_path: путь к шифруемому текстовому файлу
    # :param secret_key_path: путь к закрытому ключу ассиметричного алгоритма
    # :param symmetric_key_path: путь к зашифрованному ключу симметричного алгоритма
    # :param encrypted_file_path: путь, по которому сохранить зашифрованный текстовый файл
   

    # десериализация ключа симметричного алгоритма
    symmetric_file = symmetric_key_path + '\\key.txt'
    with open(symmetric_file, mode='rb') as key_file:
        encrypted_symmetric_key = key_file.read()

    # десериализация закрытого ключа
    private_pem = secret_key_path + '\\key.pem'
    with open(private_pem, 'rb') as pem_in:
        private_bytes = pem_in.read()
    private_key = load_pem_private_key(private_bytes, password=None)

     # дешифрование симметричного ключа асимметричным алгоритмом
    d_symmetric_key = private_key.decrypt(encrypted_symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

     # паддинг данных для работы блочного шифра (делаем длину сообщения кратной длине шифруемого блока (64 бита))
    initial_file = initial_file_path + '\\text.txt'
    with open(initial_file, 'r') as _file:
        initial_content = _file.read()
    padder = padding2.ANSIX923(64).padder()
    text = bytes(initial_content, 'UTF-8')
    padded_text = padder.update(text) + padder.finalize()

    # шифрование текста симметричным алгоритмом
     # iv - random value for block mode initialization, must be the size of a block and new each time
    iv = os.urandom(8)
    cipher = Cipher(algorithms.IDEA(d_symmetric_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    c_text = encryptor.update(padded_text) + encryptor.finalize()

    # зашифрованный текст хранится в виде словаря, где под ключом 'text' хранится сам зашифрованный текст,
    # a 'iv' is a random value for block mode initialization, which is needed for text decoding
    dict_t = {'text': c_text, 'iv': iv}
    encrypted_file = encrypted_file_path + '\\file.yaml'
    with open(encrypted_file, 'w') as _file:
        yaml.dump(dict_t, _file)