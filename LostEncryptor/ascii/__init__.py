class AsciiEncrypt():
    
    """Classe que contém as funções de codificação ascii.
    
    Note:
        É preferivel utilizar o argumento return_type no `ascii_plus` e `ascii_subtract` como `ascii`,
        já que existem alguns caractéres que não podem ser visiveis quando convertidos novamente em texto.
    
    """
    
    def __init__(self, data, ascii_table_interval = [0,256]):
        self.data = data
        self.ascii_table_interval = ascii_table_interval
    
    def ascii_plus(self, n: int = 0, increment_for: int = 0, return_type: str = 'str') -> str | list:
        
        """Função que converte `self.data` para ascii e soma com `n`
        
        Note:
            O `ascii_plus` não aceita o dado para ser codificado como atributo direto, é necessário instanciar um objeto `LostEncrypt` ou
            `AsciiEncrypt` e setar o `self.data`, fora isso a função não entrega nada.

        Args:
            n (int): Numero de casas a serem saltadas.
            increment_for (int): Numero usado para servir como incremento a cada vez que uma casa é saltada. 
            return_type (str): O tipo de retorno da função.

        Returns:
            (str | list): Pode ser ou em `string` ou `list` dependendo do valor de `return_type`
            
        Example: Quero transformar o texto `teste` contido em `self.data` em ascii e somar 2 cada caracter.
            ```python
            >>> objeto = LostEncrypt('teste')
            >>> print(asciiPlus(n=2))
            vguvg
            ```
        """
        
        
        
        match return_type:
            case "str":
                
                response = ""
                for letter in self.data:
                    ascii_transform = ord(letter) + n
                    max_interval = ascii_transform // self.ascii_table_interval[1]
                    response += chr(ascii_transform - self.ascii_table_interval[1]*max_interval)
                    n += increment_for
                    
            case "ascii":
                
                response = []
                for letter in self.data:
                    ascii_transform = ord(letter) + n
                    max_interval = ascii_transform // self.ascii_table_interval[1]
                    response.append(ascii_transform - self.ascii_table_interval[1]*max_interval)
                    n += increment_for
                
        self.data = response
        return response

    
    def ascii_subtract(self, n: int = 0, increment_for: int = 0, return_type: str = 'str'):
        """Função que converte `self.data` para ascii e subtrai com `n`
        
        Note:
            O `ascii_subtract` não aceita o dado para ser codificado como atributo direto, é necessário instanciar um objeto `LostEncrypt` ou
            `AsciiEncrypt` e setar o `self.data`, fora isso a função não entrega nada.

        Args:
            n (int): Numero de casas a serem saltadas para trás.
            increment_for (int): Numero usado para servir como incremento a cada vez que uma casa é saltada para trás. 
            return_type (str): O tipo de retorno da função.

        Returns:
            (str | list): Pode ser ou em `string` ou `list` dependendo do valor de `return_type`
            
        Example: Quero transformar o texto `teste` contido em `self.data` em ascii e subtrair 2 cada caracter.
            ```python
            >>> objeto = LostEncrypt('teste')
            >>> print(ascii_subtract(n=2))
            rcqrc
            ```
        """
        
        match return_type:
            
            #! DEVE SER CORRIGIDO
            
            case "str":
                response = ""
                for letter in self.data:
                    ascii_transform = ord(letter) - n # -100
                    min_interval = ascii_transform // -(self.ascii_table_interval[1])
                    if ascii_transform < 0:
                        ascii_transform += 256
                        if min_interval > 1:
                            ascii_transform += 256*min_interval-1
                        response += chr(ascii_transform) # * Deve ser testado
                    else:
                        response += chr(ascii_transform)
                    n += increment_for
                    
            case "ascii":
                response = []
                for letter in self.data:
                    ascii_transform = ord(letter) - n
                    min_interval = ascii_transform // -(self.ascii_table_interval[1])
                    if ascii_transform < 0:
                        ascii_transform += 256
                        if min_interval > 1:
                            ascii_transform += 256*min_interval-1
                        response.append(ascii_transform) # * Deve ser testado
                    else: 
                        response.append(ascii_transform)
                    n += increment_for
                    
                    
        self.data = response
        return response
    
    
    