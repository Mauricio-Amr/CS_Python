"""
zip - unindo iteraveis
zip_longest - IterTools
"""

from itertools import zip_longest, count


indice = count()

### COdigo
cidades = [ 'Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte belo']

###Codigo
estados = [ 'SP', 'MG', 'BA']


#cidades_estados = zip(estados, cidades)
#cidades_estados = zip_longest(estados, cidades)
#cidades_estados = itertools.zip_longest(estados,cidades, fillvalue='Estado')

#print(dict(cidades_estados))


cidade_estados = zip(
    indice,
    estados,
    cidades,

)

for indice , estado , cidade in cidade_estados:
    print(indice, estado,cidade)