carinho = []

carinho.append(('Produto 1', 10))
carinho.append(('Produto 2', 10))
carinho.append(('Produto 3', 10))
carinho.append(('Produto 4', 10))
carinho.append(('Produto 5', 10))
carinho.append(('Produto 6', 50))

total = sum([float(valor[1]) for valor in carinho])

print(total)