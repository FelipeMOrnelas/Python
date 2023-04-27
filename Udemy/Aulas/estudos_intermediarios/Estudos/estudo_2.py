lista = [
    ['P1', 20],
    ['P2', 5],
    ['P3', 10],
    ['P4', 23],
    ['P5', 2],
]

romano = ['I','V','X','I','L']

romano.sort()
print(romano)

print(f'Sem efeito {lista}')
print(sorted(lista, key=lambda i: i[1]))
print(f'Sem efeito {lista}')
lista.sort(key=lambda item: item[1])
print(lista)
