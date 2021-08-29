'''
Faça um programa que pergunte a hora ao usuario e , baseando - se no horario
descrito, exiba a saudação apropriada
Ex : bom dia 0-11, boa tarde 12-17, boa noite 18 - 23
'''

nome = input('Digite o seu nome : ')
horario = input('Digite o horario : ')

try:
    if horario.isdigit():
        horario = int(horario)
    if horario >= 0 and horario <= 11:
        print (f'bom dia {nome}')
    elif horario >= 12  and horario <= 17:
        print (f'boa tarde {nome}')
    elif horario >= 18 and horario <= 23 :
        print(f'boa noite {nome}')
    else :
        print ('Você não digito um horario valido')

except :
    print ('erro')