from abc import abstractmethod
from abc import ABC

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo
    


    def depositar(self, valor ):
        self._saldo += valor
        print(f'Depósito de R$ {valor} efetuado com sucesso!')
        print(f'Seu saldo atual é de R$ {self._saldo:.2f}')


    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite):
        super().__init__(agencia, numero, saldo) 
        self._limite = limite 


    def sacar(self, valor):
        total = self._saldo + self._limite
        if valor > total:
            print('ERRO: O valor requerido excede o valor disponível!')
        else:
            self._saldo -= valor
            print(f'Saque de R$ {valor} efetuado com sucesso!')
            print(f'Seu Saldo atual é de R$ {self._saldo:.2f}')
            



class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, saldo):
        super().__init__(agencia, numero, saldo) 

    def sacar(self, valor):      
        if valor > self._saldo:
            print('ERRO: O valor requerido excede o valor disponível!')
        else:
            self._saldo -= valor
            print('Saque efetuado com sucesso!')