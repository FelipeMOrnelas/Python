def bug(romano):
    numero_romano = []
    digitado = romano
    i = 0

    while True:
        i += 0

        if i == len(digitado):
            romano = numero_romano
            return romano
        elif digitado[i] == 'I':
            if i + 1 == len(digitado):
                numero_romano.append(digitado[i])
                romano = numero_romano
                return romano
            elif digitado[i] + digitado[i + 1] == 'IV':
                j = 'IV'
                numero_romano.append(j)
                i += 2
            elif digitado[i] + digitado[i + 1] == 'IX':
                j = 'IX'
                numero_romano.append(j)
                i += 2
            else:
                numero_romano.append(digitado[i])
                i += 1
        elif digitado[i] == 'V':
            numero_romano.append(digitado[i])
            i += 1
        elif digitado[i] == 'X':
            if i + 1 == len(digitado):
                numero_romano.append(digitado[i])
                romano = numero_romano
                return romano
            elif digitado[i] + digitado[i + 1] == 'XL':
                j = 'XL'
                numero_romano.append(j)
                i += 2
            elif digitado[i] + digitado[i + 1] == 'XC':
                j = 'XC'
                numero_romano.append(j)
                i += 2
            else:
                numero_romano.append(digitado[i])
                i += 1
        elif digitado[i] == 'L':
            numero_romano.append(digitado[i])
            i += 1
        elif digitado[i] == 'C':
            if i + 1 == len(digitado):
                numero_romano.append(digitado[i])
                romano = numero_romano
                return romano
            elif digitado[i] + digitado[i + 1] == 'CD':
                j = 'CD'
                numero_romano.append(j)
                i += 2
            elif digitado[i] + digitado[i + 1] == 'CM':
                j = 'CM'
                numero_romano.append(j)
                i += 2
            else:
                numero_romano.append(digitado[i])
                i += 1
        elif digitado[i] == 'D':
            numero_romano.append(digitado[i])
            i += 1
        elif digitado[i] == 'M':
            numero_romano.append(digitado[i])
            i += 1
        else:
            print(f'\nA letra {digitado[i]} não existe!')
            print("Excluindo para continuar!")
            i += 1

    romano = numero_romano
    return romano

def verificar(romano):
    romano_lista = []
    lista_temporaria = []

    for n, i in enumerate(romano):
        romano_lista.append(i)
    for n, i in enumerate(romano_lista):
        if romano_lista[n] == 'I' or romano_lista[n] == 'IV' or romano_lista[n] == 'V' or romano_lista[n] == 'IX' or romano_lista[n] == 'X' or romano_lista[n] == 'XL' or romano_lista[n] == 'L' or romano_lista[n] == 'XC' or romano_lista[n] == 'C' or romano_lista[n] == 'CD' or romano_lista[n] == 'D' or romano_lista[n] == 'CM' or romano_lista[n] == 'M':
            lista_temporaria.append(romano_lista[n])
        else:
            print(f'\nO "{romano_lista[n]}" não é um número romano!')
            print("Excluindo e continuando...")

    romano_lista = lista_temporaria
    return romano_lista

def conversor(romano):
    numero = []
    contador = 0

    for n, i in enumerate(romano):
        numero.append(i)

    repetir = len(numero)
    # numero.append()

    for n, i in enumerate(numero):
        if numero[n] == 'I':
            contador += 1
        elif numero[n] == 'IV':
            contador += 4
        elif numero[n] == 'V':
            contador += 5
        elif numero[n] == 'IX':
            contador += 9
        elif numero[n] == 'X':
            contador += 10
        elif numero[n] == 'XL':
            contador += 40
        elif numero[n] == 'L':
            contador += 50
        elif numero[n] == 'XC':
            contador += 90
        elif numero[n] == 'C':
            contador += 100
        elif numero[n] == 'CD':
            contador += 400
        elif numero[n] == 'D':
            contador += 500
        elif numero[n] == 'CM':
            contador += 900
        elif numero[n] == 'M':
            contador += 1000
        else:
            print("Errado")
    romano = int(contador)
    return romano

def converter(numero):
    n = []
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while numero:
        div = numero // num[i]
        numero %= num[i]

        while div:
            n.append(sym[i])
            div -= 1
        i -= 1
    return n

romano = input("Digite o número romano para converter: ")

romano = bug(romano)

verificado_romano = verificar(romano)

contador = conversor(verificado_romano)

numero = int(contador)

correto = converter(numero)

verificado_romano = ''.join(verificado_romano)
correto = ''.join(correto)

if verificado_romano == correto:
    print(f'\nO número {verificado_romano} convertido é: {contador}')
else:
    print(f'\nO formato "{verificado_romano}" não existe')
    print(f'\nSe você quis dizer {correto} então é: {contador}')
