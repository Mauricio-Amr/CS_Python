"""
Variaveis dentro da função

"""

variavel = 'valor'

def func():
    print(variavel)



def func2():
    #Não é boa pratica troca a varivel global
    global variavel
    variavel = 'outro valor'
    print(variavel)


def func3(arg = None):
    arg = arg.replace('v', 'c')
    return arg

def func4 ():
    outra_variavel2 ='mauricio s amr'
    return  outra_variavel2

def func5(args):
    print(args)

var1 = func4()
func5(var1)

func()
func2()
outra_variavel = func3(arg = variavel)
print(outra_variavel)

print(variavel)