"""
Faça uma lista de tarefas com as seguintes opçoes :
    adicionar tarefa
    Listar tarefas
    opçãos de desfazer tarefas
    opção refazer
"""


def adicionar_tarefa(tarefa, lt_tarefas):
    lt_tarefa.append(tarefa)


def listar_tarefa(lt_tarefa):
    print(lt_tarefa)


def defazer_tarefa(lt_tarefa,lt_refazer_tarefa ):
    if not lt_tarefa :
        print("Não tem elemento na lista ")
        return

    ultima_tarefa = lt_tarefa.pop()
    lt_refazer_tarefa.append(ultima_tarefa)


def refazer_tarefa(lt_tarefa, lt_refazer_tarefa):
    if not lt_refazer_tarefa:
        print("Nada a ser refeito")
        return
    ultimo_refazer = lt_refazer_tarefa.pop()
    lt_tarefa.append(ultimo_refazer)


if __name__ == '__main__':

    lt_tarefa = []
    lt_desfazer_tarefa = []
    lt_refazer_tarefa = []

    while True:
        opcao = input("Digite 1 para adicionar "
                      "\nDigite 2 para listar "
                      "\nDigite 3 para desfazer "
                      "\nDigite 4 para refazer "
                      "\nDigite S para sair "
                      "\n\nQual a sua opcao : ")


        if opcao == '1':
            tarefa = input("Digite sua tarefa ")
            adicionar_tarefa(tarefa, lt_tarefa)

        elif opcao == '2':
            listar_tarefa(lt_tarefa)

        elif opcao == '3':
            defazer_tarefa(lt_tarefa,lt_refazer_tarefa)

        elif opcao == '4':
            refazer_tarefa(lt_tarefa, lt_refazer_tarefa)


        elif opcao == 'S':
            break

        else :
            print(f'Opção {opcao} não é valida , coloque uma opção  valida \n\n')