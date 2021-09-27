from dados import produtos, pessoas, lista

#nova_lista = filter(lambda x : x > 5, lista)
'''lista comprehetion'''
#nova_lista = [x for x in lista if x > 5]
#print(list(nova_lista))

# def filtra(produto):
#     if produto['preco']> 50:
#         produto['e_caro'] = True
#     return  True
#
# nova_lista_produto = filter(filtra, produtos)
#
# for produto in nova_lista_produto:
#     print(produto)
#

def filtraPessoa(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else :
        return False

nova_lista_pessoa = filter(filtraPessoa, pessoas)

for pessoa in nova_lista_pessoa:
    print(pessoa)


