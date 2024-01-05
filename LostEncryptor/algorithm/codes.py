import base64


class Codes():
    
    def __init__(self,data):
        self.data = data
        
    def EncodeBase64(self):
        self.data = base64.b64encode(self.data)
        return self.data

    def DecodeBase64(self):
        self.data = base64.b64decode(self.data)
        return self.data 