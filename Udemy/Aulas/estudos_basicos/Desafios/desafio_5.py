cpf_novo = list(range(0,11))
solucao_1 = 0
solucao_2 = 0
converter = list(range(0,11))

cpf = input("Digite seu cpf somente numero: ")

for i, j in enumerate(cpf):
    cpf_novo[i] = int(j)
cpf_novo.pop()
cpf_novo.pop()

for n, r in enumerate(range(10, 1, -1)):
    solucao_1 += cpf_novo[n] * r
    n += 1


digito_1 = (11 - (solucao_1 % 11))

if digito_1 > 9:
    digito_1 = 0

cpf_novo.append(digito_1)

for n, r in enumerate(range(11, 1, -1)):
    # print(f"{cpf[n]} * {r} = {cpf[n]*r}")
    solucao_2 += cpf_novo[n] * r
    n += 1

digito_2 = (11 - (solucao_2 % 11))

if digito_2 > 9:
    digito_2 = 0

cpf_novo.append(digito_2)

for i in range(0, 11):
    converter[i] = str(cpf_novo[i])
    i += 1

cpf_novo = ''.join(converter)

sequencia = cpf_novo == str(cpf_novo[0] * 11)

if cpf == cpf_novo and not sequencia:
    print("CPF informado é Valido")
else:
    print("CPF informado é Invalido")



