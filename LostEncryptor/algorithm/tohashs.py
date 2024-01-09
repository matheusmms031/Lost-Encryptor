import hashlib
from typing import Literal




class ToHASHs():
    """Classe que contém as funções de hash para a classe `LostEncrypt`
    
    """
    

    def __init__(self,data:str = '') -> None:
        self.data = data
        
    def is_list_or_str(self,data): #* Isto é utilitário
        
        data_encode = None
        if isinstance(data,str):
            data_encode = data.encode()
        elif isinstance(data,list):
            data_encode = bytes(data)
            
        return data_encode
    
    def return_type_is(self,return_type,cripto): #* Isto é utilitário
        
        data = None
        if return_type == 'hexadecimal':
            data = cripto.hexdigest()
        elif return_type == 'bytes':
            data = cripto.digest()
            
        return data
            
        
    def to_md5(self, return_type: Literal['hexadecimal','decimal'] = 'hexadecimal') -> str | bytes:
        """Criptografa o `self.data` em `MD5`

        Args:
            return_type (Literal['bytes','hexadecimal']): Especifica o tipo de dados de retorno.

        Returns:
            (Literal['hexadecimal','bytes']): Em bytes ou em hexadecimal.
            
        """
        
        
        data_encode = self.is_list_or_str(self.data)
        criptografado = hashlib.md5(data_encode)   
        self.data = self.return_type_is(return_type,criptografado)
        return self.data
    
    def to_sha1(self, return_type: str = 'hexadecimal') -> str | bytes:
        """Criptografa o `self.data` em `SHA1`

        Args:
            return_type (Literal['bytes','hexadecimal']): Especifica o tipo de dados de retorno.

        Returns:
            (Literal['hexadecimal','bytes']): Em bytes ou em hexadecimal.
        """
        
        data_encode = self.is_list_or_str(self.data)
        criptografado = hashlib.sha1(data_encode)   
        self.data = self.return_type_is(return_type,criptografado)
        return self.data
    
    def to_sha256(self, return_type: str = 'hexadecimal') -> str | bytes:
        """Criptografa o `self.data` em `SHA256`

        Args:
            return_type (Literal['bytes','hexadecimal']): Especifica o tipo de dados de retorno.

        Returns:
            (Literal['hexadecimal','bytes']): Em bytes ou em hexadecimal.
        """
        
        data_encode = self.is_list_or_str(self.data)
        criptografado = hashlib.sha256(data_encode)   
        self.data = self.return_type_is(return_type,criptografado)
        return self.data
    
    def to_sha512(self, return_type: str = 'hexadecimal') -> str | bytes:
        """Criptografa o `self.data` em `SHA512`

        Args:
            return_type (Literal['bytes','hexadecimal']): Especifica o tipo de dados de retorno.

        Returns:
            (Literal['hexadecimal','bytes']): Em bytes ou em hexadecimal.
        """
        
        data_encode = self.is_list_or_str(self.data)
        criptografado = hashlib.sha512(data_encode)   
        self.data = self.return_type_is(return_type,criptografado)
        return self.data