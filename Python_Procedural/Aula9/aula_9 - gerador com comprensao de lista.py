import sys
import time

lista1 = [ x for x in range(1000)]
#print(type(lista))

#cria um gerador , mudando de cochete para parenteses
lista2 = (x for x in range(1000))
#print(type(lista))

print(sys.getsizeof(lista1))#consome mais memoria

print(sys.getsizeof(lista2))#consome menos memoria