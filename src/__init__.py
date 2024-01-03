import sys
from pathlib import Path


sys.path.append(str(Path(__file__).parent.parent))


from src.ascii import AsciiEncrypt


# The `LostEncrypt` class is a subclass of `AsciiEncrypt` that encrypts data using ASCII values and
# allows for customization of the return type.
class LostEncrypt(AsciiEncrypt):

    def __init__(self, data, returnType:str = 'str', asciiTableInterval = [33,126]):
        AsciiEncrypt.__init__(self,asciiTableInterval)
        
        self.data = data
        self.returnType = returnType
        
