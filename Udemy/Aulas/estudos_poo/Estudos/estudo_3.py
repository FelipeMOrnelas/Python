class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


    @property
    def preco(self):
        return self._preco

    @preco.setter 
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

produto01 = Produto('SABAO', 10)
produto01.desconto(15)
produto02 = Produto('Papel', 'R$20')
produto02.desconto(15)
print(f'{produto01.nome}: {produto01.preco}')
print(f'{produto02.nome}: {produto02.preco}')
