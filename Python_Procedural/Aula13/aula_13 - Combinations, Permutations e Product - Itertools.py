"""
Combinations, Permutations e products - Intertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem os valores únicos
Produto - ordem importa e repete o valores unicos

"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

# for grupo in combinations(pessoas, 2):
#     print(grupo)

#
# for grupo in permutations(pessoas, 2):
#     print(grupo)
#

for grupo in product(pessoas, repeat=2):
    print(grupo)