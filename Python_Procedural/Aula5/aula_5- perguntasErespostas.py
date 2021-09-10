perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ? ',
        'resposta': {'a': '1', 'b': '4', 'c': '3', 'd': '2'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2 * 3 ? ',
        'resposta': {'a': '9', 'b': '4', 'c': '8', 'd': '6'},
        'resposta_certa': 'd',
    },
}

resposta_certa = 0
for pk, pv in perguntas.items():
    print(f'{pk} : {pv["pergunta"]} ')

    print('Respostas : ')
    for rk, rv in pv["resposta"].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Digite sua resposta : ')

    if resposta_usuario == pv["resposta_certa"]:
        print('Parabens você acertouuu !!!')
        resposta_certa += 1
    else:
        print('ERRROOOOUUUU , respota errada kkkkkk')
    print()

    qtd_pergunta = len(perguntas)
    porcentagem_acerto = resposta_certa / qtd_pergunta * 100

    print(f'Você acerto {resposta_certa} perguntas')
    print(f'Sua porcentagem de acerto fo de {porcentagem_acerto}%')
