# ###1. Генерация ключей гибридной системы
# *Входные параметры:*  
# *1) путь, по которому сериализовать зашифрованный симметричный ключ;*  
# *2) путь, по которому сериализовать открытый ключ;*  
# *3) путь, по которому сериазизовать закрытый ключ.*

# 1.1. Сгеренировать ключ для симметричного алгоритма.  
# 1.2. Сгенерировать ключи для ассиметричного алгоритма.  
# 1.3. Сериализовать ассиметричные ключи.   
# 1.4. Зашифровать ключ симметричного шифрования открытым ключом и сохранить по указанному пути. 

# ###2. Шифрование данных гибридной системой
# *Входные параметры:*  
# *1) путь к шифруемому текстовому файлу (очевидно, что файл должен быть достаточно объемным);*  
# *2) путь к закрытому ключу ассиметричного алгоритма;*  
# *3) путь к зашированному ключу симметричного алгоритма;*  
# *4) путь, по которому сохранить зашифрованный текстовый файл;*  

# 2.1. Расшифровать симметричный ключ.  
# 2.2. Зашифровать текст симметричным алгоритмом и сохранить по указанному пути.   

# ###3. Дешифрование данных гибридной системой
# *Входные парметры:*  
# *1) путь к зашифрованному текстовому файлу;*  
# *2) путь к закрытому ключу ассиметричного алгоритма;*  
# *3) путь к зашированному ключу симметричного алгоритма;*  
# *4) путь, по которому сохранить расшифрованный текстовый файл.*  

# 3.1. Расшифровать симметричный ключ.  
# 3.2. Расшифровать текст симметричным алгоритмом и сохранить по указанному пути. 


import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def key_generation_func(symmetric_key_path: str, public_key_path: str, secret_key_path: str) -> None:
    # :param symmetric_key_path:  путь, по которому сериализовать зашифрованный симметричный ключ
    # :param public_key_path: путь, по которому сериализовать открытый ключ
    # :param secret_key_path: путь, по которому сериализовать закрытый ключ

        # генерация ключа симметричного алгоритма шифрования
        symmetric_key = os.urandom(16)

        # генерация пары ключей для асимметричного алгоритма шифрования
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()
         # сериализация открытого ключа в файл
        public_pem = public_key_path + '\\key.pem'
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))

        # сериализация закрытого ключа в файл
        private_pem = secret_key_path + '\\key.pem'
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))

        # шифрование симметричного ключа открытым ключом при помощи RSA-OAEP
        encrypted_symmetric_key = public_key.encrypt(symmetric_key,
                                                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                algorithm=hashes.SHA256(),
                                                                label=None))

        # сериализация ключа симмеричного алгоритма в файл
        symmetric_file = symmetric_key_path + '\\key.txt'
        with open(symmetric_file, 'wb') as key_file:
            key_file.write(encrypted_symmetric_key)


