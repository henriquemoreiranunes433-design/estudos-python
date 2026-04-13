from pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta