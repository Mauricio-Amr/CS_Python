from dados  import produtos, pessoas, lista

#nova_lista = map(lambda x : x*2,lista)

#com lista comprehetion
# nova_lista = [x * 2 for x in lista]
# print(lista)
# print(list(nova_lista))

# for produto in produtos:
#     print(produto)

def aumentaPreco (p):
    p['preco'] =round(p['preco'] * 1.05,2)
    return p



# novos_produtos  = map(aumentaPreco, produtos)
# for preco in novos_produtos:
#     print(preco)



def aumenta_idade(p):
    p['nova_idade'] = p['idade']* 1.20
    return p

#nomes = map(lambda p : p['idade'] *1.2, pessoas)
nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)