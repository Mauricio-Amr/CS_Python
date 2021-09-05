def saudacao (msg = 'Ola', nome = 'Usuario' ):
    return print(f'{msg} {nome} !!!')

msg = input('Digite uma saudação : ')
nome = input ('Digite o  nome : ')

saudacao(msg , nome)