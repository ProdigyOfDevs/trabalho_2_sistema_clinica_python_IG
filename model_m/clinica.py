from datetime import time
class Clinica:
    def __init__(self,nome:str,cidade:str,descricao:str,
                 hora_inicial,minuto_inicial,
                 hora_final,minuto_final):
        self.__nome=nome
        self.__cidade=cidade
        self.__descricao=descricao
        self.__horario_inicial=time(hora_inicial,minuto_inicial)
        self.__horario_fim=time(hora_final,minuto_final)

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    @property
    def cidade(self):
        return self.__cidade
    @cidade.setter
    def cidade(self, cidade:str):
        self.__cidade = cidade

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao:str):
        self.__descricao = descricao

    
    @property
    def horario_inicial(self):
        return self.__horario_inicial
    @horario_inicial.setter
    def horario_inicial(self, horario_inicial: time):
        if isinstance(horario_inicial, time):
            self.__horario_inicial = horario_inicial
    
    @property
    def horario_fim(self):
        return self.__horario_fim
    @horario_fim.setter
    def horario_fim(self, horario_fim: time):
        if isinstance(horario_fim, time):
            self.__horario_fim = horario_fim