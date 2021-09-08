"""
Crie uma função1 que receba uma função2 como parametro e retorne o  valor da função2 executada
Faça a função1 executar duas funçoes que receba um numero diferentes de argumentos
"""

def fala_oi(nome):
    return  f'Oi {nome}'

def saudacao(nome , saudação):
    return f'{saudação} {nome}'

def mestre(funcao , *args, **kwargs):
    return funcao(*args, **kwargs)

nome = input('Digite um nome : ')
saudec = input ('Digite a saudação :')



executando = mestre(fala_oi, nome )
executando2 = mestre(saudacao , nome , saudec)

print(executando)
print(executando2)