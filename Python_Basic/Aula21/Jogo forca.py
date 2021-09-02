secreto = 'perfume'
digitado = []
chance = 3

while True:
    if chance  <= 0:
        print('Você perdeu !!!')
        break

    letra = input('Digite uma letra : ')

    if len(letra) >1:
        print('Ahhh isso não vale , digite apenas uma letra')
        continue

    digitado.append(letra)

    if letra in secreto:
        print(f'Uhhhhuulll.  a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Afffzzz :  a letra "{letra}" NÃO EXISTE  na palavra secreta')
        digitado.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitado:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Que legal , VOCÊ GANHOU !!! ')
        print(f'A palavra ela {secreto_temporario}')
    else :
        print(f'A palavra secreta esta assim :  {secreto_temporario}')

    if letra not in secreto:
        chance -= 1
    print(f'Você ainda tem : {chance} chances')
    print()