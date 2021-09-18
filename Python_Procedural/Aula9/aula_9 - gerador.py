import sys
import time

# def gera():
#     r =[]
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1)
#     return r

#função geradora
# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#

def gera():
   variavel = 'valor 1 '
   yield  variavel
   variavel = 'valor 2 '
   yield variavel
   variavel = 'valor 3 '
   yield variavel


g  = gera()
print(next(g))
print(next(g))
print(next(g))
print(next(g))# apresnta uma exception StopIteration

''' melhor forma para usa o gerador é com o "for"'''


# for v in g:
#     print(v)

#geradore é  tanto um interavel quanto um interador
#
# print(hasattr(g,'__iter__'))
# print(hasattr(g,'__next__'))