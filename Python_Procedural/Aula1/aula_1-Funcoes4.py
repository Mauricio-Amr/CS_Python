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


func()
func2()
outra_variavel = func3(arg = variavel)
print(outra_variavel)

print(variavel)