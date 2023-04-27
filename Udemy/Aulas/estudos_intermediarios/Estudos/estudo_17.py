from dados import produtos,pessoas,lista

idades = filter(lambda  i: i['idade'] >= 18, pessoas)

for idade in idades:
    print(idade)

# nova_lista = filter(lambda p: p['preco'] > 10, produtos)
#
# for produto in nova_lista:
#     print(produto)


