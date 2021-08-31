'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. 
'''

import math

num_int1 = int(input('Informe um número inteiro: '))
num_int2 = int(input('Informe outro número inteiro: '))
num_real = float(input('Informe um número real: '))

print('O dobro do primeiro vezes a metade do segundo é', (2 * num_int1) / (num_int2 / 2.0))

print('A soma do triplo do primeiro com o terceiro é', (3 * num_int1) + num_real)

print('O terceiro elevado ao cubo é', math.pow(num_real, 3))
