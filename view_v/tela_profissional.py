import FreeSimpleGUI as sg
from view_v.tela import TelaApp

class TelaProfissional(TelaApp):

    def __init__(self):
        self.__nada = None
    
    def entrando_profissional(self) -> int:

        layout = [
            [sg.Text("MENU DE PROFISSIONAIS",
                    font=("Arial",18,"bold"),
                    justification="center",
                    expand_x=True)],

            [sg.HorizontalSeparator()],

            [sg.Button("Cadastrar novo profissional",
                    key="1",
                    size=(35,2))],

            [sg.Button("Listar profissionais cadastrados",
                    key="2",
                    size=(35,2))],

            [sg.Button("Alterar profissional cadastrado",
                    key="3",
                    size=(35,2))],

            [sg.Button("Remover profissional cadastrado",
                    key="4",
                    size=(35,2))],

            [sg.HorizontalSeparator()],

            [sg.Button("Voltar",
                    key="5",
                    button_color=("white","firebrick"),
                    size=(15,1))]
        ]

        window = sg.Window(
            "Menu de Profissionais",
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

    def pegar_dados_profissional(self, alteracao=False) -> dict:
        if alteracao:
            titulo = "Alterando Profissional"
        else:
            titulo = "Cadastro de Novo Profissional"

        layout = [
            [sg.Text("Nome do Profissional:", size=(25,1)),
            sg.Input(key="nome")],
            [sg.Text("Celular:", size=(25,1)),
            sg.Input(key="celular")],
            [sg.Text("CPF:", size=(25,1)),
            sg.Input(key="cpf")],
            [sg.Text("Especialidade:", size=(25,1)),
            sg.Input(key="especialidade")],
            [sg.Text("Registro Profissional (ex: CRM, CREFITO):", size=(30,1)),
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

    def mostrar_profissionais(self, profissionais: list):
        dados = []

        for prof in profissionais:
            dados.append([prof.nome,prof.cpf,prof.celular,prof.especialidade,prof.registro_profissional])

        layout = [[sg.Table(values=dados,headings=["Nome","CPF","Celular","Especialidade","Registro"],
                    auto_size_columns=True,justification="center",expand_x=True,expand_y=True,
                    num_rows=min(len(dados), 15),key="-TABLE-")],
                    [sg.Button("Prosseguir")]]

        window = sg.Window("Profissionais", layout, resizable=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Prosseguir"):
                break
        window.close()

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


