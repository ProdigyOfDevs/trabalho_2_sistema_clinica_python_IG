from control_c.controlador_clinica import ControladorClinica
from control_c.controlador_paciente import ControladorPaciente
from control_c.controlador_profissional import ControladorProfissional
from control_c.controlador_tipo_atendimento import ControladorTipoAtendimento
from control_c.controlador_atendimento import ControladorAtendimento
from view_v.tela import TelaApp
from view_v.tela_clinica import TelaClinica
from view_v.tela_paciente import TelaPaciente
from view_v.tela_profissional import TelaProfissional
from view_v.tela_tipo_atendimento import TelaTipoAtendimento
from view_v.tela_atendimento import TelaAtendimento

class ControladorPrincipal:
    def __init__(self):
        self.__tela = TelaApp()
        self.__tela_clinica = TelaClinica()
        self.__tela_paciente = TelaPaciente()
        self.__tela_profissional = TelaProfissional()
        self.__tela_tipo_atendimento = TelaTipoAtendimento()
        self.__tela_atendimento = TelaAtendimento()
        self.__controlador_clinica = ControladorClinica(self)
        self.__controlador_paciente = ControladorPaciente(self)
        self.__controlador_profissional = ControladorProfissional(self)
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento(self)
        self.__controlador_atendimento = ControladorAtendimento(self)

    @property
    def tela(self):
        return self.__tela
    
    @property
    def tela_clinica(self):
        return self.__tela_clinica
    
    @property
    def tela_paciente(self):
        return self.__tela_paciente
    
    @property
    def tela_profissional(self):
        return self.__tela_profissional
    
    @property
    def tela_tipo_atendimento(self):
        return self.__tela_tipo_atendimento
    
    @property
    def tela_atendimento(self):
        return self.__tela_atendimento

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
