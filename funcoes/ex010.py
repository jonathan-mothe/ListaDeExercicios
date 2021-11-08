import random


def JogaDadosCraps():
    jogada = random.randint(2, 12)
    return jogada


quantidadeJogadas = 1
acabou = False
ponto = 0

while (not acabou):
    jogada = JogaDadosCraps()
    print('Jogada %d: %d' % (quantidadeJogadas, jogada))

    if (quantidadeJogadas == 1):
        if (jogada == 2) or (jogada == 3) or (jogada == 12):
            print('Craps! Você Perdeu!')
            acabou = True
        elif (jogada == 7) or (jogada == 11):
            print('Você Ganhou!')
            acabou = True
        else:
            ponto = jogada
            print('Seu ponto é %d' % ponto)
    else:
        if (jogada == 7):
            print('Você Perdeu!')
            acabou = True
        elif (jogada == ponto):
            print('Você Ganhou!')
            acabou = True
    quantidadeJogadas += 1