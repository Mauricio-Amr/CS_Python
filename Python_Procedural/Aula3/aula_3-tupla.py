t1 = (1,2,3,'a','mauricio') # so  pode adiciona elemento  quando criada

#busca atraves do  indice

#interar
for c in t1:
    print(c)
#fatiando
print(t1[2:])

#para criar uma tupla basta coloca uma virgula
t2 = 1,8,9,10


#concatenção
t3 =t1+t2
print(t3)

n1,n2,n3 ,*_, n = t3
print(n)

t4 = (1,2,3,4,5)*20
#print(t4)

#para alterar tem que muda para lista
t1 = list(t1)
t1[1] = 3000
print(t1)

t1=tuple(t1)
print(t1)
