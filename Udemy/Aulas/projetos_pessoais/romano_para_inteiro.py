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
    print(n)





numero = int(input('Digite o número que vai ser convertido para número romano: '))

print(converter(numero))