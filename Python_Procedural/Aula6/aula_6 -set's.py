"""
add (adiciona ), update (atualiza), clear, discart
union | (une)
intersection & (todos os elementos nos dois set's)
difference - (elementos apenas no set da esquerda)
symetric_diference ^ (elementos que estão nos dois sets , mas não em ambos)

"""
# set somente pode receber elementos imutaveis
s1 = {1, 2, 3, 4, 5, 6}
print(s1)

s2 = set()  # cria um conjunto vazio
# adiciona elemento
s2.add(1)
s2.add(2)
s2.add(3)
#s2.add((4, 5, 6, "mauricio"))
print(s2)

#remove o elemento do conjunto
s2.discard(2)
print(s2)

#update cria uma interação em cima do elemento, e não respeita ordem

s2.update('Python')
print(s2)

#usando para remover itens duplicados
l1 = [ 1,2 ,1,3,4,3,4,5,5,8,6,6,6,6,6,6]
l1 = set(l1)
l1 = list(l1)

print(l1)

#union
s3 = {1,2,3,4}
s4 = {3, 4, 5,6,7,8}

s5 = s3 | s4
print("union : ", s5)
s5 = s3 & s4
print("intersectippon : ",s5)
s5 = s3 - s4 #diferencça , prioriza o lado esquerdo
print ("difference : " , s5)

s5 =s3 ^ s4
print("asimetric diference : ", s5)


lista_1 = [ 'Joao ', 'maria', 'antonio']
lista_2 = [ 'Joao ', 'maria', 'antonio','maria','maria','maria','Joao ','Joao ']

print(lista_1 == lista_2)

lista_1 = set(lista_1)
lista_2 = set(lista_2)

print(lista_1 ,"///", lista_2)
