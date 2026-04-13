def ficha (nome='<desconhecido>', gol = 0):
     print(f'O jogador {nome}, fez {gol} gols.')


jogador = input('Digite o nome do jogador: ')
gols = input('Digite os gols do jogador: ')
if gols.isnumeric():
     gols = int(gols)
else :
     gols = 0
if jogador.strip() == '':
    ficha(gol = gols)
else:

    ficha(jogador, gols)


