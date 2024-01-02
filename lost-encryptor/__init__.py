class LostEncrypt():

    def __init__(self, data, returnType = 'str'):
        self.data = data
        self.respose = data
        self.returnType = returnType


    def asciiPlus(self,n: int = 1, incrementFor: int = 0):
        match self.returnType:
            case 'str':
                response = ''
                if incrementFor != 0:
                    for letter in self.data:
                        response += chr(ord(letter)+n)
                        n += incrementFor
                else:
                    for letter in self.data:
                        response += chr(ord(letter)+n)
            case 'ascii':
                response = []
                if incrementFor != 0:
                    for letter in self.data:
                        response.append(ord(letter)+n)
                        n += incrementFor
                else:
                    for letter in self.data:
                        response.append(ord(letter)+n)
        self.response = response
        return self.response



    
    
enc = LostEncrypt('teste','str')
print(enc.asciiPlus(1,1))