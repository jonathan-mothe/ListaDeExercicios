'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e
a velocidade de um link de Internet (em Mbps),calcule e
informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanho = float(input('Informe o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade de conexão em Mbps: '))

tamanho_bits = tamanho * 1024 * 1024 * 8
tempo_segundos = tamanho_bits / (velocidade * 1024 * 1024)
tempo_minutos = tempo_segundos / 60

print('Tempo aproximado de download:', tempo_minutos, 'minutos')
