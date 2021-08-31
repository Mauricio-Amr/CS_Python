'''
While em python
utilizado para realizar açoes enquanto uma
condição for verdadeira

requisistos : entender condiçoes e operadores

'''

#Laço infinito
# while True:
#     nome = input('Qual o seu nome ')
#     print(f'Olá {nome}')
#
# print ('Não sera executada')


# x= 0
# while x<10 :
#     y = 0
#     while y<10 :
#         print(f'x vale {x} e y vale {y}')
#         y += 1
#
#     x += 1
# print('acabou')

while True:

    num_1 = input('Digite um numro : ')
    num_2 = input('Digite outro valor : ')
    operador = input('Digite um operador : ')
    sair  = input('Deseja sair ? s = sim / n = não')

    if sair == 's':
        break

    if not num_1.isnumeric() or not  num_2.isnumeric():
        print('Voce precisa digitar um numero')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif  operador == '*' :
        print(num_1 * num_2)
    elif  operador == '/' :
        print(num_1 / num_2)
    else:
        print('operador não valido')
