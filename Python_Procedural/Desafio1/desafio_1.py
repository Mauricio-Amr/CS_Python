"""
-> É uma lista de Listas de numeros inteiros
-> A lista interna tem o tamanho de 10 elementos
-> As listas internas contem numero 1 a 10 e eles podem ser duplicados

EXERCICIO

-> Crie uma Função que encontra os dois primeiros numeros duplicados na lista interna
-> Requisitos
    A ordem dos numeros duplicados é considerada apartir da segunda ocorrencia ( O numero duplicado em si)
    Exemplo : [1, 2, 3, ->3<-, 2, 1]
    Se não encontrar o duplicado na lista , retorne -1
"""

listas_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],

]


def procurarvalorlista(*lista):


        for x in lista:
            print(x)
            TAM = len(x)-1
            z=0
            while z <= TAM -1:
                if x[z] == x[z+1]:
                    return (x[z] , x[z+1])
                    break

                elif z <= TAM:
                    z += 1

            numero = -1
            return numero




for lista_de_inteiros in listas_de_listas_de_inteiros:

    print(procurarvalorlista(lista_de_inteiros))