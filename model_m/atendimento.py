from datetime import date, time
from model_m.clinica import Clinica
from model_m.paciente import Paciente
from model_m.profissional import Profissional
from model_m.tipoAtendimento import TipoAtendimento
from model_m.procedimento import Procedimento
from model_m.pagamento import Pagamento, PagamentoCartao, PagamentoDinheiro, PagamentoPix


class Atendimento:
    def __init__(self,ano:int,mes:int,dia:int, hora_inicio:int,minuto_inicio:int, hora_fim:int,minuto_fim:int,
                valor:float, clinica:Clinica, paciente:Paciente, profissional:Profissional, tipo_atend:TipoAtendimento):
        self.__data = date(ano,mes,dia)
        self.__horario_inicio = time(hora_inicio,minuto_inicio)
        self.__horario_fim = time(hora_fim,minuto_fim)
        self.__valor = valor
        if isinstance(clinica,Clinica):
            self.__clinica = clinica
        if isinstance(paciente,Paciente):
            self.__paciente = paciente
        if isinstance(profissional,Profissional):
            self.__profissional_responsavel = profissional
        if isinstance(tipo_atend,TipoAtendimento):
            self.__tipo_atendimento = tipo_atend
        self.__pagamentos = []
        self.__procedimentos = []
       
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data
    
    @property
    def horario_inicio(self):
        return self.__horario_inicio
    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: time):
        if isinstance(horario_inicio, time):
            self.__horario_inicio = horario_inicio
    
    @property
    def horario_fim(self):
        return self.__horario_fim
    @horario_fim.setter
    def horario_fim(self, horario_fim: time):
        if isinstance(horario_fim, time):
            self.__horario_fim = horario_fim

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor:float):
        self.__valor = valor
    
    @property
    def clinica(self):
        return self.__clinica
    @clinica.setter
    def clinica(self, clinica:Clinica):
        if isinstance(clinica,Clinica):
            self.__clinica = clinica
    
    @property
    def paciente(self):
        return self.__paciente
    @paciente.setter
    def paciente(self, paciente:Paciente):
        if isinstance(paciente,Paciente):
            self.__paciente = paciente

    @property
    def profissional_responsavel(self):
        return self.__profissional_responsavel
    @profissional_responsavel.setter
    def profissional_responsavel(self, profissional_responsavel:Profissional):
        if isinstance(profissional_responsavel,Profissional):
            self.__profissional_responsavel = profissional_responsavel
    
    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento
    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento:TipoAtendimento):
        if isinstance(tipo_atendimento,TipoAtendimento):
            self.__tipo_atendimento = tipo_atendimento
    
    @property
    def pagamentos(self):
        return self.__pagamentos
    def adicionar_pagamento(self, pagamento: Pagamento):
        if isinstance(pagamento, Pagamento):
            self.__pagamentos.append(pagamento)
    def remover_pagamento(self):
        ultimo=len(self.pagamentos)
        self.__pagamentos.pop(ultimo-1)

    @property
    def procedimentos(self):
        return self.__procedimentos
    def adicionar_procedimento(self, descricao:str, custo:float, profissional:Profissional):
        if isinstance(profissional,Profissional):
            self.__procedimentos.append(Procedimento(descricao,custo,profissional))
    def remover_procedimento(self):
        ultimo=len(self.procedimentos)
        self.__procedimentos.pop(ultimo-1)

    def valor_de_atendimento(self):
        total=0
        total+=self.__tipo_atendimento.valor_base
        return total

    def total_de_procedimentos(self):
        total=0
        for x in range(len(self.__procedimentos)):
            total+=self.__procedimentos[x].custo
        return total
    
    def valor_restante(self):
        valor_restante=self.__valor
        valor_restante+=self.total_de_procedimentos()
        valor_restante+=self.valor_de_atendimento()
        for x in range(len(self.__pagamentos)):
            valor_restante-=self.__pagamentos[x].valor
        return valor_restante
