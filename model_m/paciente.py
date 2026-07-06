from model_m.pessoa import Pessoa
import datetime

class Paciente(Pessoa):
    def __init__(self, nome:str, celular:str, cpf:str, ano_nascimento:int, mes_nascimento:int, dia_nascimento:int):
        super().__init__(nome, celular, cpf)
        self.__nascimento = datetime.date(ano_nascimento,mes_nascimento,dia_nascimento)

    @property
    def nascimento(self):
        return self.__nascimento
    @nascimento.setter
    def nascimento(self, nascimento: datetime.date):
        if isinstance(nascimento, datetime.date):
            self.__nascimento = nascimento