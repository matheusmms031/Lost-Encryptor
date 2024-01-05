
"""
Lost Encryptor
~~~~~~~~~~~~~~~~~~~~~

Pacote de criptografia e codificação em cadas.

:license: GPL V.3.0.
"""


import sys
from pathlib import Path
import hashlib


#! ISSO TEM QUE SER REVISTO MAIS TARDE

if __name__ != '__main__':
    from LostEncryptor.ascii import AsciiEncrypt
    from LostEncryptor.algorithm.tohashs import ToHASHs
    #? from LostEncryptor.algorithm.brasil_algorithm import BrasilAlgorithm <- Deve ser revista importação
else:
    from ascii import AsciiEncrypt
    from algorithm.tohashs import ToHASHs
    #? from algorithm.brasil_algorithm import BrasilAlgorithm <- Deve ser revista importação
    
#! ISSO TEM QUE SER REVISTO MAIS TARDE



# The `LostEncrypt` class is a subclass of `AsciiEncrypt` and `ToHASHs` that takes a string as input
# and initializes the `data` attribute.
class LostEncrypt(AsciiEncrypt,ToHASHs):

    def __init__(self, data: str):
        AsciiEncrypt.__init__(self,data)
        self.data = str(data)

        
