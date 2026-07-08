import FreeSimpleGUI as sg
from view_v.tela import TelaApp

class TelaAtendimento(TelaApp):

    def __init__(self):
        self.__nada = None

    def entrando_atendimento(self) -> int:
        layout = [
        [sg.Text("MENU DE ATENDIMENTOS",
                 font=("Arial",18,"bold"),
                 justification="center",
                 expand_x=True)],

        [sg.HorizontalSeparator()],

        [sg.Button("Agendar novo atendimento",
                   key="1",
                   size=(35,2))],

        [sg.Button("Listar atendimentos agendados",
                   key="2",
                   size=(35,2))],

        [sg.Button("Adicionar procedimento",
                   key="3",
                   size=(35,2))],

        [sg.Button("Registrar pagamento",
                   key="4",
                   size=(35,2))],

        [sg.Button("Cancelar/Excluir atendimento",
                   key="5",
                   size=(35,2))],

        [sg.Button("Emitir relatórios consolidados",
                   key="6",
                   size=(35,2))],

        [sg.HorizontalSeparator()],

        [sg.Button("Voltar",
                   key="7",
                   button_color=("white","firebrick"),
                   size=(15,1))]
        ]

        window = sg.Window(
            "Menu de Atendimentos",
            layout,
            element_justification="center",
            finalize=True
        )

        while True:

            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "7"):
                window.close()
                return 7

            if event in ("1","2","3","4","5","6"):
                window.close()
                return int(event)
            
    def pegar_dados_atendimento(self) -> dict:
        layout = [[sg.Text("Ano:"), sg.Input(key="ano", size=(8,1))],
            [sg.Text("Mês:"), sg.Input(key="mes", size=(8,1))],
            [sg.Text("Dia:"), sg.Input(key="dia", size=(8,1))],
            [sg.HorizontalSeparator()],
            [sg.Text("Hora início:"), sg.Input(key="hi", size=(8,1))],
            [sg.Text("Minuto início:"), sg.Input(key="mi", size=(8,1))],
            [sg.Text("Hora fim:"), sg.Input(key="hf", size=(8,1))],
            [sg.Text("Minuto fim:"), sg.Input(key="mf", size=(8,1))],
            [sg.HorizontalSeparator()],
            [sg.Text("Valor (R$):"), sg.Input(key="valor")],
            [sg.Button("Salvar"), sg.Button("Cancelar")]]

        window = sg.Window("Cadastro de Atendimento", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Salvar":
                try:
                    ano = int(values["ano"])
                    if ano < 2020:
                        raise ValueError("Ano inválido.")
                    mes = int(values["mes"])
                    if not (1 <= mes <= 12):
                        raise ValueError("Mês inválido.")
                    dia = int(values["dia"])
                    if not (1 <= dia <= 31):
                        raise ValueError("Dia inválido.")
                    hora_inicio = int(values["hi"])
                    if not (0 <= hora_inicio <= 23):
                        raise ValueError("Hora inicial inválida.")
                    minuto_inicio = int(values["mi"])
                    if not (0 <= minuto_inicio <= 59):
                        raise ValueError("Minuto inicial inválido.")
                    hora_fim = int(values["hf"])
                    if not (0 <= hora_fim <= 23):
                        raise ValueError("Hora final inválida.")
                    minuto_fim = int(values["mf"])
                    if not (0 <= minuto_fim <= 59):
                        raise ValueError("Minuto final inválido.")
                    valor = float(values["valor"])
                    if valor < 0:
                        raise ValueError("Valor inválido.")

                    window.close()

                    return {"ano": ano,
                        "mes": mes,
                        "dia": dia,
                        "hora_inicio": hora_inicio,
                        "minuto_inicio": minuto_inicio,
                        "hora_fim": hora_fim,
                        "minuto_fim": minuto_fim,
                        "valor": valor}

                except ValueError as e:
                    sg.popup_error(e)
                    return None

    def mostrar_atendimentos(self, atendimentos: list):
        dados = []

        for idx, a in enumerate(atendimentos):
            dados.append([idx,a.data.strftime("%d/%m/%Y"),
                f"{a.horario_inicio.strftime('%H:%M')} - {a.horario_fim.strftime('%H:%M')}",
                a.clinica.nome,a.paciente.nome,
                f"R$ {a.valor_restante():.2f}"])

        layout = [[sg.Table(values=dados,headings=["ID","Data","Horário","Clínica","Paciente","Valor Restante"],
                    auto_size_columns=True,justification="center",expand_x=True,expand_y=True,
                    num_rows=min(len(dados), 15),key="-TABLE-")],
                [sg.Button("Prosseguir")]]

        window = sg.Window("Atendimentos", layout, resizable=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Prosseguir"):
                break
        window.close()

    def selecionar_atendimento(self) -> int:
        layout = [[sg.Text("Número do atendimento (IND)")],
        [sg.Input(key="indice")],
        [sg.Button("Selecionar"),sg.Button("Cancelar")]]

        window = sg.Window("Selecionar Atendimento", layout)

        event, values = window.read()
        window.close()

        if event != "Selecionar":
            return -1
        try:
            return int(values["indice"])
        except ValueError:
            sg.popup_error("Digite um número válido.")
            return -1

    def pegar_dados_procedimento(self) -> dict:

        layout = [[sg.Text("Descrição:"), sg.Input(key="descricao")],
            [sg.Text("Custo (R$):"), sg.Input(key="custo")],
            [sg.Button("Salvar"), sg.Button("Cancelar")]]

        window = sg.Window("Adicionar Procedimento", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Salvar":
                try:
                    descricao = values["descricao"].strip()
                    if not descricao:
                        raise ValueError("Informe a descrição.")
                    custo = float(values["custo"])
                    if custo < 0:
                        raise ValueError("O custo não pode ser negativo.")
                    window.close()
                    return {"descricao": descricao,
                        "custo": custo}
                except ValueError as e:
                    sg.popup_error(e)
                    return None
    
    def mostrar_relatorios(self,rel_clinicas,custo_barato,atend_barato,
        custo_caro,atend_caro,rel_procedimentos,proc_barato,proc_caro):

        dados_clinicas = []
        for nome, qtd in rel_clinicas:
            dados_clinicas.append([nome, qtd])

        if rel_procedimentos:
            dados_procedimentos = []
            for nome, qtd in rel_procedimentos:
                dados_procedimentos.append([nome, qtd])
        else:
            dados_procedimentos = [["Nenhum procedimento registrado", ""]]

        atendimento_barato = [[atend_barato.clinica.nome,
            atend_barato.paciente.nome,
            atend_barato.data.strftime("%d/%m/%Y"),
            f"R$ {custo_barato:.2f}"]]

        atendimento_caro = [[atend_caro.clinica.nome,
            atend_caro.paciente.nome,
            atend_caro.data.strftime("%d/%m/%Y"),
            f"R$ {custo_caro:.2f}"]]

        if proc_barato and proc_caro:
            procedimentos_extremos = [["Mais barato",
                    proc_barato.descricao,
                    f"R$ {proc_barato.custo:.2f}",
                    proc_barato.profissional_responsavel.nome],
                    ["Mais caro",
                    proc_caro.descricao,
                    f"R$ {proc_caro.custo:.2f}",
                    proc_caro.profissional_responsavel.nome]]
        else:
            procedimentos_extremos = [["", "Nenhum procedimento", "", ""]]

        layout = [[sg.Text("RELATÓRIOS CONSOLIDADOS",font=("Arial",16,"bold"))],
            [sg.HorizontalSeparator()],
            [sg.Text("Clínicas com maior número de atendimentos",font=("Arial",11,"bold"))],
            [sg.Table(values=dados_clinicas,headings=["Clínica","Atendimentos"],
                        auto_size_columns=True,justification="center",num_rows=min(len(dados_clinicas),6))],
            [sg.Text("Atendimento mais barato",font=("Arial",11,"bold"))],
            [sg.Table(values=atendimento_barato,headings=["Clínica","Paciente","Data","Valor"],
                        auto_size_columns=True)],
            [sg.Text("Atendimento mais caro",font=("Arial",11,"bold"))],
            [sg.Table(values=atendimento_caro,headings=["Clínica","Paciente","Data","Valor"],
                        auto_size_columns=True)],
            [sg.Text("Procedimentos mais realizados",font=("Arial",11,"bold"))],
            [sg.Table(values=dados_procedimentos,headings=["Procedimento","Quantidade"],
                        auto_size_columns=True,justification="center",num_rows=min(len(dados_procedimentos),10))],
            [sg.Text("Procedimentos extremos",font=("Arial",11,"bold"))],
            [sg.Table(values=procedimentos_extremos,headings=["Tipo","Procedimento","Custo","Responsável"],
                        auto_size_columns=True)],
            [sg.Button("Prosseguir")]]

        window = sg.Window("Relatórios",layout,resizable=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED,"Prosseguir"):
                break
        window.close()
    
    def pegar_dados_pagamento(self):

        layout = [[sg.Text("Ano"), sg.Input(key="ano", size=(8,1))],
            [sg.Text("Mês"), sg.Input(key="mes", size=(8,1))],
            [sg.Text("Dia"), sg.Input(key="dia", size=(8,1))],
            [sg.Text("Valor (R$)"), sg.Input(key="valor")],
            [sg.Text("Forma de pagamento"),sg.Combo(["PIX", "Dinheiro", "Cartão de Crédito"],
                    key="tipo",readonly=True)],
            [sg.Text("CPF Pagador"), sg.Input(key="cpf")],
            [sg.Text("Número Cartão"), sg.Input(key="cartao")],
            [sg.Text("Bandeira"), sg.Input(key="bandeira")],
            [sg.Button("Salvar"), sg.Button("Cancelar")]]

        window = sg.Window("Registrar Pagamento", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Salvar":
                try:
                    ano = int(values["ano"])
                    mes = int(values["mes"])
                    dia = int(values["dia"])
                    valor = float(values["valor"])
                    if valor <= 0:
                        raise ValueError("Valor inválido.")
                    mapa = {"PIX": 1,
                        "Dinheiro": 2,
                        "Cartão de Crédito": 3}
                    tipo = mapa[values["tipo"]]
                    cpf = values["cpf"].strip()
                    cartao = values["cartao"].strip()
                    bandeira = values["bandeira"].strip()
                    if tipo == 1 and not cpf:
                        raise ValueError("Informe o CPF.")
                    if tipo == 3:
                        if not cartao:
                            raise ValueError("Informe o cartão.")
                        if not bandeira:
                            raise ValueError("Informe a bandeira.")
                    window.close()

                    return {"ano": ano,
                        "mes": mes,
                        "dia": dia,
                        "valor": valor,
                        "tipo": tipo,
                        "cpf_pagador": cpf,
                        "numero_cartao": cartao,
                        "bandeira": bandeira}

                except ValueError as e:
                    sg.popup_error(e)
                    return None
