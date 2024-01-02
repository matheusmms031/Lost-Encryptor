class AsciiEncrypt():
    
    def __init__(self, asciiTableInterval = [33,126]):
        self.asciiTableInterval = asciiTableInterval
    
    def asciiPlus(self, n: int = 1, incrementFor: int = 0):
        match self.returnType:
            case "str":
                response = ""
                if incrementFor != 0:
                    for letter in self.data:
                        response += chr(ord(letter) + n)
                        n += incrementFor
                else:
                    for letter in self.data:
                        response += chr(ord(letter) + n)
            case "ascii":
                response = []
                if incrementFor != 0:
                    for letter in self.data:
                        response.append(ord(letter) + n)
                        n += incrementFor
                else:
                    for letter in self.data:
                        response.append(ord(letter) + n)
        self.response = response
        return self.response

    def asciiSubtract(self, n: int = 1, incrementFor: int = 0):
        match self.returnType:
            case "str":
                response = ""
                for letter in self.data:
                    response += chr(ord(letter) - n)
                    n += incrementFor
            case "ascii":
                response = []
                for letter in self.data:
                    response.append(ord(letter) - n)
                    n += incrementFor
        self.response = response
        return self.response