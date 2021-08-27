"""
Operadores relacionais
== : igualdade
> : maior que
>= : maior ou igual que
< : menor que
<= : menor ou igual que
!= : diferente que
"""

print(2 == 2)
#Op. relacional retorna um bool

num_1 = 2
num_2 = 4

print(num_1 == num_2)

#espressão recebe o resultado da comparação
# expressao = num_1 == num_2
expressao = num_1 < num_2
# expressao = num_1 <= num_2
# expressao = num_1 > num_2
# expressao = num_1 >= num_2
# expressao = num_1 != num_2

print('expressão : ',expressao)


nome = input('Qual o seu nome ? ')
idade = int(input('Qual a sua idade ? '))

#idade para pegar emprestimo
idade_menor = 20
idade_maior = 30


#if idade <= idade_limite:
if idade >= 20 and idade_maior <= 30 :
    print (f'{nome} emprestimo disponivel')

else :
    print(f'{nome} não pode pegar o emprestimo')
