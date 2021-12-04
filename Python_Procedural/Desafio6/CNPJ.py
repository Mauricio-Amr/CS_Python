"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""


#
# # lista_cnpj1 = []
# #lista_cnpj2 = []
# lista_dig1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
# lista_dig2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
# # resultado = []
# #resultado2 = []
#
# cnpj = "04.252.011/0001-10"
# cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")
#
# lista_cnpj1 = [int(i) for i in cnpj[0:12]]
#
# resultado = sum([lista_cnpj1[i] * lista_dig1[i] for i in range(len(lista_cnpj1))])
# dig1 = 11 - (resultado % 11)
# if dig1 > 9:
#     dig1 = 0
#
# lista_cnpj2 = lista_cnpj1.copy()
# lista_cnpj2.append(dig1)
#
# resultado2 = sum([lista_cnpj2[i] * lista_dig2[i] for i in range(len(lista_cnpj2))])
# dig2 = 11 - (resultado2 % 11)
# if dig2 > 9:
#     dig2 = 0
#
# lista_cnpj2.append(dig2)
# cnpj2 = [str(i) for i in lista_cnpj2[:]]
# cnpj2 = ''.join(cnpj2)
#
# if cnpj == cnpj2:
#     print(f'cnpj {cnpj2} valido')
# else:
#     print(f'cnpj {cnpj2} valido')


def validar_cnpj(valor):
    result = converter_cnpj(valor)
    listacnpj = criar_lista_cnpj(result)
    #print("res",result)
    calc = calculate_cnpj(listacnpj)
    #print(calc)
    comparar_cnpj(result, calc)


def converter_cnpj(valor):
    cnpj = valor
    cnpj_cv = cnpj.replace(".", "").replace("/", "").replace("-", "")
    return cnpj_cv

def criar_lista_cnpj(cnpj_cv):
    cnpj_cv = [int(i) for i in cnpj_cv[0:12]]
    return cnpj_cv


def calculate_cnpj(lista_cnpj):

    # print(len(lista_cnpj))
    lista_dig1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    lista_dig2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    if len(lista_cnpj) <= 12:
        resultado = sum([lista_cnpj[i] * lista_dig1[i] for i in range(len(lista_cnpj[0:12]))])
        dig1 = 11 - (resultado % 11)
        if dig1 > 9:
            dig1 = 0
            lista_cnpj.append(dig1)
            #print("lista_cnpj",lista_cnpj)

        else:
            lista_cnpj.append(dig1)
            #print("lista_cnpj", lista_cnpj)

        calculate_cnpj(lista_cnpj)

    else:
        resultado = sum([lista_cnpj[i] * lista_dig2[i] for i in range(len(lista_cnpj[0:13]))])
        dig2 = 11 - (resultado % 11)
        if dig2 > 9:
            dig2 = 0
            lista_cnpj.append(dig2)

        else:
            lista_cnpj.append(dig2)

    return lista_cnpj


def comparar_cnpj(cnpj_ori, cnpj_veri):
    cnpj_veri = [str(i) for i in cnpj_veri[:]]
    cnpj_veri = ''.join((cnpj_veri))
    #print(cnpj_veri)

    cnpj_ori = [str(i) for i in cnpj_ori[:]]
    cnpj_ori = ''.join((cnpj_ori))
    #print(cnpj_ori)

    if cnpj_ori == cnpj_veri:

        print(f'cnpj {cnpj_ori} valido')
    else:
        print(f'cnpj {cnpj_ori} invalido')


if __name__ == '__main__':
    valor_cnpj = "12.544.992/0001-15"
    validar_cnpj(valor_cnpj)
