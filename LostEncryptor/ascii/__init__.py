class AsciiEncrypt():
    """
    The `AsciiEncrypt` class provides methods for encrypting and decrypting ASCII characters using a
    specified interval.
    
    Args:
      n (int): The parameter `n` in the `asciiPlus` and `asciiSubtract` methods represents the number of
    positions to shift the ASCII value of each character. It determines how much the ASCII value will be
    incremented or decremented. Defaults to 1
      incrementFor (int): The `incrementFor` parameter is used to specify the amount by which the value
    of `n` should be incremented after each iteration of the loop. It allows for dynamic incrementation
    of `n` in order to achieve different encryption patterns. Defaults to 0
    """
    
    def __init__(self, data, asciiTableInterval = [0,256]):
        self.data = data
        self.asciiTableInterval = asciiTableInterval
    
    def asciiPlus(self, n: int = 1, incrementFor: int = 0, returnType: str = 'str') -> str | list:
        match returnType:
            case "str":
                
                response = ""
                for letter in self.data:
                    ascii = ord(letter) + n
                    maxInterval = ascii // self.asciiTableInterval[1]
                    response += chr(ascii - self.asciiTableInterval[1]*maxInterval)
                    n += incrementFor
                    
            case "ascii":
                
                response = []
                for letter in self.data:
                    ascii = ord(letter) + n
                    maxInterval = ascii // self.asciiTableInterval[1]
                    response.append(ascii - self.asciiTableInterval[1]*maxInterval)
                    n += incrementFor
                
        self.data = response
        return response

    
    def asciiSubtract(self, n: int = 1, incrementFor: int = 0, returnType: str = 'str'): #! Está faltando redefinir quando for menor que 0
        
        match returnType:
            case "str":
                response = ""
                for letter in self.data:
                    ascii = ord(letter) - n
                    minInterval = ascii // self.asciiTableInterval[0]
                    response += chr(ascii - minInterval*self.asciiTableInterval[1])
                    n += incrementFor
            case "ascii":
                response = []
                for letter in self.data:
                    response.append(ord(letter) - n)
                    n += incrementFor
                    
                    
        self.data = response
        return response
    
    
    