"""
Desconpactando lista em Python
"""

lista = ['luiz', 'Pedro', 'Joao',1,2,3,4,5,6,7]

n1, n2, n3, *outra_lista , ultimo_da_lista = lista

print(ultimo_da_lista)

