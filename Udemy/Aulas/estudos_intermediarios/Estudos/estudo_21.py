def converter(valor):
    try:
        valor = int(valor)
        return valor
    except:
        try:
            valor = float(valor)
            return valor
        except:
            pass


numero = converter(input('Digite um número: '))

if numero is not None:
    print(numero*5)