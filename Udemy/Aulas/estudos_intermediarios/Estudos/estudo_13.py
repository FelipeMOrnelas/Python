from itertools import count

contador = count(start=1)
lista = ['Felipe', 'Joao', 'Nathan']
lista = zip(contador, lista)
lista = list(lista)
print(lista)

id = int(input('Digite o id do nome: '))

print(lista[id][1])