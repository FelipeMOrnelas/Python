numero = 0
lista_de_nomes = []
quat_nomes = int(input("Digite a quantidades de nomes para add na lista: "))

lista = list(range(quat_nomes))

for i in lista:
    nomes = input(f"Digite o {numero+1}º nome: ")
    lista_de_nomes.append(nomes)
    numero = numero + 1

print(lista_de_nomes)
