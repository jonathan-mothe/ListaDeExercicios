def imprime_seq(n):
    for i in range(1, n + 1):
        for v in range(1, i + 1):
            print(v),
        print('------')

numero = int(input('Informe um numero: '))
imprime_seq(numero)