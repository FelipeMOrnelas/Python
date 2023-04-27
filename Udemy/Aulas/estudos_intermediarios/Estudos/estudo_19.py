from dados import pessoas,produtos,lista
from functools import reduce

soma_idades = reduce(lambda  ac, i: i['idade'] + ac, pessoas, 0)
print(f'Media das idades é: {soma_idades/len(pessoas)}')

# soma_produtos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
# print(f'Media dos produtos é: {soma_produtos/len(produtos)}')

# soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
# print(soma_lista)