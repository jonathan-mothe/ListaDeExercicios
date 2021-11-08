def imprime(n):
    for i in range(1, n + 1): # n inclusivo
        for v in range(1, i + 1): # i inclusivo
            print(i),
        print('------')

numero = int(input('Informe um numero: '))
imprime(numero)
