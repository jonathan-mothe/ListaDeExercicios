'''
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
    sempre arredonde os valores para cima, isto é, considere latas cheias. 
'''

tamanho = float(input('Quantos metros quadrados serão pintados? '))

litros = (tamanho / 6.0) * 1.1  # 10% de folga
latas = int(litros / 18.0)
galoes = int(litros / 3.6)

# Cálculo de latas
if (litros % 18 != 0):
    latas += 1

# Cálculo de galões
if (litros % 3.6 != 0):
    galoes += 1

# Cálculo misturando latas e galões
mistura_latas = int(litros / 18.0)
mistura_galoes = int((litros - (mistura_latas * 18.0)) / 3.6)
if ((litros - (mistura_latas * 18.0) % 3.6 != 0)):
    mistura_galoes += 1

print('Latas:', latas, ',Valor:', latas * 80)
print('Galoes:', galoes, ',Valor:', galoes * 25)
print('Latas:', mistura_latas, 'e', mistura_galoes, ',Valor: ', \
     (mistura_latas * 80)+(mistura_galoes * 25))
