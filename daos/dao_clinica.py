from daos.dao import DAO
from model_m.clinica import Clinica


# cada entidade terá uma classe dessa, implementação bem simples.
class ClinicaDAO(DAO):
    def __init__(self):
        super().__init__("clinicas.pkl")

    def add(self, clinica: Clinica):
        if (
            (clinica is not None)
            and isinstance(clinica, Clinica)
        ):
            super().add(clinica.nome, clinica)

    def update(self, clinica: Clinica):
        if (
            (clinica is not None)
            and isinstance(clinica, Clinica)
        ):
            super().update(clinica.nome, clinica)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)