from daos.dao import DAO
from model_m.paciente import Paciente


class PacienteDAO(DAO):
    def __init__(self):
        super().__init__("pacientes.pkl")

    def add(self, paciente: Paciente):
        if (
            (paciente is not None)
            and isinstance(paciente, Paciente)
            and isinstance(paciente.cpf, str)
        ):
            super().add(paciente.cpf, paciente)

    def update(self, paciente: Paciente):
        if (
            (paciente is not None)
            and isinstance(paciente, Paciente)
            and isinstance(paciente.cpf, str)
        ):
            super().update(paciente.cpf, paciente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
