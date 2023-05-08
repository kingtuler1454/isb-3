# ###1. Генерация ключей гибридной системы SM4, длина ключа 128 бит;


import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


# 1.1. Сгеренировать ключ для симметричного алгоритма.  
# 1.2. Сгенерировать ключи для ассиметричного алгоритма.  
# 1.3. Сериализовать ассиметричные ключи.   
# 1.4. Зашифровать ключ симметричного шифрования открытым ключом и сохранить по указанному пути. 


def key_generation_func(symmetric_key_path: str, public_key_path: str, secret_key_path: str) -> None:
    # :param symmetric_key_path:  путь, по которому сериализовать зашифрованный симметричный ключ
    # :param public_key_path: путь, по которому сериализовать открытый ключ
    # :param secret_key_path: путь, по которому сериализовать закрытый ключ

       
        symmetric_key = os.urandom(16)  # 1.1 генерация ключа симметричного алгоритма шифрования
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        ) # 1.2 генерация пары ключей для асимметричного алгоритма шифрования
        private_key = keys
        public_key = keys.public_key()
         # 1.3 сериализация открытого ключа в файл
        public_pem = public_key_path + '\\key.pem'
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))

        # 1.3 сериализация закрытого ключа в файл
        private_pem = secret_key_path + '\\key.pem'
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))

        #1.4 шифрование симметричного ключа открытым ключом при помощи RSA-OAEP
        encrypted_symmetric_key = public_key.encrypt(symmetric_key,
                                                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                algorithm=hashes.SHA256(),
                                                                label=None))

        #1.4  сериализация ключа симмеричного алгоритма в файл
        symmetric_file = symmetric_key_path + '\\key.txt'
        with open(symmetric_file, 'wb') as key_file:
            key_file.write(encrypted_symmetric_key)


