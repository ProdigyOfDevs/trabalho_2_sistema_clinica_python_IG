from daos.dao import DAO
from model_m.atendimento import Atendimento


class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__("atendimentos.pkl")

    def add(self, atendimento: Atendimento):
        if (
            (atendimento is not None)
            and isinstance(atendimento, Atendimento)
        ):
            key = f"{atendimento.paciente.cpf}_{atendimento.data.strftime('%d%m%Y')}_{atendimento.horario_inicio.strftime('%H%M')}"
            super().add(key, atendimento)

    def update(self, atendimento: Atendimento):
        if (
            (atendimento is not None)
            and isinstance(atendimento, Atendimento)
        ):
            key = f"{atendimento.paciente.cpf}_{atendimento.data.strftime('%d%m%Y')}_{atendimento.horario_inicio.strftime('%H%M')}"
            super().update(key, atendimento)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
