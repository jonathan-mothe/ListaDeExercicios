def qtd_digitos(digito):
    if (digito == 0):
        return 0
    return 1 + qtd_digitos(digito/10)

digito = int(input('Informe um número inteiro: '))
print('O número %d possui %d dígitos.' % (digito, qtd_digitos(digito)))
