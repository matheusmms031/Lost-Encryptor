from ascii import AsciiEncrypt


class LostEncrypt(AsciiEncrypt):

    def __init__(self, data, returnType:str = 'str', asciiTableInterval = [33,126]):
        AsciiEncrypt.__init__(self,asciiTableInterval)
        
        
        self.data = data
        self.respose = data
        self.returnType = returnType
    
    
    
    
enc = LostEncrypt('teste','str')
print(enc.asciiPlus(1,1))
print(enc.asciiSubtract(1))
print(enc.asciiTableInterval)