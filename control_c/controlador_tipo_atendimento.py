from model_m.tipoAtendimento import TipoAtendimento

class ControladorTipoAtendimento:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tipos_atendimento = []

    @property
    def tipos_atendimento(self):
        return self.__tipos_atendimento

    def busca_tipo_por_descricao(self, descricao: str):
        for tipo in self.__tipos_atendimento:
            if tipo.descricao.lower() == descricao.lower().strip():
                return tipo
        return None

    def incluir_tipo_atendimento(self):
        dados = self.__controlador_principal.tela_tipo_atendimento.pegar_dados_tipo_atendimento()
        if dados:
            if self.busca_tipo_por_descricao(dados["descricao"]):
                self.__controlador_principal.tela_tipo_atendimento.mostra_mensagem("Erro: Já existe um tipo de atendimento cadastrado com esta descrição.")
                return
            
            novo_tipo = TipoAtendimento(
                dados["descricao"],
                dados["valor_base"]
            )
            self.__tipos_atendimento.append(novo_tipo)
            self.__controlador_principal.tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento cadastrado com sucesso!")

    def listar_tipos_atendimento(self):
        if not self.__tipos_atendimento:
            self.__controlador_principal.tela_tipo_atendimento.mostra_mensagem("Nenhum tipo de atendimento cadastrado.")
            return
        
        self.__controlador_principal.tela_tipo_atendimento.mostrar_tipos_atendimento(self.__tipos_atendimento)

    def alterar_tipo_atendimento(self):
        if not self.__tipos_atendimento:
            self.__controlador_principal.tela_tipo_atendimento.mostra_mensagem("Nenhum tipo de atendimento cadastrado para alterar.")
            return

        descricao_busca = self.__controlador_principal.tela_tipo_atendimento.selecionar_tipo_atendimento()
        tipo = self.busca_tipo_por_descricao(descricao_busca)

        if tipo:
            novos_dados = self.__controlador_principal.tela_tipo_atendimento.pegar_dados_tipo_atendimento(alteracao=True)
            if novos_dados:
                tipo.descricao = novos_dados["descricao"]
                tipo.valor_base = novos_dados["valor_base"]
                self.__controlador_principal.tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento alterado com sucesso!")
        else:
            self.__controlador_principal.tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento não encontrado.")

    def excluir_tipo_atendimento(self):
        if not self.__tipos_atendimento:
            self.__controlador_principal.tela_tipo_atendimento.mostra_mensagem("Nenhum tipo de atendimento cadastrado para excluir.")
            return

        descricao_busca = self.__controlador_principal.tela_tipo_atendimento.selecionar_tipo_atendimento()
        tipo = self.busca_tipo_por_descricao(descricao_busca)

        if tipo:
            self.__tipos_atendimento.remove(tipo)
            self.__controlador_principal.tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento excluído com sucesso!")
        else:
            self.__controlador_principal.tela_tipo_atendimento.mostra_mensagem("Tipo de atendimento não encontrado.")

    def abre_menu(self):
        while True:
            opcao = self.__controlador_principal.tela_tipo_atendimento.entrando_tipo_atendimento()
            if opcao == 1:
                self.incluir_tipo_atendimento()
            elif opcao == 2:
                self.listar_tipos_atendimento()
            elif opcao == 3:
                self.alterar_tipo_atendimento()
            elif opcao == 4:
                self.excluir_tipo_atendimento()
            elif opcao == 5:
                break

