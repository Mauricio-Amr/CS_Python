l1 = [1,2,3,4,5,6]
l2 = [v*2 for v in l1]
#print(l2)

# lista1 = [
#     ('chave', 2),
#     ('chave2', 'valor')
# ]

#d1 = {key : valor for key, valor in enumerate(range(5))}
#d1 = {x for x in range(5)} #isto vira um set
d1 = {f'chave_{x}' : x for x in range(5)}
#d1 = dict(lista1)

print(d1)

