"""
Funções (def) em Python - *args **kwargs

"""

def func(a1, a2, a3, a4, a5 , nome = None , a6 =None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

def func2(*args, **kwargs): #args argumentos , kwargs passa os argumentos nomeados

  print(args)
  print(kwargs)
  idade  = kwargs.get('idade')
  if idade is not None:
      print(idade)



lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func2(*lista, lista2 , nome = 'luiz', sobrenome ='Miranda', idade = 30)



print('################################')

var = func(1,2,3,4,5, nome = 'mauricio', a6 = '1')
print (var[0], var[1])