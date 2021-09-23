def numero(valor):
    if (valor < 0):
        return 'n'
    else:
        return 'p'

n = int(input('Informe um número: '))
print(numero(n))