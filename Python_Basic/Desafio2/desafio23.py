'''
Faça um programa que peça o primeiro nome de usuario . Se tiver 4 letras ou
menos escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras , escreva
"Seu nome é normal "; maior que seis letras "Seu nome é muito grande "
'''

nome = input('Digite seu nome : ')
print(len(nome))
try :
    if len(nome) <= 4 :
        print(f'{nome} , seu nome é muito curto')
    elif len(nome) >=5 and len(nome) <= 6 :
        print(f'{nome} ,seu nome é normal')
    else:
        print(f'{nome} , seu nome é muito grande')


except :
    print ('Error')