from abc import ABC, abstractmethod

class Notificacao(ABC) :
    def __init__(self,mensagem)-> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando: ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao) :
    def enviar(self) -> bool:
        print('SMS: enviando: ', self.mensagem)
        return True


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Success: sua notificação foi enviada.')

    else:
        print('Error: sua notificação não foi enviada.')

notificar_Email = NotificacaoEmail ('Testando e-mail')
notificar(notificar_Email)

notificarSMS = NotificacaoSMS ('Testando SMS')
notificar(notificarSMS)



# n1 = NotificacaoEmail('Testando Notificação')
# n1.enviar()
# n2 = NotificacaoSMS('Testando Notificação')
# n2.enviar()


