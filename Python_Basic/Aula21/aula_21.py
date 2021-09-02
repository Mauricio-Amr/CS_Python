"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#listas suportam diversos valores
lista = ['A', 'B','C','D', 'E']
#         0    1   2   3   4
# -       5    4   3   2   1
print (lista)
#alterando valor da lista
lista[4] = 'alt'
print(lista)


#ler lista do fim para inicio
print(lista[-1])

#fatiamento
print(lista[0:3])
print (lista[2:4])
print(lista[:4])
print(lista[::2])
#invertido
print(lista[::-1])

################################
l1 = [1,2,3]
l2 = [4,5,6]
#l3 =l1 +l2

print(l1)
print(l2)
#print (l3)

#extender uma lista atraves de outra
#l1.extend(l2)
#print(l1)

#adiciona elemento ao final da lista
l2.append('b')

#adiciona em  qualquer lugar da lista
l2.insert(0, 'banana')
print('l2 : ' ,l2[0])

#remover o ultimo elemento da lista
print('lista l2 ; ', l2)
l2.pop()
print ('Ultimo item removiso : ', l2)

#deleta elemento de uma lista
l4 = [1,2,3,4,5,6,7,8,9]
print(l2)
l2.insert(0,'banana')
print(l2)
del (l2[::2])
#del (l2[0])
print('del',l2)
######

#minimo e maximo
print('min : ' , min(l4))
print('max : ' , max(l4))

#list
l5 = list(range(1,10))
print('l5: ',l5)

# soma = 0
# for valor in l5 :
#     soma = soma + valor
#     print(f'{soma} + {valor} = {soma}')


l6 = ['String', True, 10 , 5.89]

for elem in l6 :
    print(f'O tipo de elemento {type(elem)} e o seu valor é {elem} ')