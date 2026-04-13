class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe (self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    ...

class Funcionaio(Pessoa):
    ...


c1 = Cliente('Henrique', 'Moreira')
c1.falar_nome_classe()
f1 = Funcionaio('Cláudio', 'Pereira')
f1.falar_nome_classe()