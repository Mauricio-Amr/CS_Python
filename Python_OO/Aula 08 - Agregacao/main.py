from classe import CarrinhDeCompra
from classe import Produto

carrinho = CarrinhDeCompra()
p1 = Produto('camiseta', 50)
p2 =Produto('iphone', 10000)
p3 = Produto('Caneca', 15)


carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)


carrinho.listar_produto()
print(carrinho.soma_total())