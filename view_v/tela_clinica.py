import FreeSimpleGUI as sg
from view_v.tela import TelaApp

class TelaClinica(TelaApp):

    def __init__(self):
        self.__nada = None

    def entrando_clinica(self) -> int:

        layout = [
            [sg.Text("MENU DE CLÍNICAS",
                    font=("Arial",18,"bold"),
                    justification="center",
                    expand_x=True)],

            [sg.HorizontalSeparator()],

            [sg.Button("Cadastrar nova clínica",
                    key="1",
                    size=(35,2))],

            [sg.Button("Listar clínicas cadastradas",
                    key="2",
                    size=(35,2))],

            [sg.Button("Alterar clínica cadastrada",
                    key="3",
                    size=(35,2))],

            [sg.Button("Remover clínica cadastrada",
                    key="4",
                    size=(35,2))],

            [sg.HorizontalSeparator()],

            [sg.Button("Voltar",
                    key="5",
                    button_color=("white","firebrick"),
                    size=(15,1))]
        ]

        window = sg.Window(
            "Menu de Clínicas",
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
    
    def mostrar_clinicas(self, clinicas):
        dados = []
        for c in clinicas:
            dados.append([c.nome,c.cidade,c.descricao,
                f"{c.horario_inicial.strftime('%H:%M')} - {c.horario_fim.strftime('%H:%M')}"])
            
        layout = [[sg.Table(values=dados,headings=["Nome","Cidade","Descrição","Funcionamento"],
                auto_size_columns=True,justification="center",expand_x=True,expand_y=True)],
                [sg.Button("Prosseguir")]]

        window = sg.Window("Clínicas", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Prosseguir"):
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
    