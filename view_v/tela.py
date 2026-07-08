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
    
    def mostra_mensagem(self, mensagem: str):
        sg.Popup("Aviso", mensagem)
