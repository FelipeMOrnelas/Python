continuar = 0
while continuar == 0:
    print("\n")
    calculadora = "Calculadora"
    print(f"{calculadora:-^31}")

    print()
    n1 = input("Digite o primeiro número: ")
    operador = input("Digite o operador: ")
    n2 = input("Digite o segundo número: ")


    if not n1.isdigit() or not n2.isdigit():
        print("\nVocê não digitou um número valido!")
        continue

    n1 = int(n1)
    n2 = int(n2)

    if operador == '+':
        print(f"{n1} + {n2} = {n1 + n2}")
    elif operador == '-':
        print(f"{n1} - {n2} = {n1 - n2}")
    elif operador == '*':
        print(f"{n1} * {n2} = {n1 * n2}")
    elif operador == '/':
        print(f"{n1} / {n2} = {n1 / n2}")
    else:
        print("\nOperador não existe!")
    loop = 0
    while loop == 0:
        print("\nDeseja continuar? (1-SIM) (2-NÃO)")
        resposta = input("R: ")

        if resposta == '1':
            loop = 1
            continue
        elif resposta == '2':
            continuar = 1
            break
        else:
            print("Valor invalidao!")