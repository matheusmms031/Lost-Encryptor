import base64


class Codes():
    """Classe que contém funções para codificar e decodificar em bases.
    
    """
    
    def __init__(self,data):
        self.data = data
        
    def EncodeBase64(self):
        """Função que encoda o `self.data` em `base64`

        Returns:
            (bytes): Retorna em bytes o `self.data` em `base64`
        """
        self.data = base64.b64encode(self.data)
        return self.data

    def DecodeBase64(self):
        """Função que decoda o `self.data` em `base64`

        Returns:
            (bytes): Retorna em bytes o `self.data` decodado em `base64`
        """
        
        self.data = base64.b64decode(self.data)
        return self.data 