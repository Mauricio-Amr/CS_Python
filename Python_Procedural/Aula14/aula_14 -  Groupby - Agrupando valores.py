from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricia', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'Jose', 'nota': 'B'},

]

#alunos.sort(key=lambda item: item['nota'] )

# for aluno in alunos:
#     print(aluno)


ordena = lambda item : item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento , valor_agrupados in alunos_agrupados:

    var1 ,var2 = tee(valor_agrupados)
    novos_valores_agrupados = valor_agrupados

    print(f'agrupamento : {agrupamento}')

    for aluno in var1:
        print(f'\t{aluno}')

    qunatidade = len(list(var2))
    print(f'{qunatidade} aluno tiraram nota {agrupamento}')
    print()

