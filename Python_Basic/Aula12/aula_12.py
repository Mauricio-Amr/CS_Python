usuario = input('Digite seu Usuario : ')
qtd_caracteres = len(usuario)

print(usuario , qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6 :
    print('Você precisa digita mais de 6 caracteres')
else:
    print('Você foi cadastrado no sistema')




string1 = input('digite alguma coisa : ')
string2 = input('digite alguma outra coisa coisa : ')

print(f'A quantidade de caracteres digitado {len(string1) + len(string2)}')

#len não funciona com int, float e nem com bool