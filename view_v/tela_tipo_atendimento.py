import FreeSimpleGUI as sg
from view_v.tela import TelaApp

class TelaTipoAtendimento(TelaApp):

    def __init__(self):
        self.__nada = None

    def entrando_tipo_atendimento(self) -> int:
        layout = [
        [sg.Text("MENU DE TIPOS DE ATENDIMENTO",
                 font=("Arial",18,"bold"),
                 justification="center",
                 expand_x=True)],

        [sg.HorizontalSeparator()],

        [sg.Button("Cadastrar novo tipo de atendimento",
                   key="1",
                   size=(35,2))],

        [sg.Button("Listar tipos de atendimento",
                   key="2",
                   size=(35,2))],

        [sg.Button("Alterar tipo de atendimento",
                   key="3",
                   size=(35,2))],

        [sg.Button("Remover tipo de atendimento",
                   key="4",
                   size=(35,2))],

        [sg.HorizontalSeparator()],

        [sg.Button("Voltar",
                   key="5",
                   button_color=("white","firebrick"),
                   size=(15,1))]
        ]

        window = sg.Window(
            "Menu de Tipos de Atendimento",
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
            
    def pegar_dados_tipo_atendimento(self, alteracao=False) -> dict:
        if alteracao:
            titulo = "Alterando Tipo de Atendimento"
        else:
            titulo = "Cadastro de Novo Tipo de Atendimento"

        layout = [[sg.Text("Descrição (ex: Consulta, Exame, Retorno):", size=(35,1)),sg.Input(key="descricao")],
            [sg.Text("Valor Base (R$):", size=(25,1)), sg.Input(key="valor_base")],
            [sg.Button("Salvar"), sg.Button("Cancelar")]]
        
        window = sg.Window(titulo, layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Salvar":
                try:
                    descricao = values["descricao"].strip()
                    valor_base = int(values["valor_base"])
                    if not descricao:
                        raise ValueError("A descrição não pode ser vazia.")
                    if valor_base < 0:
                        raise ValueError("O valor base não pode ser negativo.")
                    window.close()
                    return {"descricao": descricao,
                        "valor_base": valor_base}
                except ValueError as e:
                    sg.popup_error(f"Entrada inválida:\n{e}")

    def mostrar_tipos_atendimento(self, tipos: list):
        dados = []

        for t in tipos:
            dados.append([t.descricao,f"R$ {t.valor_base:.2f}"])

        layout =[[sg.Table(values=dados,headings=["Descrição","Valor Base"],
                    auto_size_columns=True,justification="center",
                    expand_x=True,expand_y=True,num_rows=min(len(dados), 15),
                    key="-TABLE-")],
                [sg.Button("Prosseguir")]]

        window = sg.Window("Tipos de Atendimento", layout, resizable=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Prosseguir"):
                break
        window.close()

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









