import FreeSimpleGUI as sg

class TelaApp:

    def __init__(self):
        self.__nada = None

    def inicializacao(self) -> int:

        layout = [[sg.Text("SISTEMA DE GERENCIAMENTO CLÍNICO",
                    font=("Arial", 18, "bold"),justification="center",expand_x=True)],
            [sg.HorizontalSeparator()],
            [sg.Button("Gerenciar Pacientes",key="1",size=(35,2))],
            [sg.Button("Gerenciar Clínicas",key="2",size=(35,2))],
            [sg.Button("Gerenciar Profissionais",key="3",size=(35,2))],
            [sg.Button("Gerenciar Tipos de Atendimento",key="4",size=(35,2))],
            [sg.Button("Gerenciar Atendimentos e Relatórios",key="5",size=(35,2))],
            [sg.HorizontalSeparator()],
            [sg.Button("Sair",key="0",button_color=("white", "firebrick"),size=(15,1))]]

        window = sg.Window("Sistema Clínico",layout,element_justification="center",finalize=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "0"):
                window.close()
                return 0
            if event in ("1", "2", "3", "4", "5"):
                window.close()
                return int(event)
    
    def entrando_clinica(self) -> int:
        layout = [
        [sg.Text("1) Cadastrar nova clínica")],
        [sg.Text("2) Listar clínicas cadastradas")],
        [sg.Text("3) Alterar clínica cadastrada")],
        [sg.Text("4) Remover clínica cadastrada")],
        [sg.Text("5) Retornar ao menu anterior")],
        [sg.Text('Opção:'),sg.InputText("")],
        [sg.Submit()]
        ]

        window = sg.Window("MENU DE CLÍNICAS").Layout(layout)

        button, values = window.Read()

        if button=='Submit':
            entrada=values[0]
            try:
                opcao = int(entrada)

                window.close()
                return opcao
            except ValueError:
                return -1
    
    def entrando_paciente(self) -> int:
        layout = [
        [sg.Text("1) Cadastrar novo paciente")],
        [sg.Text("2) Listar pacientes cadastrados")],
        [sg.Text("3) Alterar paciente cadastrado")],
        [sg.Text("4) Remover paciente cadastrado")],
        [sg.Text("5) Retornar ao menu anterior")],
        [sg.Text('Opção:'),sg.InputText("")],
        [sg.Submit()]
        ]

        window = sg.Window("MENU DE PACIENTES").Layout(layout)

        button, values = window.Read()

        if button=='Submit':
            entrada=values[0]
            try:
                opcao = int(entrada)
                window.close()
                return opcao
            except ValueError:
                return -1
    
    def entrando_profissional(self) -> int:
        layout = [
        [sg.Text("1) Cadastrar novo profissional")],
        [sg.Text("2) Listar profissionais cadastrados")],
        [sg.Text("3) Alterar profissional cadastrado")],
        [sg.Text("4) Remover profissional cadastrado")],
        [sg.Text("5) Retornar ao menu anterior")],
        [sg.Text('Opção:'),sg.InputText("")],
        [sg.Submit()]
        ]

        window = sg.Window("MENU DE PROFISSIONAIS").Layout(layout)

        button, values = window.Read()

        if button=='Submit':
            entrada=values[0]
            try:
                opcao = int(entrada)
                window.close()
                return opcao
            except ValueError:
                return -1
    
    def entrando_tipo_atendimento(self) -> int:
        layout = [
        [sg.Text("1) Cadastrar novo tipo de atendimento")],
        [sg.Text("2) Listar tipos de atendimento")],
        [sg.Text("3) Alterar tipo de atendimento")],
        [sg.Text("4) Remover tipo de atendimento")],
        [sg.Text("5) Retornar ao menu anterior")],
        [sg.Text('Opção:'),sg.InputText("")],
        [sg.Submit()]
        ]

        window = sg.Window("MENU DE TIPOS DE ATENDIMENTO").Layout(layout)

        button, values = window.Read()

        if button=='Submit':
            entrada=values[0]
            try:
                opcao = int(entrada)
                window.close()
                return opcao
            except ValueError:
                return -1
    
    def entrando_atendimento(self) -> int:
        layout = [
        [sg.Text("1) Agendar novo atendimento")],
        [sg.Text("2) Listar atendimentos agendados")],
        [sg.Text("3) Adicionar procedimento a um atendimento")],
        [sg.Text("4) Registrar pagamento de um atendimento")],
        [sg.Text("5) Cancelar/Excluir um atendimento")],
        [sg.Text("6) Emitir relatórios consolidados")],
        [sg.Text("7) Retornar ao menu anterior")],
        [sg.Text('Opção:'),sg.InputText("")],
        [sg.Submit()]
        ]

        window = sg.Window("MENU DE ATENDIMENTOS").Layout(layout)

        button, values = window.Read()

        if button=='Submit':
            entrada=values[0]
            try:
                opcao = int(entrada)
                window.close()
                return opcao
            except ValueError:
                return -1
    
    def mostra_mensagem(self, mensagem: str):
        sg.Popup("Aviso", mensagem)
    
    def pegar_dados_clinica(self, alteracao=False) -> dict:
        if alteracao:
            titulo = "Alterando Clínica"
        else:
            titulo = "Cadastro de Nova Clínica"

        layout = [
            [sg.Text("Nome da Clínica:", size=(25,1)),
            sg.Input(key="nome")],
            [sg.Text("Cidade:", size=(25,1)),
            sg.Input(key="cidade")],
            [sg.Text("Descrição/Especialidade:", size=(25,1)),
            sg.Input(key="descricao")],
            [sg.Text("Hora de abertura (0-23):", size=(25,1)),
            sg.Input(key="hora_abertura")],
            [sg.Text("Minuto de abertura (0-59):", size=(25,1)),
            sg.Input(key="minuto_abertura")],
            [sg.Text("Hora de fechamento (0-23):", size=(25,1)),
            sg.Input(key="hora_fechamento")],
            [sg.Text("Minuto de fechamento (0-59):", size=(25,1)),
            sg.Input(key="minuto_fechamento")],
            [sg.Button("Salvar"), sg.Button("Cancelar")]
        ]

        window = sg.Window(titulo, layout)

        while True:

            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None

            if event == "Salvar":

                try:

                    nome = values["nome"].strip()
                    cidade = values["cidade"].strip()
                    descricao = values["descricao"].strip()

                    if not nome:
                        raise ValueError("O nome não pode ser vazio.")

                    if not cidade:
                        raise ValueError("A cidade não pode ser vazia.")

                    if not descricao:
                        raise ValueError("A descrição não pode ser vazia.")

                    hora_abertura = int(values["hora_abertura"])

                    if not (0 <= hora_abertura <= 23):
                        raise ValueError("Hora de abertura deve ser entre 0 e 23.")

                    minuto_abertura = int(values["minuto_abertura"])

                    if not (0 <= minuto_abertura <= 59):
                        raise ValueError("Minuto de abertura deve ser entre 0 e 59.")

                    hora_fechamento = int(values["hora_fechamento"])

                    if not (0 <= hora_fechamento <= 23):
                        raise ValueError("Hora de fechamento deve ser entre 0 e 23.")

                    minuto_fechamento = int(values["minuto_fechamento"])

                    if not (0 <= minuto_fechamento <= 59):
                        raise ValueError("Minuto de fechamento deve ser entre 0 e 59.")

                    window.close()

                    return {
                        "nome": nome,
                        "cidade": cidade,
                        "descricao": descricao,
                        "hora_abertura": hora_abertura,
                        "minuto_abertura": minuto_abertura,
                        "hora_fechamento": hora_fechamento,
                        "minuto_fechamento": minuto_fechamento
                    }

                except ValueError as e:
                    sg.popup_error(f"Entrada inválida:\n{e}")
    
    def pegar_dados_paciente(self, alteracao=False) -> dict:
        if alteracao:
            titulo = "Alterando Paciente"
        else:
            titulo = "Cadastro de Novo Paciente"

        layout = [
            [sg.Text("Nome do Paciente:", size=(25,1)),
            sg.Input(key="nome")],
            [sg.Text("Celular:", size=(25,1)),
            sg.Input(key="celular")],
            [sg.Text("CPF:", size=(25,1)),
            sg.Input(key="cpf")],
            [sg.Text("Ano de Nascimento (ex: 1995):", size=(25,1)),
            sg.Input(key="ano_nascimento")],
            [sg.Text("Mês de Nascimento (1-12):", size=(25,1)),
            sg.Input(key="mes_nascimento")],
            [sg.Text("Dia de Nascimento (1-31):", size=(25,1)),
            sg.Input(key="dia_nascimento")],
            [sg.Button("Salvar"), sg.Button("Cancelar")]
        ]

        window = sg.Window(titulo, layout)

        while True:

            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None

            if event == "Salvar":

                try:

                    nome = values["nome"].strip()
                    celular = values["celular"].strip()
                    cpf = values["cpf"].strip()

                    if not nome:
                        raise ValueError("O nome não pode ser vazio.")

                    if not celular:
                        raise ValueError("O celular não pode ser vazio.")

                    if not cpf:
                        raise ValueError("O CPF não pode ser vazio.")

                    ano = int(values["ano_nascimento"])
                    if ano < 1900 or ano > 2026:
                        raise ValueError("Ano de nascimento inválido.")

                    mes = int(values["mes_nascimento"])
                    if not (1 <= mes <= 12):
                        raise ValueError("Mês de nascimento deve ser entre 1 e 12.")

                    dia = int(values["dia_nascimento"])
                    if not (1 <= dia <= 31):
                        raise ValueError("Dia de nascimento deve ser entre 1 e 31.")

                    window.close()

                    return {
                        "nome": nome,
                        "celular": celular,
                        "cpf": cpf,
                        "ano_nascimento": ano,
                        "mes_nascimento": mes,
                        "dia_nascimento": dia
                    }

                except ValueError as e:
                    sg.popup_error(f"Entrada inválida:\n{e}")
    
    def pegar_dados_profissional(self, alteracao=False) -> dict:
        if alteracao:
            titulo = "Alterando Profissional"
        else:
            titulo = "Cadastro de Novo Profissional"

        layout = [
            [sg.Text("Nome do Paciente:", size=(25,1)),
            sg.Input(key="nome")],
            [sg.Text("Celular:", size=(25,1)),
            sg.Input(key="celular")],
            [sg.Text("CPF:", size=(25,1)),
            sg.Input(key="cpf")],
            [sg.Text("Especialidade:", size=(25,1)),
            sg.Input(key="especialidade")],
            [sg.Text("Registro Profissional (ex: CRM, CREFITO):", size=(25,1)),
            sg.Input(key="registro_profissional")],
            [sg.Button("Salvar"), sg.Button("Cancelar")]
        ]

        window = sg.Window(titulo, layout)

        while True:

            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None

            if event == "Salvar":

                try:

                    nome = values["nome"].strip()
                    celular = values["celular"].strip()
                    cpf = values["cpf"].strip()
                    especialidade = values["especialidade"].strip()
                    registro_profissional = values["registro_profissional"].strip()

                    if not nome:
                        raise ValueError("O nome não pode ser vazio.")

                    if not celular:
                        raise ValueError("O celular não pode ser vazio.")

                    if not cpf:
                        raise ValueError("O CPF não pode ser vazio.")

                    if not especialidade:
                        raise ValueError("A especialidade não pode ser vazia.")

                    if not registro_profissional:
                        raise ValueError("O registro profissional não pode ser vazio.")

                    window.close()

                    return {
                        "nome": nome,
                        "celular": celular,
                        "cpf": cpf,
                        "especialidade": especialidade,
                        "registro_profissional": registro_profissional
                    }

                except ValueError as e:
                    sg.popup_error(f"Entrada inválida:\n{e}")
    
    def pegar_dados_tipo_atendimento(self, alteracao=False) -> dict:
        if alteracao:
            titulo = "Alterando Tipo de Atendimento"
        else:
            titulo = "Cadastro de Novo Tipo de Atendimento"

        layout = [[sg.Text("Descrição (ex: Consulta, Exame, Retorno):", size=(25,1)),
            sg.Input(key="descricao")],
            [sg.Text("Valor Base (R$):", size=(25,1)),
            sg.Input(key="valor_base")]]

        window = sg.Window(titulo, layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Salvar":
                try:
                    descricao = values["descricao"].strip()
                    valor_base = values["valor_base"].strip()
                    if not descricao:
                        raise ValueError("A descrição não pode ser vazia.")
                    if valor_base < 0:
                        raise ValueError("O valor base não pode ser negativo.")
                    window.close()
                    return {"descricao": descricao,
                        "valor_base": valor_base}
                except ValueError as e:
                    sg.popup_error(f"Entrada inválida:\n{e}")
    
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
    
    def mostrar_clinicas(self, clinicas):
        dados = []
        for c in clinicas:
            dados.append([c.nome,c.cidade,c.descricao,
                f"{c.horario_inicial.strftime('%H:%M')} - {c.horario_fim.strftime('%H:%M')}"])
            
        layout = [[sg.Table(values=dados,headings=["Nome","Cidade","Descrição","Funcionamento"],
                auto_size_columns=True,justification="center",expand_x=True,expand_y=True)],
                [sg.Button("Fechar")]]

        window = sg.Window("Clínicas", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break
        window.close()
    
    def mostrar_pacientes(self, pacientes: list):

        dados = []

        for pac in pacientes:
            dados.append([pac.nome,pac.cpf,pac.celular,pac.nascimento.strftime("%d/%m/%Y")])

        layout = [[sg.Table(values=dados,headings=["Nome", "CPF", "Celular", "Nascimento"],
                    auto_size_columns=True,justification="center",expand_x=True,expand_y=True,
                    num_rows=min(len(dados), 15),key="-TABLE-")],
                    [sg.Button("Fechar")]]

        window = sg.Window("Pacientes", layout, resizable=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break
        window.close()
    
    def mostrar_profissionais(self, profissionais: list):
        dados = []

        for prof in profissionais:
            dados.append([prof.nome,prof.cpf,prof.celular,prof.especialidade,prof.registro_profissional])

        layout = [[sg.Table(values=dados,headings=["Nome","CPF","Celular","Especialidade","Registro"],
                    auto_size_columns=True,justification="center",expand_x=True,expand_y=True,
                    num_rows=min(len(dados), 15),key="-TABLE-")],
                    [sg.Button("Fechar")]]

        window = sg.Window("Profissionais", layout, resizable=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break
        window.close()
    
    def mostrar_tipos_atendimento(self, tipos: list):
        dados = []

        for t in tipos:
            dados.append([t.descricao,f"R$ {t.valor_base:.2f}"])

        layout =[[sg.Table(values=dados,headings=["Descrição","Valor Base"],
                    auto_size_columns=True,justification="center",
                    expand_x=True,expand_y=True,num_rows=min(len(dados), 15),
                    key="-TABLE-")],
                [sg.Button("Fechar")]]

        window = sg.Window("Tipos de Atendimento", layout, resizable=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break
        window.close()
    
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
                [sg.Button("Fechar")]]

        window = sg.Window("Atendimentos", layout, resizable=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break
        window.close()
    
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
                        auto_size_columns=True,justification="center",num_rows=min(len(dados_procedimentos),6))],
            [sg.Text("Procedimentos extremos",font=("Arial",11,"bold"))],
            [sg.Table(values=procedimentos_extremos,headings=["Tipo","Procedimento","Custo","Responsável"],
                        auto_size_columns=True)],
            [sg.Button("Fechar")]]

        window = sg.Window("Relatórios",layout,resizable=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED,"Fechar"):
                break
        window.close()

    def selecionar_clinica(self) -> str:

        layout = [[sg.Text("Nome da clínica")],
            [sg.Input(key="nome")],
            [sg.Button("Selecionar"),sg.Button("Cancelar")]]

        window = sg.Window("Selecionar Clínica", layout)

        event, values = window.read()

        window.close()

        if event == "Selecionar":
            return values["nome"].strip()
        return ""

    def selecionar_paciente(self) -> str:

        layout = [[sg.Text("CPF do paciente")],
            [sg.Input(key="cpf")],
            [sg.Button("Selecionar"),sg.Button("Cancelar")]]

        window = sg.Window("Selecionar Paciente", layout)

        event, values = window.read()

        window.close()

        if event == "Selecionar":
            return values["cpf"].strip()
        return ""

    def selecionar_profissional(self) -> str:

        layout = [[sg.Text("CPF do profissional")],
            [sg.Input(key="cpf")],
            [sg.Button("Selecionar"),sg.Button("Cancelar")]]

        window = sg.Window("Selecionar Profissional", layout)

        event, values = window.read()

        window.close()

        if event == "Selecionar":
            return values["cpf"].strip()
        return ""

    def selecionar_tipo_atendimento(self) -> str:
        layout = [[sg.Text("Descrição do tipo de atendimento")],
        [sg.Input(key="descricao")],
        [sg.Button("Selecionar"),sg.Button("Cancelar")]]

        window = sg.Window("Selecionar Tipo", layout)

        event, values = window.read()

        window.close()

        if event == "Selecionar":
            return values["descricao"].strip()
        return ""

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