'''
Combunations = combinações que não se repetem
Permutations = combinações que se repetem, mas não entre elas
Product = todos os tipos de combinações
'''

from itertools import combinations, permutations, product

senha = [1,2,3,4,5,6,7,8,9,0]
contador_de_combinacoes = 0
senha_do_sitema = (9, 0, 9, 0)

for combinacoes in product(senha, repeat= 4):
    contador_de_combinacoes += 1
    print(combinacoes)
    if combinacoes == senha_do_sitema:
        print(f'Achamos seu senha que é {combinacoes}')
        break

print(f'Temos {contador_de_combinacoes} tipos de senha')