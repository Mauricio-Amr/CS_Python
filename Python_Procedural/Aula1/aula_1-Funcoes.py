"""
Funçoes - def em Python (parte 1)
"""

def funcao():
    print('Ola mundo !')

def saudacao(msg = 'ola', nome ='usuario' ):

    nome  = nome.replace('e','3')
    msg = msg.replace('e', '3')
    print(msg , nome)





saudacao(nome ='Zezinho' , msg = 'Hi')
saudacao('ola', 'mauricio')
saudacao()
funcao()
funcao()
funcao()
funcao()

