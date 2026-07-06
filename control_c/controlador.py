from model_m.clinica import Clinica
from model_m.paciente import Paciente
from model_m.profissional import Profissional
from model_m.tipoAtendimento import TipoAtendimento
from model_m.atendimento import Atendimento
from model_m.pagamento import PagamentoPix, PagamentoCartao, PagamentoDinheiro
from view_v.tela import TelaApp
from datetime import time, date

class ControladorClinica:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__clinicas = []

    @property
    def clinicas(self):
        return self.__clinicas

    def busca_clinica_por_nome(self, nome: str):
        for clinica in self.__clinicas:
            if clinica.nome.lower() == nome.lower().strip():
                return clinica
        return None

    def incluir_clinica(self):
        dados = self.__controlador_principal.tela.pegar_dados_clinica()
        if dados:
            if self.busca_clinica_por_nome(dados["nome"]):
                self.__controlador_principal.tela.mostra_mensagem("Erro: Já existe uma clínica cadastrada com este nome.")
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
            self.__clinicas.append(nova_clinica)
            self.__controlador_principal.tela.mostra_mensagem("Clínica cadastrada com sucesso!")

    def listar_clinicas(self):
        if not self.__clinicas:
            self.__controlador_principal.tela.mostra_mensagem("Nenhuma clínica cadastrada.")
            return
        
        self.__controlador_principal.tela.mostrar_clinicas(self.__clinicas)

    def alterar_clinica(self):
        if not self.__clinicas:
            self.__controlador_principal.tela.mostra_mensagem("Nenhuma clínica cadastrada para alterar.")
            return

        nome_busca = self.__controlador_principal.tela.selecionar_clinica()
        clinica = self.busca_clinica_por_nome(nome_busca)

        if clinica:
            novos_dados = self.__controlador_principal.tela.pegar_dados_clinica(alteracao=True)
            if novos_dados:
                clinica.nome = novos_dados["nome"]
                clinica.cidade = novos_dados["cidade"]
                clinica.descricao = novos_dados["descricao"]
                
                clinica.horario_inicial = time(novos_dados["hora_abertura"], novos_dados["minuto_abertura"])
                clinica.horario_fim = time(novos_dados["hora_fechamento"], novos_dados["minuto_fechamento"])
                
                self.__controlador_principal.tela.mostra_mensagem("Clínica alterada com sucesso!")
        else:
            self.__controlador_principal.tela.mostra_mensagem("Clínica não encontrada.")

    def excluir_clinica(self):
        if not self.__clinicas:
            self.__controlador_principal.tela.mostra_mensagem("Nenhuma clínica cadastrada para excluir.")
            return

        nome_busca = self.__controlador_principal.tela.selecionar_clinica()
        clinica = self.busca_clinica_por_nome(nome_busca)

        if clinica:
            self.__clinicas.remove(clinica)
            self.__controlador_principal.tela.mostra_mensagem("Clínica excluída com sucesso!")
        else:
            self.__controlador_principal.tela.mostra_mensagem("Clínica não encontrada.")

    def abre_menu(self):
        while True:
            opcao = self.__controlador_principal.tela.entrando_clinica()
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
        dados = self.__controlador_principal.tela.pegar_dados_paciente()
        if dados:
            if self.busca_paciente_por_cpf(dados["cpf"]):
                self.__controlador_principal.tela.mostra_mensagem("Erro: Já existe um paciente cadastrado com este CPF.")
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
            self.__controlador_principal.tela.mostra_mensagem("Paciente cadastrado com sucesso!")

    def listar_pacientes(self):
        if not self.__pacientes:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum paciente cadastrado.")
            return
        
        self.__controlador_principal.tela.mostrar_pacientes(self.__pacientes)

    def alterar_paciente(self):
        if not self.__pacientes:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum paciente cadastrado para alterar.")
            return

        cpf_busca = self.__controlador_principal.tela.selecionar_paciente()
        paciente = self.busca_paciente_por_cpf(cpf_busca)

        if paciente:
            novos_dados = self.__controlador_principal.tela.pegar_dados_paciente(alteracao=True)
            if novos_dados:
                paciente.nome = novos_dados["nome"]
                paciente.celular = novos_dados["celular"]
                paciente.nascimento = date(
                    novos_dados["ano_nascimento"],
                    novos_dados["mes_nascimento"],
                    novos_dados["dia_nascimento"]
                )
                self.__controlador_principal.tela.mostra_mensagem("Paciente alterado com sucesso!")
        else:
            self.__controlador_principal.tela.mostra_mensagem("Paciente não encontrado.")

    def excluir_paciente(self):
        if not self.__pacientes:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum paciente cadastrado para excluir.")
            return

        cpf_busca = self.__controlador_principal.tela.selecionar_paciente()
        paciente = self.busca_paciente_por_cpf(cpf_busca)

        if paciente:
            self.__pacientes.remove(paciente)
            self.__controlador_principal.tela.mostra_mensagem("Paciente excluído com sucesso!")
        else:
            self.__controlador_principal.tela.mostra_mensagem("Paciente não encontrado.")

    def abre_menu(self):
        while True:
            opcao = self.__controlador_principal.tela.entrando_paciente()
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
        dados = self.__controlador_principal.tela.pegar_dados_profissional()
        if dados:
            if self.busca_profissional_por_cpf(dados["cpf"]):
                self.__controlador_principal.tela.mostra_mensagem("Erro: Já existe um profissional cadastrado com este CPF.")
                return
            
            novo_profissional = Profissional(
                dados["nome"],
                dados["celular"],
                dados["cpf"],
                dados["especialidade"],
                dados["registro_profissional"]
            )
            self.__profissionais.append(novo_profissional)
            self.__controlador_principal.tela.mostra_mensagem("Profissional cadastrado com sucesso!")

    def listar_profissionais(self):
        if not self.__profissionais:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        
        self.__controlador_principal.tela.mostrar_profissionais(self.__profissionais)

    def alterar_profissional(self):
        if not self.__profissionais:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum profissional cadastrado para alterar.")
            return

        cpf_busca = self.__controlador_principal.tela.selecionar_profissional()
        profissional = self.busca_profissional_por_cpf(cpf_busca)

        if profissional:
            novos_dados = self.__controlador_principal.tela.pegar_dados_profissional(alteracao=True)
            if novos_dados:
                profissional.nome = novos_dados["nome"]
                profissional.celular = novos_dados["celular"]
                profissional.especialidade = novos_dados["especialidade"]
                profissional.registro_profissional = novos_dados["registro_profissional"]
                self.__controlador_principal.tela.mostra_mensagem("Profissional alterado com sucesso!")
        else:
            self.__controlador_principal.tela.mostra_mensagem("Profissional não encontrado.")

    def excluir_profissional(self):
        if not self.__profissionais:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum profissional cadastrado para excluir.")
            return

        cpf_busca = self.__controlador_principal.tela.selecionar_profissional()
        profissional = self.busca_profissional_por_cpf(cpf_busca)

        if profesional := profissional:
            self.__profissionais.remove(profissional)
            self.__controlador_principal.tela.mostra_mensagem("Profissional excluído com sucesso!")
        else:
            self.__controlador_principal.tela.mostra_mensagem("Profissional não encontrado.")

    def abre_menu(self):
        while True:
            opcao = self.__controlador_principal.tela.entrando_profissional()
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
        dados = self.__controlador_principal.tela.pegar_dados_tipo_atendimento()
        if dados:
            if self.busca_tipo_por_descricao(dados["descricao"]):
                self.__controlador_principal.tela.mostra_mensagem("Erro: Já existe um tipo de atendimento cadastrado com esta descrição.")
                return
            
            novo_tipo = TipoAtendimento(
                dados["descricao"],
                dados["valor_base"]
            )
            self.__tipos_atendimento.append(novo_tipo)
            self.__controlador_principal.tela.mostra_mensagem("Tipo de atendimento cadastrado com sucesso!")

    def listar_tipos_atendimento(self):
        if not self.__tipos_atendimento:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum tipo de atendimento cadastrado.")
            return
        
        self.__controlador_principal.tela.mostrar_tipos_atendimento(self.__tipos_atendimento)

    def alterar_tipo_atendimento(self):
        if not self.__tipos_atendimento:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum tipo de atendimento cadastrado para alterar.")
            return

        descricao_busca = self.__controlador_principal.tela.selecionar_tipo_atendimento()
        tipo = self.busca_tipo_por_descricao(descricao_busca)

        if tipo:
            novos_dados = self.__controlador_principal.tela.pegar_dados_tipo_atendimento(alteracao=True)
            if novos_dados:
                tipo.descricao = novos_dados["descricao"]
                tipo.valor_base = novos_dados["valor_base"]
                self.__controlador_principal.tela.mostra_mensagem("Tipo de atendimento alterado com sucesso!")
        else:
            self.__controlador_principal.tela.mostra_mensagem("Tipo de atendimento não encontrado.")

    def excluir_tipo_atendimento(self):
        if not self.__tipos_atendimento:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum tipo de atendimento cadastrado para excluir.")
            return

        descricao_busca = self.__controlador_principal.tela.selecionar_tipo_atendimento()
        tipo = self.busca_tipo_por_descricao(descricao_busca)

        if tipo:
            self.__tipos_atendimento.remove(tipo)
            self.__controlador_principal.tela.mostra_mensagem("Tipo de atendimento excluído com sucesso!")
        else:
            self.__controlador_principal.tela.mostra_mensagem("Tipo de atendimento não encontrado.")

    def abre_menu(self):
        while True:
            opcao = self.__controlador_principal.tela.entrando_tipo_atendimento()
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


class ControladorAtendimento:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__atendimentos = []

    @property
    def atendimentos(self):
        return self.__atendimentos

    def incluir_atendimento(self):
        # Validação inicial: precisamos ter clínicas, pacientes, profissionais e tipos de atendimento cadastrados
        if not self.__controlador_principal.controlador_clinica.clinicas:
            self.__controlador_principal.tela.mostra_mensagem("Erro: Não há clínicas cadastradas.")
            return
        if not self.__controlador_principal.controlador_paciente.pacientes:
            self.__controlador_principal.tela.mostra_mensagem("Erro: Não há pacientes cadastrados.")
            return
        if not self.__controlador_principal.controlador_profissional.profissionais:
            self.__controlador_principal.tela.mostra_mensagem("Erro: Não há profissionais cadastrados.")
            return
        if not self.__controlador_principal.controlador_tipo_atendimento.tipos_atendimento:
            self.__controlador_principal.tela.mostra_mensagem("Erro: Não há tipos de atendimento cadastrados.")
            return

        # Selecionar Clínica
        self.__controlador_principal.controlador_clinica.listar_clinicas()
        nome_clinica = self.__controlador_principal.tela.selecionar_clinica()
        clinica = self.__controlador_principal.controlador_clinica.busca_clinica_por_nome(nome_clinica)
        if not clinica:
            self.__controlador_principal.tela.mostra_mensagem("Erro: Clínica não encontrada.")
            return

        # Selecionar Paciente
        self.__controlador_principal.controlador_paciente.listar_pacientes()
        cpf_paciente = self.__controlador_principal.tela.selecionar_paciente()
        paciente = self.__controlador_principal.controlador_paciente.busca_paciente_por_cpf(cpf_paciente)
        if not paciente:
            self.__controlador_principal.tela.mostra_mensagem("Erro: Paciente não encontrado.")
            return

        # Selecionar Profissional
        self.__controlador_principal.controlador_profissional.listar_profissionais()
        cpf_prof = self.__controlador_principal.tela.selecionar_profissional()
        profissional = self.__controlador_principal.controlador_profissional.busca_profissional_por_cpf(cpf_prof)
        if not profissional:
            self.__controlador_principal.tela.mostra_mensagem("Erro: Profissional não encontrado.")
            return

        # Selecionar Tipo de Atendimento
        self.__controlador_principal.controlador_tipo_atendimento.listar_tipos_atendimento()
        desc_tipo = self.__controlador_principal.tela.selecionar_tipo_atendimento()
        tipo = self.__controlador_principal.controlador_tipo_atendimento.busca_tipo_por_descricao(desc_tipo)
        if not tipo:
            self.__controlador_principal.tela.mostra_mensagem("Erro: Tipo de atendimento não encontrado.")
            return

        # Pegar dados de agendamento (data, horários, valor)
        dados = self.__controlador_principal.tela.pegar_dados_atendimento()
        if dados:
            data_atendimento = date(dados["ano"], dados["mes"], dados["dia"])
            horario_inicio = time(dados["hora_inicio"], dados["minuto_inicio"])
            horario_fim = time(dados["hora_fim"], dados["minuto_fim"])

            # Validar se o paciente tem 18 anos completos na data do agendamento
            nascimento = paciente.nascimento
            idade = data_atendimento.year - nascimento.year - ((data_atendimento.month, data_atendimento.day) < (nascimento.month, nascimento.day))
            if idade < 18:
                self.__controlador_principal.tela.mostra_mensagem("Erro: Pacientes menores de 18 anos não podem agendar atendimentos de forma independente.")
                return

            # Validar se o atendimento ocorre dentro do período de funcionamento da clínica
            if not (horario_inicio >= clinica.horario_inicial and horario_fim <= clinica.horario_fim):
                self.__controlador_principal.tela.mostra_mensagem(f"Erro: O atendimento deve ocorrer dentro do funcionamento da clínica ({clinica.horario_inicial.strftime('%H:%M')} às {clinica.horario_fim.strftime('%H:%M')}).")
                return
            if horario_inicio >= horario_fim:
                self.__controlador_principal.tela.mostra_mensagem("Erro: O horário de início deve ser anterior ao horário de término.")
                return

            novo_atendimento = Atendimento(
                dados["ano"], dados["mes"], dados["dia"],
                dados["hora_inicio"], dados["minuto_inicio"],
                dados["hora_fim"], dados["minuto_fim"],
                dados["valor"],
                clinica,
                paciente,
                profissional,
                tipo
            )
            self.__atendimentos.append(novo_atendimento)
            self.__controlador_principal.tela.mostra_mensagem("Atendimento agendado com sucesso!")

    def listar_atendimentos(self):
        if not self.__atendimentos:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum atendimento agendado.")
            return
        self.__controlador_principal.tela.mostrar_atendimentos(self.__atendimentos)

    def incluir_procedimento(self):
        if not self.__atendimentos:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum atendimento agendado.")
            return

        self.listar_atendimentos()
        index = self.__controlador_principal.tela.selecionar_atendimento()
        if not (0 <= index < len(self.__atendimentos)):
            self.__controlador_principal.tela.mostra_mensagem("Erro: Seleção inválida.")
            return

        atendimento = self.__atendimentos[index]

        # Selecionar Profissional Responsável pelo procedimento
        self.__controlador_principal.controlador_profissional.listar_profissionais()
        cpf_prof = self.__controlador_principal.tela.selecionar_profissional()
        profissional = self.__controlador_principal.controlador_profissional.busca_profissional_por_cpf(cpf_prof)
        if not profissional:
            self.__controlador_principal.tela.mostra_mensagem("Erro: Profissional não encontrado.")
            return

        dados = self.__controlador_principal.tela.pegar_dados_procedimento()
        if dados:
            # Chama o método do Atendimento que instancia e anexa o procedimento internamente
            atendimento.adicionar_procedimento(dados["descricao"], dados["custo"], profissional)
            self.__controlador_principal.tela.mostra_mensagem("Procedimento registrado no atendimento com sucesso!")

    def registrar_pagamento(self):
        if not self.__atendimentos:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum atendimento agendado.")
            return

        self.listar_atendimentos()
        index = self.__controlador_principal.tela.selecionar_atendimento()
        if not (0 <= index < len(self.__atendimentos)):
            self.__controlador_principal.tela.mostra_mensagem("Erro: Seleção inválida.")
            return

        atendimento = self.__atendimentos[index]
        
        # Calcular valor restante
        valor_devedor = atendimento.valor_restante()
        if valor_devedor <= 0:
            self.__controlador_principal.tela.mostra_mensagem("Este atendimento já está totalmente pago!")
            return

        self.__controlador_principal.tela.mostra_mensagem(f"Valor restante pendente: R$ {valor_devedor:.2f}")

        dados = self.__controlador_principal.tela.pegar_dados_pagamento()
        if dados:
            data_pagamento = date(dados["ano"], dados["mes"], dados["dia"])

            # Os pagamentos devem ser realizados até a data do atendimento
            if data_pagamento > atendimento.data:
                self.__controlador_principal.tela.mostra_mensagem("Erro: O pagamento não pode ser realizado em data posterior ao atendimento.")
                return

            if dados["valor"] > valor_devedor:
                self.__controlador_principal.tela.mostra_mensagem("Erro: O valor pago excede o valor restante do atendimento.")
                return

            # Cria a modalidade correta de pagamento
            pagamento = None
            if dados["tipo"] == 1: # PIX
                pagamento = PagamentoPix(data_pagamento, atendimento.paciente, dados["valor"], dados["cpf_pagador"])
            elif dados["tipo"] == 2: # Dinheiro
                pagamento = PagamentoDinheiro(data_pagamento, atendimento.paciente, dados["valor"])
            elif dados["tipo"] == 3: # Cartão
                pagamento = PagamentoCartao(data_pagamento, atendimento.paciente, dados["valor"], dados["numero_cartao"], dados["bandeira"])

            if pagamento:
                # Adiciona o pagamento no atendimento
                atendimento.adicionar_pagamento(pagamento)
                self.__controlador_principal.tela.mostra_mensagem("Pagamento registrado com sucesso!")

    def excluir_atendimento(self):
        if not self.__atendimentos:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum atendimento agendado para excluir.")
            return

        self.listar_atendimentos()
        index = self.__controlador_principal.tela.selecionar_atendimento()
        if not (0 <= index < len(self.__atendimentos)):
            self.__controlador_principal.tela.mostra_mensagem("Erro: Seleção inválida.")
            return

        self.__atendimentos.pop(index)
        self.__controlador_principal.tela.mostra_mensagem("Atendimento cancelado com sucesso!")

    def emitir_relatorios(self):
        if not self.__atendimentos:
            self.__controlador_principal.tela.mostra_mensagem("Nenhum dado cadastrado para emitir relatórios.")
            return

        # 1. Clínicas com maior número de atendimentos
        contagem_clinicas = {}
        for atend in self.__atendimentos:
            clinica = atend.clinica.nome
            contagem_clinicas[clinica] = contagem_clinicas.get(clinica, 0) + 1
        relatorio_clinicas = sorted(contagem_clinicas.items(), key=lambda item: item[1], reverse=True)

        # Atendimentos mais caros e mais baratos
        # Custo total = valor base + base do tipo + soma dos custos dos procedimentos
        def custo_total(atend):
            return atend.valor + atend.total_de_procedimentos() + atend.valor_de_atendimento()
        
        atendimentos_ordenados = sorted(self.__atendimentos, key=custo_total)
        atend_mais_barato = atendimentos_ordenados[0]
        atend_mais_caro = atendimentos_ordenados[-1]

        # Procedimentos mais realizados (mais populares)
        contagem_procedimentos = {}
        todos_procedimentos = []
        for atend in self.__atendimentos:
            for proc in atend.procedimentos:
                todos_procedimentos.append(proc)
                desc = proc.descricao.lower().strip()
                contagem_procedimentos[desc] = contagem_procedimentos.get(desc, 0) + 1
        relatorio_procedimentos_pop = sorted(contagem_procedimentos.items(), key=lambda item: item[1], reverse=True)

        # Procedimentos mais caros e mais baratos
        proc_mais_caro = None
        proc_mais_barato = None
        if todos_procedimentos:
            todos_procedimentos_ordenados = sorted(todos_procedimentos, key=lambda p: p.custo)
            proc_mais_barato = todos_procedimentos_ordenados[0]
            proc_mais_caro = todos_procedimentos_ordenados[-1]

        # Exibe os relatórios consolidados
        self.__controlador_principal.tela.mostrar_relatorios(
            relatorio_clinicas,
            custo_total(atend_mais_barato), atend_mais_barato,
            custo_total(atend_mais_caro), atend_mais_caro,
            relatorio_procedimentos_pop,
            proc_mais_barato,
            proc_mais_caro
        )

    def abre_menu(self):
        while True:
            opcao = self.__controlador_principal.tela.entrando_atendimento()
            if opcao == 1:
                self.incluir_atendimento()
            elif opcao == 2:
                self.listar_atendimentos()
            elif opcao == 3:
                self.incluir_procedimento()
            elif opcao == 4:
                self.registrar_pagamento()
            elif opcao == 5:
                self.excluir_atendimento()
            elif opcao == 6:
                self.emitir_relatorios()
            elif opcao == 7:
                break


class ControladorPrincipal:
    def __init__(self):
        self.__tela = TelaApp()
        self.__controlador_clinica = ControladorClinica(self)
        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_profissional = ControladorProfissional(self)
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento(self)
        self.__controlador_atendimento = ControladorAtendimento(self)

    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_clinica(self):
        return self.__controlador_clinica

    @property
    def controlador_paciente(self):
        return self.__controlador_paciente

    @property
    def controlador_profissional(self):
        return self.__controlador_profissional

    @property
    def controlador_tipo_atendimento(self):
        return self.__controlador_tipo_atendimento

    @property
    def controlador_atendimento(self):
        return self.__controlador_atendimento

    def inicializa_sistema(self):
        while True:
            opcao = self.__tela.inicializacao()
            if opcao == 1:
                self.__controlador_paciente.abre_menu()
            elif opcao == 2:
                self.__controlador_clinica.abre_menu()
            elif opcao == 3:
                self.__controlador_profissional.abre_menu()
            elif opcao == 4:
                self.__controlador_tipo_atendimento.abre_menu()
            elif opcao == 5:
                self.__controlador_atendimento.abre_menu()
            elif opcao == 0:
                self.__tela.mostra_mensagem("Obrigado por usar o sistema!")
                break
            else:
                self.__tela.mostra_mensagem("Opção inválida.")
