class AsciiEncrypt():
    """
    A classe `AsciiEncrypt` fornece métodos para criptografar e descriptografar caracteres ASCII usando um
    intervalo especificado.
    
    Argumentos:
      n (int): O parâmetro `n` nos métodos `asciiPlus` e `asciiSubtract` representa o número de
    posições para mudar o valor ASCII de cada caractere. Determina quanto será o valor ASCII
    incrementado ou decrementado. O padrão é 1
      incrementFor (int): O parâmetro `incrementFor` é usado para especificar a quantidade pela qual o valor
    de `n` deve ser incrementado após cada iteração do loop. Permite incrementação dinâmica
    de `n` para obter diferentes padrões de criptografia. O padrão é 0
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

    
    def asciiSubtract(self, n: int = 1, incrementFor: int = 0, returnType: str = 'str'):
        
        match returnType:
            case "str":
                response = ""
                for letter in self.data:
                    ascii = ord(letter) - n
                    minInterval = ascii // self.asciiTableInterval[0]
                    if minInterval != 0:
                        response += chr(self.asciiTableInterval[1] - (ascii - minInterval*self.asciiTableInterval[1])) # * Deve ser testado
                    else:
                        response += chr(ascii)
                    n += incrementFor
                    
            case "ascii":
                response = []
                for letter in self.data:
                    ascii = ord(letter) - n
                    minInterval = ascii // self.asciiTableInterval[0]
                    if minInterval != 0:
                        response.append(self.asciiTableInterval[1] - (ascii - minInterval*self.asciiTableInterval[1])) # * Deve ser testado
                    else: 
                        response.append(ascii)
                    n += incrementFor
                    
                    
        self.data = response
        return response
    
    
    