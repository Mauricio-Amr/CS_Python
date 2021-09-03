"""
Operador tenario em Python

"""

logger_user = False

if logger_user :
    msg = 'Usuario logado'
else:
    msg = 'Necessario logar'

print(msg)


#modo tenario

msg = 'Usuario logado ' if logger_user else 'Necessario logar'
print(msg)


idade = input('Qual a sua Idade ')

if not idade.isnumeric():
    print('Você precisa digita um numero ')

else:
    idade = int(idade)
    idade_maior = (idade>=18)

    msg = 'Pode acessar ' if idade_maior else 'Não pode acessar'
    print(msg)