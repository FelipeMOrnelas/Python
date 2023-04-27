class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def isere_endereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.endereco:
            print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
