import sys
from pathlib import Path
import hashlib
from typing import overload, Union, Literal



if __name__ != '__main__':
    from algorithm.tohashs import ToHASHs
    from ascii import AsciiEncrypt
else:
    from tohashs import ToHASHs
    sys.path.append(str(Path(__file__).parent.parent))
    from ascii import AsciiEncrypt


class BrasilAlgorithm(AsciiEncrypt,ToHASHs):
    
    def __init__(self,data: str, key: int) -> None:
        self.data = data
        AsciiEncrypt.__init__(self,data)
        self.key = key
    
    def paco(self):
        self.asciiPlus(self.key)
        return self.data