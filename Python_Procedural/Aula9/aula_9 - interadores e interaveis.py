#lista = [0,1,2,3,4,5]
#print(hasattr(lista, '__iter__')) #verifica se o objeto é interavel
#print(hasattr(lista,'__next__')) #mostra se  lista é um interador

# lista = iter(lista) #transforma a lista em um interador
# print(next(lista)) #interador mostra o valor de cada vez diferente de um interavel
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
#
#
# #o for transforma o objeto em um iterador mostrando cada elemento em uma linha
# for v in lista:
#     print(v)
#
#

import sys

lista  = list(range(1000))
print(sys.getsizeof(lista))