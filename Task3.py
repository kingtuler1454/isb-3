import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives import padding as padding2
import yaml


def decrypting_data(encrypted_file_path: str, secret_key_path: str, symmetric_key_path: str,
                    decrypted_file_path: str) -> None:
    
    # :param encrypted_file_path: путь к зашифрованному текстовому файлу
    # :param secret_key_path: путь к закрытому ключу ассиметричного алгоритма
    # :param symmetric_key_path: путь к зашифрованному ключу симметричного алгоритма
    # :param decrypted_file_path: путь, по которому сохранить расшифрованный текстовый файл
    # :return: ничего не возвращает


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
    dsymmetric_key = private_key.decrypt(encrypted_symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
      
    # десериализация шифрованного файла
    encrypted_file = encrypted_file_path + '\\file.yaml'
    with open(encrypted_file) as _file:
        content_encrypted = yaml.safe_load(_file)

    text_enc = content_encrypted["text"]
    iv_enc = content_encrypted["iv"]

    # дешифрование и депаддинг текста симметричным алгоритмом
    cipher = Cipher(algorithms.IDEA(dsymmetric_key), modes.CBC(iv_enc))
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(text_enc) + decryptor.finalize()

    unpadder = padding2.ANSIX923(64).unpadder()
    unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

    decrypted_file = decrypted_file_path + '\\file.txt'
    with open(decrypted_file, 'w') as _file:
        _file.write(str(unpadded_dc_text))