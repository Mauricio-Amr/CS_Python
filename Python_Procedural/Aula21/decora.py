from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado =  funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time)*1000
        print(f'\nA função {funcao.__name__} levou {tempo}ms para executar.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(5000):
        print(i, end='')

        
demora()
