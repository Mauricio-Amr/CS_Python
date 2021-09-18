#list tuples, str -> Sequence -> Iteravel
#estes elementos cria uma sequencia que pode ser interavel

"""geradores e interadores são feitos para consumir os valores e acabou,
caso  precise consumilos novamente teria que usa outra forma  """


nome =  'Mauricio Silva Amaral'
iterador  = iter(nome)

gerador =  (letra for letra in nome )

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('olha o "FOR')

for letra in gerador:
    print(letra)

"""
try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))


except:
    pass


print('CADE O VALORES')
#o iterando consome , esgotando o que esta na memoria
for valor in iterador:
    print(valor)
"""