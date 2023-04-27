from itertools import combinations,count

listas = []
contador =0

for n in count(start=0):
    listas.append(n)
    if n >= 60:
        break

for combinacoes in combinations(listas, 6):
    contador += 1

print(contador)
