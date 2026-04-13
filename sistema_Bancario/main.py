from contas import  ContaCorrente, ContaPoupanca
from clinte import Cliente
from banco import Banco


nubank = Banco()
cp1 = ContaPoupanca(1111, 12345, 0,)
henrique = Cliente('Henrique', 20, cp1)
nubank.inserir_cliente(henrique)
nubank.inserir_conta(cp1)

if nubank.autenticar(henrique, cp1):
    cp1.depositar(100)
    cp1.sacar(200)
print()
bradesco = Banco()
cc1 = ContaCorrente(1111, 12345, 0,500)
henrique = Cliente('Henrique', 20, cc1)
bradesco.inserir_cliente(henrique)
bradesco.inserir_conta(cc1)

if bradesco.autenticar(henrique, cc1):
    cc1.depositar(1000)
    cc1.sacar(250)


   


