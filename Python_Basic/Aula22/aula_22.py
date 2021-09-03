"""
For / else em Python
"""

variavel = ['mauricio', 'joão', 'maria']

comeca_com_j =False
for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j =True
        break
    #     print('Começa com j ', valor)
    # else:
    #     print('Não começa com j', valor)
# if comeca_com_j:
#     print('existe uma palavra com j')
else:
    print('Não existe palavra com j')