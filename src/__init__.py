import sys
from pathlib import Path
import hashlib



#! ISSO TEM QUE SER REVISTO MAIS TARDE

if __name__ != '__main__':
    sys.path.append(str(Path(__file__).parent.parent))
    from src.ascii import AsciiEncrypt
else:
    from ascii import AsciiEncrypt
    
#! ISSO TEM QUE SER REVISTO MAIS TARDE




# The `LostEncrypt` class is a subclass of `AsciiEncrypt` that encrypts data using ASCII values and
# allows for customization of the return type.
class LostEncrypt(AsciiEncrypt):

    def __init__(self, data, asciiTableInterval = [33,126]):
        AsciiEncrypt.__init__(self,asciiTableInterval)
        self.data = str(data)
    
    def toHASH(self, codify, type: str = 'hexadecimal') -> str | bytes:
        data = self.data
        if isinstance(data,str):
            data_encode = self.data.encode()
        elif isinstance(data,list):
            data_encode = bytes(self.data)
            
        if codify == 'md5':
            hash = hashlib.md5(data_encode)
        elif codify == 'sha1':
            hash = hashlib.sha1(data_encode)
        elif codify == 'sha256':
            hash = hashlib.sha256(data_encode)
        elif codify == 'sha512':
            hash = hashlib.sha512(data_encode)
            
        if type == 'hexadecimal':
            self.data = hash.hexdigest()
        elif type == 'bytes':
            self.data = hash.digest()
            
        return self.data

        
                
teste = LostEncrypt('Teste')
teste.asciiPlus(0,returnType='str')
teste.toHASH('md5')
print(teste.data)