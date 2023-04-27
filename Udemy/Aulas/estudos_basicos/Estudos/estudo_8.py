nome = []

while True:

    nome_digitado = input("Digite um nome: ")

    nome.append(nome_digitado)
    n = 1
    for lista in nome:
        print(f"{n}º - {lista}")

        n += 1

    print(nome)
