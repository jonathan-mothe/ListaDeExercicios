'''
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 
'''

sexo = input('Informe seu sexo (M/F): ')
altura = float(input('Informe sua altura: '))
peso = float(input('Informe o seu peso: '))

if (sexo == 'F'):
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = (72.7 * altura) - 58

if (peso > peso_ideal):
    print('Você está acima do seu peso ideal:', peso_ideal)
elif (peso < peso_ideal):
    print('Você está abaixo do seu peso ideal:', peso_ideal)
else:
    print('Você está no seu peso ideal:', peso_ideal)
