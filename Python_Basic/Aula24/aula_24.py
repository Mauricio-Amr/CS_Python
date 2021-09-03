'''
# Enumerate - enumerar elemento de uma lista #list
'''

lista = [
    ['Joao', 'Maria', 'Artur'],
    ['Mary', 'Jonh','Richard'],
    ['Mario','Natalia', 'Maris']
]

enumerada = list(enumerate(lista))
#print(enumerada[1][1][1])

# for v1, v2 in enumerate(lista, 50):
#    print(v1,v2)

for v1 in enumerate(lista):
    indice , minha_lista =v1
    nome1, nome2, nome3 = minha_lista
    print(nome1)