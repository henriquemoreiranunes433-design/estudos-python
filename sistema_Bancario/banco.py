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