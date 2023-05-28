from cryptography.hazmat.primitives.serialization import load_pem_private_key, serialization
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import yaml




    # 1.1 генерация ключа симметричного алгоритма шифрования 
    # 1.2 генерация пары ключей для асимметричного алгоритма шифрования
    

    

class Serialization:
    def __init__(self,public_key_path,secret_key_path,private_key,public_key,symmetric_key_path,encrypted_symmetric_key,encrypted_file_path) -> None:
        self.public_key_path=public_key_path
        self.secret_key_path=secret_key_path
        self.private_key=private_key
        self.public_key=public_key
        self.symmetric_key_path=symmetric_key_path
        self.encrypted_symmetric_key=encrypted_symmetric_key
        self.encrypted_file_path=encrypted_file_path


    def serialiation_public_key(self):
        """сериализация открытого ключа в файл"""
        public_pem=self.public_key_path + '\\public_key.pem'
        with open(public_pem, 'wb') as public_out:
            public_out.write(self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
  

    def serialiation_private_key(self):
        """сериализация закрытого ключа в файл"""
        private_pem = self.secret_key_path + '\\private_key.pem'
        with open(private_pem, 'wb',) as private_out:
            private_out.write(self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
    
    
    def serialiation_private_key(self):
        """сериализация ключа симмеричного алгоритма в файл"""
        symmetric_file = self.symmetric_key_path + '\\sym_key.txt'
        with open(symmetric_file, 'wb') as key_file:
            key_file.write(self.encrypted_symmetric_key)   


    def deserialiation_public_key(self):
        """десериализация открытого ключа в файл"""
        symmetric_file = self.symmetric_key_path + '\\sym_key.txt'
        with open(symmetric_file, mode='rb') as key_file:
            public_key= key_file.read()
        return public_key


    def deserialiation_private_key(self):
        """десериализация закрытого ключа в файл"""
        private_pem = self.secret_key_path + '\\private_key.pem'
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        private_key = load_pem_private_key(private_bytes, password=None)
        return private_key


    def deserialiation_private_key(self):
        """десериализация ключа симмеричного алгоритма в файл"""
        symmetric_file = self.symmetric_key_path + '\\sym_key.txt'
        with open(symmetric_file, mode='rb') as key_file:
            encrypted_symmetric_key= key_file.read()
        return encrypted_symmetric_key


    def deserialization_shipher_file(self):
        # десериализация шифрованного файла
        encrypted_file = self.encrypted_file_path + '\\secret_text.yaml'
        with open(encrypted_file) as _file:
            content_encrypted = yaml.safe_load(_file)
        return content_encrypted


     

    
    

   
    
    

        
    # 1.4a шифрование симметричного ключа открытым ключом при помощи RSA-OAEP1
    # 2.3 дешифрование симметричного ключа асимметричным алгоритмом1
    # 2.5  # шифрование текста симметричным алгоритмом 
    # дешифрование  текста симметричным алгоритмом
  
    #  депаддинг данных для работы блочного шифра
    # 2.4 паддинг данных для работы блочного шифра (делаем длину сообщения кратной длине шифруемого блока --------------------- (64 бита))
    
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


    def encrypted_text_symmetric_algorithm(self):
        """шифрование текста симметричным алгоритмом"""
        iv = os.urandom(int(int(self.bit)/8))
        cipher = Cipher(algorithms.AES(d_symmetric_key), modes.CBC(iv))
        encryptor = cipher.ezncryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()


from cryptography.hazmat.primitives.asymmetric import  padding,padding2

class Padding:
    def __init__(self,initial_file_path) -> None:
      self.initial_file_path=initial_file_path
    
    def padding(self):
        """паддинг данных для работы блочного шифра (делаем длину сообщения кратной длине шифруемого блока"""
        initial_file = self.initial_file_path + '\\text.txt'
        with open(initial_file, 'r') as _file:
            initial_content = _file.read()
        padder = padding2.ANSIX923(256).padder()
        text = bytes(initial_content, 'UTF-8')
        padded_text = padder.update(text) + padder.finalize()
    

    def depadding(self):
        unpadder = padding2.ANSIX923(256).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

        decrypted_file = self.decrypted_file_path + '\\finish_text.txt'
        with open(decrypted_file, 'w') as _file:
            _file.write(str(unpadded_dc_text))