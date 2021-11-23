"""
Faça uma lista de tarefas com as seguintes opçoes :
    adicionar tarefa
    Listar tarefas
    opçãos de desfazer tarefas
    opção refazer
"""


def lista_de_tarefa():
    pass


def adicionar_tarefa(lista_de_tarefa, lista=None):
    if lista is None:
        lista = []
    lista.append(lista_de_tarefa)
    return lista


def Listar_tarefa(lista):
    print(lista)


def defazer_tarefa(lista=[]):
    lista.pop()
    return lista

def refazer_tarefa(lista_atual, lista_anterior):
    lista_atual = lista_anterior.copy()

    return lista_atual

lt_tarefa = []

while True:
    opcao = input("Digite 1 para adicionar "
                  "\nDigite 2 para listar "
                  "\nDigite 3 para desfazer "
                  "\nDigite 4 para refazer "
                  "\nDigite S para sair "
                  "\n\nQual a sua opcao : ")


    if opcao == '1':
        tarefa = input("Digite sua tarefa ")
        listaDeTarefa = adicionar_tarefa(tarefa, lt_tarefa)

    elif opcao == '2':
        Listar_tarefa(listaDeTarefa)

    elif opcao == '3':
        listaDeTarefa = defazer_tarefa(listaDeTarefa)
        Listar_tarefa(listaDeTarefa)

    elif opcao == '4':
        listaDeTarefa = refazer_tarefa(listaDeTarefa,lt_tarefa)
        print(listaDeTarefa)

    elif opcao == 'S':
        break

    else :
        print(f'Opção {opcao} não é valida , coloque uma opção  valida \n\n')