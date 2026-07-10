from model_m.atendimento import Atendimento
from model_m.pagamento import PagamentoPix, PagamentoCartao, PagamentoDinheiro
from daos.dao_atendimento import AtendimentoDAO
from datetime import time, date

class ControladorAtendimento:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__atendimentos_dao = AtendimentoDAO()

    @property
    def atendimentos(self):
        return list(self.__atendimentos_dao.get_all())

    def incluir_atendimento(self):
        if not self.__controlador_principal.controlador_clinica.clinicas:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: Não há clínicas cadastradas.")
            return
        if not self.__controlador_principal.controlador_paciente.pacientes:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: Não há pacientes cadastrados.")
            return
        if not self.__controlador_principal.controlador_profissional.profissionais:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: Não há profissionais cadastrados.")
            return
        if not self.__controlador_principal.controlador_tipo_atendimento.tipos_atendimento:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: Não há tipos de atendimento cadastrados.")
            return

        self.__controlador_principal.controlador_clinica.listar_clinicas()
        nome_clinica = self.__controlador_principal.tela_clinica.selecionar_clinica()
        clinica = self.__controlador_principal.controlador_clinica.busca_clinica_por_nome(nome_clinica)
        if not clinica:
            self.__controlador_principal.tela_clinica.mostra_mensagem("Erro: Clínica não encontrada.")
            return

        self.__controlador_principal.controlador_paciente.listar_pacientes()
        cpf_paciente = self.__controlador_principal.tela_paciente.selecionar_paciente()
        paciente = self.__controlador_principal.controlador_paciente.busca_paciente_por_cpf(cpf_paciente)
        if not paciente:
            self.__controlador_principal.tela_paciente.mostra_mensagem("Erro: Paciente não encontrado.")
            return

        self.__controlador_principal.controlador_profissional.listar_profissionais()
        cpf_prof = self.__controlador_principal.tela_profissional.selecionar_profissional()
        profissional = self.__controlador_principal.controlador_profissional.busca_profissional_por_cpf(cpf_prof)
        if not profesional:
            self.__controlador_principal.tela_profissional.mostra_mensagem("Erro: Profissional não encontrado.")
            return

        self.__controlador_principal.controlador_tipo_atendimento.listar_tipos_atendimento()
        desc_tipo = self.__controlador_principal.tela_tipo_atendimento.selecionar_tipo_atendimento()
        tipo = self.__controlador_principal.controlador_tipo_atendimento.busca_tipo_por_descricao(desc_tipo)
        if not tipo:
            self.__controlador_principal.tela_tipo_atendimento.mostra_mensagem("Erro: Tipo de atendimento não encontrado.")
            return

        dados = self.__controlador_principal.tela_atendimento.pegar_dados_atendimento()
        if dados:
            data_atendimento = date(dados["ano"], dados["mes"], dados["dia"])
            horario_inicio = time(dados["hora_inicio"], dados["minuto_inicio"])
            horario_fim = time(dados["hora_fim"], dados["minuto_fim"])

            nascimento = paciente.nascimento
            idade = data_atendimento.year - nascimento.year - ((data_atendimento.month, data_atendimento.day) < (nascimento.month, nascimento.day))
            if idade < 18:
                self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: Pacientes menores de 18 anos não podem agendar atendimentos de forma independente.")
                return

            if not (horario_inicio >= clinica.horario_inicial and horario_fim <= clinica.horario_fim):
                self.__controlador_principal.tela_atendimento.mostra_mensagem(f"Erro: O atendimento deve ocorrer dentro do funcionamento da clínica ({clinica.horario_inicial.strftime('%H:%M')} às {clinica.horario_fim.strftime('%H:%M')}).")
                return
            if horario_inicio >= horario_fim:
                self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: O horário de início deve ser anterior ao horário de término.")
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
            self.__atendimentos_dao.add(novo_atendimento)
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Atendimento agendado com sucesso!")

    def listar_atendimentos(self):
        atendimentos = list(self.__atendimentos_dao.get_all())
        if not atendimentos:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Nenhum atendimento agendado.")
            return
        self.__controlador_principal.tela_atendimento.mostrar_atendimentos(atendimentos)

    def incluir_procedimento(self):
        atendimentos = list(self.__atendimentos_dao.get_all())
        if not atendimentos:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Nenhum atendimento agendado.")
            return

        self.listar_atendimentos()
        index = self.__controlador_principal.tela_atendimento.selecionar_atendimento()
        if not (0 <= index < len(atendimentos)):
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: Seleção inválida.")
            return

        atendimento = atendimentos[index]

        self.__controlador_principal.controlador_profissional.listar_profissionais()
        cpf_prof = self.__controlador_principal.tela_profissional.selecionar_profissional()
        profissional = self.__controlador_principal.controlador_profissional.busca_profissional_por_cpf(cpf_prof)
        if not profissional:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: Profissional não encontrado.")
            return

        dados = self.__controlador_principal.tela_atendimento.pegar_dados_procedimento()
        if dados:
            atendimento.adicionar_procedimento(dados["descricao"], dados["custo"], profissional)
            self.__atendimentos_dao.update(atendimento)
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Procedimento registrado no atendimento com sucesso!")

    def registrar_pagamento(self):
        atendimentos = list(self.__atendimentos_dao.get_all())
        if not atendimentos:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Nenhum atendimento agendado.")
            return

        self.listar_atendimentos()
        index = self.__controlador_principal.tela_atendimento.selecionar_atendimento()
        if not (0 <= index < len(atendimentos)):
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: Seleção inválida.")
            return

        atendimento = atendimentos[index]
        
        valor_devedor = atendimento.valor_restante()
        if valor_devedor <= 0:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Este atendimento já está totalmente pago!")
            return

        self.__controlador_principal.tela_atendimento.mostra_mensagem(f"Valor restante pendente: R$ {valor_devedor:.2f}")

        dados = self.__controlador_principal.tela_atendimento.pegar_dados_pagamento()
        if dados:
            data_pagamento = date(dados["ano"], dados["mes"], dados["dia"])

            if data_pagamento > atendimento.data:
                self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: O pagamento não pode ser realizado em data posterior ao atendimento.")
                return

            if dados["valor"] > valor_devedor:
                self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: O valor pago excede o valor restante do atendimento.")
                return

            pagamento = None
            if dados["tipo"] == 1: 
                pagamento = PagamentoPix(data_pagamento, atendimento.paciente, dados["valor"], dados["cpf_pagador"])
            elif dados["tipo"] == 2: 
                pagamento = PagamentoDinheiro(data_pagamento, atendimento.paciente, dados["valor"])
            elif dados["tipo"] == 3: 
                pagamento = PagamentoCartao(data_pagamento, atendimento.paciente, dados["valor"], dados["numero_cartao"], dados["bandeira"])

            if pagamento:
                atendimento.adicionar_pagamento(pagamento)
                self.__atendimentos_dao.update(atendimento)
                self.__controlador_principal.tela_atendimento.mostra_mensagem("Pagamento registrado com sucesso!")

    def excluir_atendimento(self):
        atendimentos = list(self.__atendimentos_dao.get_all())
        if not atendimentos:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Nenhum atendimento agendado para excluir.")
            return

        self.listar_atendimentos()
        index = self.__controlador_principal.tela_atendimento.selecionar_atendimento()
        if not (0 <= index < len(atendimentos)):
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Erro: Seleção inválida.")
            return

        atendimento = atendimentos[index]
        key = f"{atendimento.paciente.cpf}_{atendimento.data.strftime('%d%m%Y')}_{atendimento.horario_inicio.strftime('%H%M')}"
        self.__atendimentos_dao.remove(key)
        self.__controlador_principal.tela_atendimento.mostra_mensagem("Atendimento cancelado com sucesso!")

    def emitir_relatorios(self):
        atendimentos = list(self.__atendimentos_dao.get_all())
        if not atendimentos:
            self.__controlador_principal.tela_atendimento.mostra_mensagem("Nenhum dado cadastrado para emitir relatórios.")
            return

        contagem_clinicas = {}
        for atend in atendimentos:
            clinica = atend.clinica.nome
            contagem_clinicas[clinica] = contagem_clinicas.get(clinica, 0) + 1
        relatorio_clinicas = sorted(contagem_clinicas.items(), key=lambda item: item[1], reverse=True)

        def custo_total(atend):
            return atend.valor + atend.total_de_procedimentos() + atend.valor_de_atendimento()
        
        atendimentos_ordenados = sorted(atendimentos, key=custo_total)
        atend_mais_barato = atendimentos_ordenados[0]
        atend_mais_caro = atendimentos_ordenados[-1]

        contagem_procedimentos = {}
        todos_procedimentos = []
        for atend in atendimentos:
            for proc in atend.procedimentos:
                todos_procedimentos.append(proc)
                desc = proc.descricao.lower().strip()
                contagem_procedimentos[desc] = contagem_procedimentos.get(desc, 0) + 1
        relatorio_procedimentos_pop = sorted(contagem_procedimentos.items(), key=lambda item: item[1], reverse=True)

        proc_mais_caro = None
        proc_mais_barato = None
        if todos_procedimentos:
            todos_procedimentos_ordenados = sorted(todos_procedimentos, key=lambda p: p.custo)
            proc_mais_barato = todos_procedimentos_ordenados[0]
            proc_mais_caro = todos_procedimentos_ordenados[-1]

        self.__controlador_principal.tela_atendimento.mostrar_relatorios(
            relatorio_clinicas,
            custo_total(atend_mais_barato), atend_mais_barato,
            custo_total(atend_mais_caro), atend_mais_caro,
            relatorio_procedimentos_pop,
            proc_mais_barato,
            proc_mais_caro
        )

    def abre_menu(self):
        while True:
            opcao = self.__controlador_principal.tela_atendimento.entrando_atendimento()
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

