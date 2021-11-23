#Objetos mutaveis listas , dicionarioa
#objetos imutaveis  tupla , string, numero, True false, None

# def lista_de_clientes(clientes_iteravel, lista =[]):
#
#     lista.extend(clientes_iteravel)
#     return lista

#corringindo o bug do mutavel
def lista_de_clientes(clientes_iteravel, lista =None):
    if lista is None:
        lista = []

    lista.extend(clientes_iteravel)
    return lista

cliente1 = lista_de_clientes(['Joao','Maria','Eduardo'])
cliente2 = lista_de_clientes(['Marcos', 'Jonas','Zico'])

print(cliente1)
print(cliente2)