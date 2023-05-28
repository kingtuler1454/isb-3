  # 1.4a шифрование симметричного ключа открытым ключом при помощи RSA-OAEP1
    # 2.3 дешифрование симметричного ключа асимметричным алгоритмом1
    # 2.5  # шифрование текста симметричным алгоритмом 
    # дешифрование  текста симметричным алгоритмом
  
    #  депаддинг данных для работы блочного шифра
    # 2.4 паддинг данных для работы блочного шифра (делаем длину сообщения кратной длине шифруемого блока --------------------- (64 бита))
import os   
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
class Chipher:
    def __init__(self,public_key,symmetric_key,padding,hashes) -> None:
        self.public_key=public_key
        self.symmetric_key=symmetric_key
        self.padding=padding
        self.hashes=hashes

    def encrypted_symmetric_key(self)->str:
         """шифрование симметричного ключа открытым ключом при помощи RSA-OAEP, вернёт encrypted_symmetric_key"""
         return self.public_key.encrypt(self.symmetric_key,self.padding.OAEP(mgf=self.padding.MGF1(algorithm=self.hashes.SHA256()),
                                                                algorithm=self.hashes.SHA256(),
                                                                label=None))
    def decrypted_symmetric_key(self):
         """дешифрование симметричного ключа асимметричным алгоритмом вернёт d_symmetric_key"""
         return self.private_key.decrypt(self.encrypted_symmetric_key, self.padding.OAEP(mgf=self.padding.MGF1(algorithm=self.hashes.SHA256()), algorithm=self.hashes.SHA256(), label=None))


    def encrypted_text_symmetric_algorithm(self,d_symmetric_key,added_tex):
        """шифрование текста симметричным алгоритмом"""
        iv = os.urandom(int(int(self.bit)/8))
        cipher = Cipher(algorithms.AES(d_symmetric_key), modes.CBC(iv))
        encryptor = cipher.ezncryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()


