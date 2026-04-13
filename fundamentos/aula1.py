def voto (ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return print(f'com {idade} anos NÃO VOTA.')
    elif idade < 65 and idade >= 18:
        return print(f'com {idade} anos VOTO OBRIGATÓRIO.')
    else:
        return print(f'com {idade} anos VOTO OPCIONAL.')
    
    
nascimento = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
(voto(nascimento))
