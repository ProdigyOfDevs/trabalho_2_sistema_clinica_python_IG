from abc import ABC
from model_m.paciente import Paciente
from datetime import date

class Pagamento(ABC):
    def __init__(self, data:date , paciente:Paciente, valor:float):
        self.__data = data
        self.__paciente = paciente
        self.__valor = valor 
    
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data:date):
        self.__data = data

    @property
    def paciente(self):
        return self.__paciente
    @paciente.setter
    def paciente(self, paciente:Paciente):
        if isinstance(paciente,Paciente):
            self.__paciente = paciente

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor:float):
        self.__valor = valor

class PagamentoPix(Pagamento):
    def __init__(self, data:date, paciente:Paciente, valor:float, cpf_pagador:str):
        super().__init__( data, paciente, valor)
        self.__cpf = cpf_pagador

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf:str):
        self.__cpf = cpf

class PagamentoCartao(Pagamento):
    def __init__(self, data:date, paciente:Paciente, valor:float, num_cartao:str, bandeira:str):
        super().__init__( data, paciente, valor)
        self.__numero_cartao = num_cartao
        self.__bandeira = bandeira

    @property
    def numero_cartao(self):
        return self.__numero_cartao
    @numero_cartao.setter
    def numero_cartao(self, numero_cartao:str):
        self.__numero_cartao = numero_cartao

    @property
    def bandeira(self):
        return self.__bandeira
    @bandeira.setter
    def bandeira(self, bandeira:str):
        self.__bandeira = bandeira

class PagamentoDinheiro(Pagamento):
    def __init__(self, data:date, paciente:Paciente, valor:float,):
        super().__init__( data, paciente, valor)
