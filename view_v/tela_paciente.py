import FreeSimpleGUI as sg
from view_v.tela import TelaApp

class TelaPaciente(TelaApp):

    def __init__(self):
        self.__nada = None
    
    def entrando_paciente(self) -> int:
        layout = [
        [sg.Text("MENU DE PACIENTES",
                 font=("Arial",18,"bold"),
                 justification="center",
                 expand_x=True)],

        [sg.HorizontalSeparator()],

        [sg.Button("Cadastrar novo paciente",
                   key="1",
                   size=(35,2))],

        [sg.Button("Listar pacientes cadastrados",
                   key="2",
                   size=(35,2))],

        [sg.Button("Alterar paciente cadastrado",
                   key="3",
                   size=(35,2))],

        [sg.Button("Remover paciente cadastrado",
                   key="4",
                   size=(35,2))],

        [sg.HorizontalSeparator()],

        [sg.Button("Voltar",
                   key="5",
                   button_color=("white","firebrick"),
                   size=(15,1))]
        ]

        window = sg.Window(
            "Menu de Pacientes",
            layout,
            element_justification="center",
            finalize=True
        )

        while True:

            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "5"):
                window.close()
                return 5

            if event in ("1","2","3","4"):
                window.close()
                return int(event)

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

    def mostrar_pacientes(self, pacientes: list):

        dados = []

        for pac in pacientes:
            dados.append([pac.nome,pac.cpf,pac.celular,pac.nascimento.strftime("%d/%m/%Y")])

        layout = [[sg.Table(values=dados,headings=["Nome", "CPF", "Celular", "Nascimento"],
                    auto_size_columns=True,justification="center",expand_x=True,expand_y=True,
                    num_rows=min(len(dados), 15),key="-TABLE-")],
                    [sg.Button("Prosseguir")]]

        window = sg.Window("Pacientes", layout, resizable=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Prosseguir"):
                break
        window.close()

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
