from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto("Camisa", 50)
p2 = Produto("Iphone", 10000)
p3 = Produto("Caneca", 15)

carrinho.iserir_produto(p1)
carrinho.iserir_produto(p2)
carrinho.iserir_produto(p3)
carrinho.iserir_produto(p1)

carrinho.lista_produto()

print(f'\nValor total {carrinho.soma_total()}')
