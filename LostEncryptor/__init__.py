
"""
Lost Encryptor
~~~~~~~~~~~~~~~~~~~~~

Pacote de criptografia e codificação em cadas.

:license: GPL V.3.0.
"""


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



# The `LostEncrypt` class is a subclass of `AsciiEncrypt` and `ToHASHs` that takes a string as input
# and initializes the `data` attribute.
class LostEncrypt(AsciiEncrypt,ToHASHs,Codes):

    def __init__(self, data: str) -> None:
        AsciiEncrypt.__init__(self,data)
        self.data = str(data)
        self.encodingTypes = ['ascii','utf8']

    def toBytes(self,encoding: Literal["ascii", "utf8"]):
        if encoding in self.encodingTypes:
            self.data = self.data.encode(encoding=encoding)
                
