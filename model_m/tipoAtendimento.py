class TipoAtendimento():
    def __init__(self, descricao: str, valor_base: float):
        self.__descricao = descricao
        self.__valor_base = valor_base
    
    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao:str):
        self.__descricao = descricao
    
    @property
    def valor_base(self):
        return self.__valor_base
    @valor_base.setter
    def valor_base(self, valor_base:float):
        self.__valor_base = valor_base