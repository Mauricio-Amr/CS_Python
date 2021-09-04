"""
crie um algoritmo de validação de Cpf
"""

cpf =input('Digite seu Cpf : ')

lista = list(cpf)
indice1 = 10
indice2 = 11
lista_mult = []
lista_mult2 = []
soma1 = 0
soma2 = 0

for valor in lista:

    if valor.isnumeric():
        valor= int(valor)
        mult = (indice1*valor)
        indice1 -= 1
        lista_mult.append(mult)

        if indice1 <2:
            break

for valor2 in lista:

    if valor2.isnumeric():
        valor2= int(valor2)
        mult2 = indice2 * valor2
        indice2 -= 1
        lista_mult2.append(mult2)
        if indice2 <2:
            break


for valor in lista_mult:
    soma1 += valor

for valor in lista_mult2:
    soma2 += valor


verif1 = 11 - (soma1 % 11)
verif2 = 11 - (soma2 % 11)

if verif1 > 9 :
    digito1 = 0
    digito2 = verif2
else:
    digito1 = verif1
    digito2 = verif2

if digito2 == int(lista[-1]) and digito1 == int(lista[-2]) :
    print(f'O Cpf {cpf} é valido ')
else:
    print(f'O Cpf {cpf} não é valido ')



