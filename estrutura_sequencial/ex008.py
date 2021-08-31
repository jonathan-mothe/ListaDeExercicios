'''
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês. 
'''

valor_hora = int(input('Informe o valor/hora: '))
horas = int(input('Informe valor das horas trabalhadas: '))

print('Você receberá', valor_hora * horas, 'reais')
