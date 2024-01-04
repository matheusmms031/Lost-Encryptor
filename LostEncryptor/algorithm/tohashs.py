import hashlib


class ToHASHs():

    def __init__(self,data:str = '') -> None:
        self.data = data
    
    def toHASH(self, codify: str, type: str = 'hexadecimal') -> str | bytes:
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