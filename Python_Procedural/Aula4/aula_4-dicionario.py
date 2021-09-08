#criar dicionario
d1 ={ 'chave1': 'valor da chave'}

d1['nova_chave'] = 'valor da nova chave'

#outro meto criar

d2 =dict(chave1 = 'valor da chave 1', chave2 = 'valor da chave 2')
print(d2)

#chaves tem que ser unica
d3 ={ 'chave1': 'valor da chave','chave1': 'valor da chave','chave1': 'valor da chave real'}
print(d3)

#pode ser usado str , numero, tupla

d5 ={
    'str':'valor',
    123 : 'outro valor',
    (1,2,3,4) : 'tupla'

}

print (d5)

d5['naoExiste'] = 'Agora existe'
if 'naoExiste' in d5:
    print(d5['naoExiste'])
else:
    print('oi')

print(d5.get('nomedachave'))





#d5['nomedachave'] = 'nome de chave'
d5.update({'nomedachave' : 'nome de chave'})

if d5.get('nomedachave') is not None:
    print(d5.get('nomedachave'))

print(d5)

del d5['str']
print(d5)

#verifica se exite
print(123 in d5)
print('outro valor' in d5.values())
print(123 in d5.keys())
print(len(d5))

d6 ={
    'chave1':'valor',
    'chave2' : 'outro valor',
    'chave3' : 'tupla'
}

for k in d6.items():
    print(k[0], k[1])

for k, v in d6.items():
    print(k, v)


clientes = {
    'clientes' : {
        'nome' : 'mauricio',
        'sobrenome' : 'amaral',
    },
    'clientes2' : {
        'nome' : 'mauricio',
        'sobrenome' : 'amaral',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

#tomar cuidado com atribuição do dicionario emoutra variiavel

v = d6 #se mudar as duas muda o correto é

v= d6.copy()

#exemplo
d7 ={1:'a', 2:'b',3:'c', 'd':['mauricio', 'amaral']}
v1 =d7.copy()

v1[1] = 'armando'
v1['d'][0] ='dasdasd' #isso altera nas duas devido ser lista

print(d7)
print(v1)

import copy

a1 = copy.deepcopy(d7) #metodo de copia profunda

dict() #pode iusar para fazer cast

lista3 = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
]
print(lista3)

di1 = dict(lista3)
print(di1)


d8 = {
    1:2,
    3:4,
    5:6
}


print(d8)
d8.pop(3)
print(d8)
d8.popitem()
print(d8)