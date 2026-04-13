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
            print(f'Seu Saldo é {self._saldo}')
            



class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, saldo):
        super().__init__(agencia, numero, saldo) 

    def sacar(self, valor):      
        if valor > self._saldo:
            print('ERRO: O valor requerido excede o valor disponível!')
        else:
            self._saldo -= valor
            print('Saque efetuado com sucesso!')

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade



class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta


class Banco:
    def __init__(self):
        # Usamos o prefixo _ para indicar que estas listas são internas (Encapsulamento)
        self._agencias = [1111, 2222, 3333]
        self._clientes = []
        self._contas = []

    # Métodos para Agregação (Adicionar os objetos às listas)
    def inserir_cliente(self, cliente):
        self._clientes.append(cliente)

    def inserir_conta(self, conta):
        self._contas.append(conta)

    def autenticar(self, cliente, conta):
        # 1. Checa se a agência da conta pertence ao banco
        # (Assumindo que você criou o getter 'agencia' na classe Conta)
        if conta.agencia not in self._agencias:
            print('ERRO: Agência inválida para este banco.')
            return False

        # 2. Checa se o cliente está cadastrado
        if cliente not in self._clientes:
            print('ERRO: Cliente não encontrado na base de dados.')
            return False

        # 3. Checa se a conta está cadastrada
        if conta not in self._contas:
            print('ERRO: Conta não reconhecida por este banco.')
            return False
            
        # 4. Checa se a conta informada pertence de fato ao cliente (Vínculo)

        # Se passou por todos os "filtros", retorna True
        print(f'Autenticação confirmada para {cliente.nome}!')
        return True

nubank = Banco()
cc1 = ContaCorrente(1111, 12345, 0, 500)
henrique = Cliente('Henrique', 20, cc1)
nubank.inserir_cliente(henrique)
nubank.inserir_conta(cc1)

if nubank.autenticar(henrique, cc1):
    cc1.depositar(200)
    cc1.sacar(100)
    cc1.sacar(100)
    cc1.sacar(300)



