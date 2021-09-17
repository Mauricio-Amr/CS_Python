l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [lista for lista in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l2 for v2 in range(3)]

l3 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@') for v in l3]

tupla = (
    ('chave', 'valor'),
    ('chave1', 'valor1')
)

ex5 = [(y, x) for x, y in tupla]

l3 = list(range(100))

# ex6 =[v for v in l3 if v % 2 == 0]
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
# print(ex6)

ex7 = [v if v % 3 == 0 else (f'Não é {v}') for v in l3]
# print (ex7)

ex8 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex8)

# print (dict(ex5))
# print(ex5)

# print(ex4)
# print (ex3)
# print (ex2)
# print (l2)
