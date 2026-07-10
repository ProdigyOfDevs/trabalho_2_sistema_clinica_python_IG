from daos.dao import DAO
from model_m.tipoAtendimento import TipoAtendimento


class TipoAtendimentoDAO(DAO):
    def __init__(self):
        super().__init__("tipos_atendimento.pkl")

    def add(self, tipo_atendimento: TipoAtendimento):
        if (
            (tipo_atendimento is not None)
            and isinstance(tipo_atendimento, TipoAtendimento)
            and isinstance(tipo_atendimento.descricao, str)
        ):
            super().add(tipo_atendimento.descricao, tipo_atendimento)

    def update(self, tipo_atendimento: TipoAtendimento):
        if (
            (tipo_atendimento is not None)
            and isinstance(tipo_atendimento, TipoAtendimento)
            and isinstance(tipo_atendimento.descricao, str)
        ):
            super().update(tipo_atendimento.descricao, tipo_atendimento)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
