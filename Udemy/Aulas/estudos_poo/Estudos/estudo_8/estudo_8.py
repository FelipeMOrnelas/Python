from classes import *

c1 = Cliente('Felipe', 32)
print(c1.nome)
c1.falar()
c1.comprar()

print()

c3 = ClienteVIP('Otávio', 42)
c3.comprar()

print()

al = Aluno('Maria', 54)
c1.falar()
al.estudando()
