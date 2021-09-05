"""
Funçoes (def) em Python - return
"""

def funcoes(var):
   return

def divisao(n1, n2):
    if n2 == 0:
        return

    return n1/n2

def dump():
    return f

def f(var):
    print(var)

def dump2():
    return ('Mauricio','Amaral')

var = dump2() #('E colocar o  valor aqui !!!') # var assume o valor da função de f, atraves da função dump
print (id(var), id(f))
print('dump2 : ',var , type(var) )


#print(dump(), type(dump()))


# valor = divisao(8,0)
#
# if valor :
#     print(valor)
# else:
#     print('conta invalida')


# variavel = funcoes('Valor que eu quero')
# #print(variavel)
#
# if variavel:
#     print(variavel)
# else:
#     print('Nenhum valor')