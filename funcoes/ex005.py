def somaImposto(taxa_imposto, custo):
    custo = custo + (custo * taxa_imposto / 100.0)
    return custo

taxa = float(input('Informe o valor da taxa de imposto: '))
custo = float(input('Informe o custo do produto: '))

custo = somaImposto(taxa, custo)

print('O preco com impostos é igual a: %.2f' % custo)
