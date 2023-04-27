from dados import produtos,pessoas,lista

nova_lista = map(lambda p: p['idade'], pessoas)

for produto in nova_lista:
    print(produto)