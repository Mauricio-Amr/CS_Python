import  vendas.calcula_preco
from vendas import calcula_preco
from vendas.formata import preco
from vendas.calcula_preco import aumento, reducao
from Aula19.vendas.formata import preco
from vendas.formata.preco import real


preco = 49.99

#preco_com_aumento = vendas.calcula_preco.aumento(preco,15)
#preco_com_aumento = calcula_preco.aumento(preco,15)
preco_com_aumento = aumento(preco,15)

#preco_com_reducao = vendas.calcula_preco.reducao(preco,15)
#preco_com_reducao = calcula_preco.reducao(preco,15)
preco_com_reducao = reducao(preco,15, formata=True)


print(preco_com_aumento)
print(preco_com_reducao)
x = real(preco)
print(x)
