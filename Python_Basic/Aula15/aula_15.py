'''
Formatando valores como modificadires

:s - Texto (String)
:d - Inteiros
:f - Números de ponto flutuantes (float)
:.(numero)f - Quantidades de casas decimais (float)
:(CARACTERES) (> OU < OU ^)(QUANTIDADE)(TIPO -s, d ou f)

> - esquerda
< - direita
^ - centro

'''

num_1 = 10
num_2 = 3
divisao = (num_1/num_2)


print(divisao)

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')


nome = 'Mauricio Amaral'
print(f'{nome:s}')

num_1 =1
print(f'{num_1:0>10}')

num_1 = 159
print((f'{num_1:0<10}'))

num_1 = 1150
print(f'{num_1:0>20.2f}')

nome = 'mauricio'
sobrenome = 'Silva Amaral'
print(f'{50 -len(nome)/2}')
print(f'{nome:#^50}')

nome_formatado = '{:#>50}'.format(nome)
nome_formatado2 = '{n:0<20}'.format(n=nome)
nome_formatado3 = '{n:#^50} {s:#^40}'. format(n= nome, s = sobrenome)
nome_formatado4 = '{0} {1}'.format(nome , sobrenome)
print(nome_formatado4)

nome_comp = 'mauricio Silva Amaral'

print(nome_comp.lower()) #tudo minuscula
print(nome_comp.upper()) #tudo maiuscula
print(nome_comp.title())#primeiras maiuscula