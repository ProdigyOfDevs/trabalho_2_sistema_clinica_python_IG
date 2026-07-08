from model_m.profissional import Profissional

class ControladorProfissional:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__profissionais = []

    @property
    def profissionais(self):
        return self.__profissionais

    def busca_profissional_por_cpf(self, cpf: str):
        for profesional in self.__profissionais:
            clean_cpf = lambda c: c.replace(".", "").replace("-", "")
            if clean_cpf(profesional.cpf) == clean_cpf(cpf):
                return profesional
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
            self.__profissionais.append(novo_profissional)
            self.__controlador_principal.tela_profissional.mostra_mensagem("Profissional cadastrado com sucesso!")

    def listar_profissionais(self):
        if not self.__profissionais:
            self.__controlador_principal.tela_profissional.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        
        self.__controlador_principal.tela_profissional.mostrar_profissionais(self.__profissionais)

    def alterar_profissional(self):
        if not self.__profissionais:
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
                self.__controlador_principal.tela_profissional.mostra_mensagem("Profissional alterado com sucesso!")
        else:
            self.__controlador_principal.tela_profissional.mostra_mensagem("Profissional não encontrado.")

    def excluir_profissional(self):
        if not self.__profissionais:
            self.__controlador_principal.tela_profissional.mostra_mensagem("Nenhum profissional cadastrado para excluir.")
            return

        cpf_busca = self.__controlador_principal.tela_profissional.selecionar_profissional()
        profissional = self.busca_profissional_por_cpf(cpf_busca)

        if profesional := profissional:
            self.__profissionais.remove(profissional)
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

