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
    

    def depadding(self,dc_text):
        unpadder = padding2.ANSIX923(256).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

        decrypted_file = self.decrypted_file_path + '\\finish_text.txt'
        with open(decrypted_file, 'w') as _file:
            _file.write(str(unpadded_dc_text))


