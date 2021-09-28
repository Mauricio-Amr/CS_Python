from dados import produtos, pessoas, lista
from functools import reduce

# acumula = 0
#
# for item in lista:
#     acumula += item
#
# print(acumula)


# soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
# print(soma_lista)


soma_prod = reduce(lambda ac , i : i['preco']+ac , produtos, 0)
print(soma_prod / len(produtos))

soma_idade = reduce(lambda ac, i: i['idade']+ac, pessoas,0)
print(soma_idade/ len(pessoas))