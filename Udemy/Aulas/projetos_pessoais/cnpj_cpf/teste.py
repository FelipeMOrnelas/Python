validar_primeiro_digito = [5,4,3,2,9,8,7,6,5,4,3,2]
cnpj = [0, 4, 2, 5, 2, 0, 1, 1, 0, 0, 0, 1]
multiplicador = []
soma = 0


for n, v in enumerate(cnpj):
    multiplicador.append(cnpj[n] * validar_primeiro_digito[n])
    soma += multiplicador[n]
# for n, v in enumerate(multiplicador):
#     soma += multiplicador[n]

print(soma)