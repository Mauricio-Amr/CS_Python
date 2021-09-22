"""
Considerar duas Listas de inteiros ou  floats (Lista A e Lista B)
Some os valores da lista retornando em uma nova lista com os valores somados

se uma lista for maior que a outra, a soma deve considera o tamanho da lista menor

Exemplo :
Lista_A = [1,2,3,4,5,6,7]
lista_B = [1,2,3,4,5]

resultdo = [2,4,6,8,10]
"""

Lista_A = [1,2,3,4,5,6,7]
Lista_B = [1,2,3,4,5]

resultado =[ a + b for a , b in zip(Lista_A,Lista_B) ]
print(resultado)