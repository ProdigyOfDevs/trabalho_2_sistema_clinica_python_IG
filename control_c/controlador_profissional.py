from model_m.profissional import Profissional
from daos.dao_profissional import ProfissionalDAO

class ControladorProfissional:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__profissionais_dao = ProfissionalDAO()

    @property
    def profissionais(self):
        return list(self.__profissionais_dao.get_all())

    def busca_profissional_por_cpf(self, cpf: str):
        for profissional in self.__profissionais_dao.get_all():
            clean_cpf = lambda c: c.replace(".", "").replace("-", "")
            if clean_cpf(profissional.cpf) == clean_cpf(cpf):
                return profissional
        return None

    def incluir_profissional(self):
        dados = self.__controlador_principal.tela_profissional.pegar_dados_profissional()
        if dados:
            if self.busca_profissional_por_cpf(dados["cpf"]):
                self.__controlador_principal.tela_profissional.mostra_mensagem("Erro: Já existe um profissional cadastrado com este CPF.")
                return
            
            novo_profissional = Profissional(
                dados["nome"],
                dados["celular"],
                dados["cpf"],
                dados["especialidade"],
                dados["registro_profissional"]
            )
            self.__profissionais_dao.add(novo_profissional)
            self.__controlador_principal.tela_profissional.mostra_mensagem("Profissional cadastrado com sucesso!")

    def listar_profissionais(self):
        profissionais = list(self.__profissionais_dao.get_all())
        if not profissionais:
            self.__controlador_principal.tela_profissional.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        
        self.__controlador_principal.tela_profissional.mostrar_profissionais(profissionais)

    def alterar_profissional(self):
        profissionais = list(self.__profissionais_dao.get_all())
        if not profissionais:
            self.__controlador_principal.tela_profissional.mostra_mensagem("Nenhum profissional cadastrado para alterar.")
            return

        cpf_busca = self.__controlador_principal.tela_profissional.selecionar_profissional()
        profissional = self.busca_profissional_por_cpf(cpf_busca)

        if profissional:
            novos_dados = self.__controlador_principal.tela_profissional.pegar_dados_profissional(alteracao=True)
            if novos_dados:
                profissional.nome = novos_dados["nome"]
                profissional.celular = novos_dados["celular"]
                profissional.especialidade = novos_dados["especialidade"]
                profissional.registro_profissional = novos_dados["registro_profissional"]
                self.__profissionais_dao.update(profissional)
                self.__controlador_principal.tela_profissional.mostra_mensagem("Profissional alterado com sucesso!")
        else:
            self.__controlador_principal.tela_profissional.mostra_mensagem("Profissional não encontrado.")

    def excluir_profissional(self):
        profissionais = list(self.__profissionais_dao.get_all())
        if not profissionais:
            self.__controlador_principal.tela_profissional.mostra_mensagem("Nenhum profissional cadastrado para excluir.")
            return

        cpf_busca = self.__controlador_principal.tela_profissional.selecionar_profissional()
        profissional = self.busca_profissional_por_cpf(cpf_busca)

        if profissional:
            self.__profissionais_dao.remove(profissional.cpf)
            self.__controlador_principal.tela_profissional.mostra_mensagem("Profissional excluído com sucesso!")
        else:
            self.__controlador_principal.tela_profissional.mostra_mensagem("Profissional não encontrado.")

    def abre_menu(self):
        while True:
            opcao = self.__controlador_principal.tela_profissional.entrando_profissional()
            if opcao == 1:
                self.incluir_profissional()
            elif opcao == 2:
                self.listar_profissionais()
            elif opcao == 3:
                self.alterar_profissional()
            elif opcao == 4:
                self.excluir_profissional()
            elif opcao == 5:
                break

