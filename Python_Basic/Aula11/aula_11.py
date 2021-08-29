"""
Operadores logicos
and
or
not
in
not in

"""

a = 1
b = 2
c = 3

#V and V = V
#F and V = F

#comparacao1 and comparacao2

#V or V = V
#F or V = V
#F or F = F

#comp1 or comp2

#not é igual a inversão

a = 2
b = 3

if not b > a :
    print ('B é maior do que A')
else :
    print('A é maior do que B')


x =''
z = 0

if not x :
    print ('preencha o valor de x')



nome = 'mauricio'

#rix , exite em nome ?
if 'ric' in nome :
    print ('existe')
else :
    print ('Não existe')

# i não exite em nome ?
if 'i' not in nome:
    print('execute')
else:
    print ('não executei')

usuario  = input('Digite seu Usuario : ')
senha = input('Digite sua Senha : ')

usuario_bd = 'mauricio'
senha_bd = 'senha'

if usuario_bd == usuario and senha_bd == senha :
    print('Você esta logado no sistema')
else:
    print('Usuario ou Senha incorreta')