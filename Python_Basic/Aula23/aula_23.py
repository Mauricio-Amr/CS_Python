'''
Split , join e Enumerate em Python
* Split - Dividir uma string #str
* Join - Juntar uma lista # str
*Enumerate -Enumera elementos da lista #str
'''

# string = 'O brasil é o pais do futebol, o brasil é penta'

# lista_1= string.split(' ')
# lista_2 = string.split(',')
#print(lista_2)

# palavra = ''
# contagem = 0

# for valor in lista_1:
#     #print(f'{valor} : {lista_1.count(valor)}')
#     qtd_vezes = lista_1.count(valor)
#     if qtd_vezes > contagem:
#         contagem =qtd_vezes
#         palavra =valor
#
# print(f'A palavra que mais apareceu é {palavra} ({contagem})')
#
# for valor in lista_2:
#     print(valor.strip().capitalize())

# string = 'o brasil é penta'
# lista = string.split(' ')
# string_2 = ' '.join(lista)
# print(string)
# print(lista)
# print(string_2)

# for indice , valor in enumerate(lista):
#    print(f'{indice} : {valor} - {lista[indice]}')


lista = ['Joao', 'Maria', 'Mauricio']

for indice, nome in enumerate(lista) :
    print(indice, nome)