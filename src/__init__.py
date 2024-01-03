import sys
from pathlib import Path
import hashlib



#! ISSO TEM QUE SER REVISTO MAIS TARDE

if __name__ != '__main__':
    from src.ascii import AsciiEncrypt
    from src.algorithm.tohashs import ToHASHs
    from src.algorithm.brasil_algorithm import BrasilAlgorithm
else:
    from ascii import AsciiEncrypt
    from algorithm.tohashs import ToHASHs
    from algorithm.brasil_algorithm import BrasilAlgorithm
    
#! ISSO TEM QUE SER REVISTO MAIS TARDE



class LostEncrypt(AsciiEncrypt,ToHASHs):

    def __init__(self, data: str):
        AsciiEncrypt.__init__(self,data)
        self.data = str(data)

        

teste = LostEncrypt('Teste')
teste.asciiPlus(0,returnType='str')
teste.toHASH('md5')
print(teste.data)