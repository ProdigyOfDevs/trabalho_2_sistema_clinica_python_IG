from model_m.profissional import Profissional

class Procedimento:
    def __init__(self, descricao:str, custo:float, profissional_responsavel:Profissional):
        self.__descricao = descricao
        self.__custo = custo
        if isinstance(profissional_responsavel,Profissional):
            self.__profissional_responsavel = profissional_responsavel

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao:str):
        self.__descricao = descricao

    @property
    def custo(self):
        return self.__custo
    @custo.setter
    def custo(self, custo:float):
        self.__custo = custo

    @property
    def profissional_responsavel(self):
        return self.__profissional_responsavel
    def alocar_profissional(self, profissional_responsavel:Profissional):
        if isinstance(profissional_responsavel,Profissional):
            self.__profissional_responsavel = profissional_responsavel

        