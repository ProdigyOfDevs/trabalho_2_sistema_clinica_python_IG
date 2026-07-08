from datetime import time
from model_m.clinica import Clinica
from daos.dao_clinica import ClinicaDAO


class ControladorClinica:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        #self.__clinicas = []
        self.__clinicas_dao = ClinicaDAO()

    @property
    def clinicas(self):
        return self.__clinicas

    def busca_clinica_por_nome(self, nome: str):
        #for clinica in self.__clinicas:
        for clinica in self.__clinicas_dao.get_all():
            if clinica.nome.lower() == nome.lower().strip():
                return clinica
        return None

    def incluir_clinica(self):
        dados = self.__controlador_principal.tela_clinica.pegar_dados_clinica()
        if dados:
            if self.busca_clinica_por_nome(dados["nome"]):
                self.__controlador_principal.tela_clinica.mostra_mensagem("Erro: Já existe uma clínica cadastrada com este nome.")
                return
            
            nova_clinica = Clinica(
                dados["nome"],
                dados["cidade"],
                dados["descricao"],
                dados["hora_abertura"],
                dados["minuto_abertura"],
                dados["hora_fechamento"],
                dados["minuto_fechamento"]
            )
            #self.__clinicas.append(nova_clinica)
            self.__clinicas_dao.add(nova_clinica)
            self.__controlador_principal.tela_clinica.mostra_mensagem("Clínica cadastrada com sucesso!")

    def listar_clinicas(self):
        clinicas = list(self.__clinicas_dao.get_all())

        if len(clinicas) == 0:
            self.__controlador_principal.tela_clinica.mostra_mensagem(
                "Nenhuma clínica cadastrada."
            )
            return

        self.__controlador_principal.tela_clinica.mostrar_clinicas(clinicas)

    def alterar_clinica(self):
        clinicas = list(self.__clinicas_dao.get_all())

        if len(clinicas) == 0:
            self.__controlador_principal.tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada para alterar.")
            return

        nome_busca = self.__controlador_principal.tela_clinica.selecionar_clinica()
        clinica = self.busca_clinica_por_nome(nome_busca)

        if clinica:
            novos_dados = self.__controlador_principal.tela_clinica.pegar_dados_clinica(alteracao=True)
            if novos_dados:
                nome_antigo = clinica.nome
                clinica.nome = novos_dados["nome"]
                clinica.cidade = novos_dados["cidade"]
                clinica.descricao = novos_dados["descricao"]

                clinica.horario_inicial = time(novos_dados["hora_abertura"], novos_dados["minuto_abertura"])
                clinica.horario_fim = time(novos_dados["hora_fechamento"], novos_dados["minuto_fechamento"])

                self.__clinicas_dao.remove(nome_antigo)
                self.__clinicas_dao.add(clinica)

                self.__controlador_principal.tela_clinica.mostra_mensagem(
                    "Clínica alterada com sucesso!"
                )
        else:
            self.__controlador_principal.tela_clinica.mostra_mensagem("Clínica não encontrada.")

    def excluir_clinica(self):
        clinicas = list(self.__clinicas_dao.get_all())

        if len(clinicas) == 0:
            self.__controlador_principal.tela_clinica.mostra_mensagem("Nenhuma clínica cadastrada para excluir.")
            return

        nome_busca = self.__controlador_principal.tela_clinica.selecionar_clinica()
        clinica = self.busca_clinica_por_nome(nome_busca)

        if clinica:
            #self.__clinicas.remove(clinica)
            self.__clinicas_dao.remove(clinica.nome)
            self.__controlador_principal.tela_clinica.mostra_mensagem("Clínica excluída com sucesso!")
        else:
            self.__controlador_principal.tela_clinica.mostra_mensagem("Clínica não encontrada.")

    def abre_menu(self):
        while True:
            opcao = self.__controlador_principal.tela_clinica.entrando_clinica()
            if opcao == 1:
                self.incluir_clinica()
            elif opcao == 2:
                self.listar_clinicas()
            elif opcao == 3:
                self.alterar_clinica()
            elif opcao == 4:
                self.excluir_clinica()
            elif opcao == 5:
                break

