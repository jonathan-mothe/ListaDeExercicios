import random


def embaralha_palavra(palavra):
    tamanho = len(palavra)
    array_pos = list(range(0, tamanho))

    for i in range(0, tamanho):
        pos1 = random.randint(0, tamanho - 1)
        pos2 = random.randint(0, tamanho - 1)

        aux = array_pos[pos1]
        array_pos[pos1] = array_pos[pos2]
        array_pos[pos2] = aux

    retorno = ''
    for i in array_pos:
        retorno += palavra[i]

    return retorno.upper()

palavra = input('Informe uma palavra: ')
print(embaralha_palavra(palavra))
