import os
import yaml
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Chipher:
    """Класс для шифрования дешифрования файлов"""

    def __init__(self, public_key, symmetric_key, private_key) -> None:
        """Инициализация элемента, на вход берем открытый ключ ключ симметричного щифрования и приватный ключ"""
        self.public_key = public_key
        self.symmetric_key = symmetric_key
        self.private_key = private_key

    def encrypted_symmetric_key(self) -> str:
        """шифрование симметричного ключа открытым ключом при помощи RSA-OAEP, вернёт encrypted_symmetric_key"""
        return self.public_key.encrypt(
            self.symmetric_key,
            self.padding.OAEP(
                mgf=self.padding.MGF1(algorithm=self.hashes.SHA256()),
                algorithm=self.hashes.SHA256(),
                label=None,
            ),
        )

    def decrypted_symmetric_key(self) -> str:
        """дешифрование симметричного ключа асимметричным алгоритмом вернёт d_symmetric_key"""
        return self.private_key.decrypt(
            str(self.encrypted_symmetric_key),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

    def encrypted_text_symmetric_algorithm(
        self, d_symmetric_key, padded_text, encrypted_file_path
    ) -> None:
        """шифрование текста симметричным алгоритмом, ничего не вернёт"""
        iv = os.urandom(int(int(self.bit) / 8))
        cipher = Cipher(algorithms.AES(d_symmetric_key), modes.CBC(iv))
        encryptor = cipher.ezncryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        dict_t = {"text": c_text, "iv": iv}
        encrypted_file = encrypted_file_path + "\\secret_text.yaml"
        with open(encrypted_file, "w") as _file:
            yaml.dump(dict_t, _file)

    def decrypted_text(
        self, d_symmetric_key, padded_text, encrypted_file_path, content_encrypted
    ) -> str:
        """дешифрование текста"""
        text_enc = content_encrypted["text"]
        iv_enc = content_encrypted["iv"]
        cipher = Cipher(algorithms.AES(self.symmetric_key), modes.CBC(iv_enc))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(text_enc) + decryptor.finalize()
        return dc_text
