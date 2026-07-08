from datetime import date
from model_m.paciente import Paciente

class ControladorPaciente:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__pacientes = []

    @property
    def pacientes(self):
        return self.__pacientes

    def busca_paciente_por_cpf(self, cpf: str):
        for paciente in self.__pacientes:
            clean_cpf = lambda c: c.replace(".", "").replace("-", "")
            if clean_cpf(paciente.cpf) == clean_cpf(cpf):
                return paciente
        return None

    def incluir_paciente(self):
        dados = self.__controlador_principal.tela_paciente.pegar_dados_paciente()
        if dados:
            if self.busca_paciente_por_cpf(dados["cpf"]):
                self.__controlador_principal.tela_paciente.mostra_mensagem("Erro: Já existe um paciente cadastrado com este CPF.")
                return
            
            novo_paciente = Paciente(
                dados["nome"],
                dados["celular"],
                dados["cpf"],
                dados["ano_nascimento"],
                dados["mes_nascimento"],
                dados["dia_nascimento"]
            )
            self.__pacientes.append(novo_paciente)
            self.__controlador_principal.tela_paciente.mostra_mensagem("Paciente cadastrado com sucesso!")

    def listar_pacientes(self):
        if not self.__pacientes:
            self.__controlador_principal.tela_paciente.mostra_mensagem("Nenhum paciente cadastrado.")
            return
        
        self.__controlador_principal.tela_paciente.mostrar_pacientes(self.__pacientes)

    def alterar_paciente(self):
        if not self.__pacientes:
            self.__controlador_principal.tela_paciente.mostra_mensagem("Nenhum paciente cadastrado para alterar.")
            return

        cpf_busca = self.__controlador_principal.tela_paciente.selecionar_paciente()
        paciente = self.busca_paciente_por_cpf(cpf_busca)

        if paciente:
            novos_dados = self.__controlador_principal.tela_paciente.pegar_dados_paciente(alteracao=True)
            if novos_dados:
                paciente.nome = novos_dados["nome"]
                paciente.celular = novos_dados["celular"]
                paciente.nascimento = date(
                    novos_dados["ano_nascimento"],
                    novos_dados["mes_nascimento"],
                    novos_dados["dia_nascimento"]
                )
                self.__controlador_principal.tela_paciente.mostra_mensagem("Paciente alterado com sucesso!")
        else:
            self.__controlador_principal.tela_paciente.mostra_mensagem("Paciente não encontrado.")

    def excluir_paciente(self):
        if not self.__pacientes:
            self.__controlador_principal.tela_paciente.mostra_mensagem("Nenhum paciente cadastrado para excluir.")
            return

        cpf_busca = self.__controlador_principal.tela_paciente.selecionar_paciente()
        paciente = self.busca_paciente_por_cpf(cpf_busca)

        if paciente:
            self.__pacientes.remove(paciente)
            self.__controlador_principal.tela_paciente.mostra_mensagem("Paciente excluído com sucesso!")
        else:
            self.__controlador_principal.tela_paciente.mostra_mensagem("Paciente não encontrado.")

    def abre_menu(self):
        while True:
            opcao = self.__controlador_principal.tela_paciente.entrando_paciente()
            if opcao == 1:
                self.incluir_paciente()
            elif opcao == 2:
                self.listar_pacientes()
            elif opcao == 3:
                self.alterar_paciente()
            elif opcao == 4:
                self.excluir_paciente()
            elif opcao == 5:
                break

