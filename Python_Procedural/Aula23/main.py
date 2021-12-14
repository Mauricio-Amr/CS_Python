import CNPJ2

cnpj1 = '04.252.011/0001-10'

if CNPJ2.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')

for i in range(100):
    cnpj = CNPJ2.gerar()
    formatado = CNPJ2.formata(cnpj)

    print(formatado)