'''
Faça um programa que peça aso usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario não digite um numero
inteiro , informe que não é um numero inteiro
'''

valor = input ('Digite um numero : ')


try:
    if valor.isdigit() :
        valor= int(valor)
    elif valor % 2 == 0 :
        print(f'O {valor} é par')
    else :
        print(f'O {valor} é impar')
except :
    if valor != int() :
        print('O numero não é um inteiro')