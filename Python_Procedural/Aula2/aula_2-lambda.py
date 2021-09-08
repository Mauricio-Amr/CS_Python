# def func(arg, arg2)
#     return arg * arg2
#
#
# a = lambda x, y : x * y

lista =[
    ['P1', 13],
    ['P2', 6],
    ['P3', 20],
    ['P4', 4],
    ['P5', 18],
]

lista.sort(key= lambda i:i[1], reverse=True)
print(lista)

print(sorted(lista, key= lambda i: i[1]))