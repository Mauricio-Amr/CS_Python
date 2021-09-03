"""
Operador Or
"""

nome = input('Qual o seu  nome : ')

if nome :
    print(nome)
else:
    print('Não digitou um nome ')

#para quando chega na verdadeira
print(nome or None or False or 'Você não digitou seu nome')