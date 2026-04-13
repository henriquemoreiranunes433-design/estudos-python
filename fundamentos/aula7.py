def leiaint (msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO: Digite um número inteiro válido!!! ')
        if ok:
            break
    return valor


entrada = leiaint('digite um número intiro: ')
print(f' você digitou o número inteiro {entrada}')
