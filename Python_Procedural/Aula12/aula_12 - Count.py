"""
count - Itertools
"""

from itertools import count

#toma cuidado ao usar , isso é um loop infinito
# contador = count(start=10, step=-1)
#
# for valor in contador:
#     print(round(valor,2))
#
#     if valor >= 10 and valor <= -10:
#         break

contador =count()
lista=['maria', 'joao', 'antonio']
lista = zip(contador,lista)

print(list(lista))