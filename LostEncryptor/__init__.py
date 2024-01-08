import sys
from pathlib import Path
import hashlib
from typing import overload, Union, Literal



#! ISSO TEM QUE SER REVISTO MAIS TARDE

if __name__ != '__main__':
    from LostEncryptor.ascii import AsciiEncrypt
    from LostEncryptor.algorithm.tohashs import ToHASHs
    from LostEncryptor.algorithm.codes import Codes
    #? from LostEncryptor.algorithm.brasil_algorithm import BrasilAlgorithm <- Deve ser revista importação
else:
    from ascii import AsciiEncrypt
    from algorithm.tohashs import ToHASHs
    from algorithm.codes import Codes
    #? from algorithm.brasil_algorithm import BrasilAlgorithm <- Deve ser revista importação
    
#! ISSO TEM QUE SER REVISTO MAIS TARDE



class LostEncrypt(AsciiEncrypt,ToHASHs,Codes):
    """LostEncrypt herda propriedades e funcões de todas as outras classes.
    """

    def __init__(self, data: str) -> None:
        
        """Função inicializadora da classe LostEncrypt

        Args:
            data (str): dados que vão ser criptografados
        """
        
        AsciiEncrypt.__init__(self,data)
        Codes.__init__(self,data)
        ToHASHs.__init__(self,data)
        self.data = str(data)
        self.encodingTypes = ['ascii','utf8']
        
    def toBytes(self,encoding: Literal["ascii", "utf8"]):
        
        """Função que transforma o `self.data` para bytes.

        Args:
            encoding (Literal["ascii", "utf8"]): Tipos de codificação aceitas

        Raises:
            ValueError: [description]

        Returns:
            [bytes]: O `self.data` codificado para bytes
            
        """
        
        if encoding in self.encodingTypes:
            self.data = self.data.encode(encoding=encoding)
            return self.data
        raise ValueError(f"{encoding} not is one type of possible")
