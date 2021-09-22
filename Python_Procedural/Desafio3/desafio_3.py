# e-commerce
"""proposta : soma os valores do carrinho independente da quantidade de elementos"""

carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

#total = 0
# for produto in carrinho:
#     total += produto[1]
# print(total)

total =[]
print(carrinho)
resultado = [sum(total) for total in [v for k,v in carrinho ]  ]

print(resultado)