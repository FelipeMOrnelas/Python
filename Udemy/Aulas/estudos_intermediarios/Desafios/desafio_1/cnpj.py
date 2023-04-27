def validar(cnpj):
    primeiro_digito(cnpj)
    segundo_digito(cnpj)
    return cnpj

def primeiro_digito(cnpj):
    validar_primeiro_digito = [5,4,3,2,9,8,7,6,5,4,3,2]
    multiplicador = []
    soma = 0
    cnpj = cnpj

    for n, v in enumerate(cnpj):
        multiplicador.append(cnpj[n] * validar_primeiro_digito[n])
        soma += multiplicador[n]
    resultado = (11 - (soma % 11))

    if resultado > 9:
        resultado = 0
        cnpj.append(resultado)
    else:
        cnpj.append(resultado)

    return cnpj



def segundo_digito(cnpj):
    validar_primeiro_digito = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplicador = []
    soma = 0
    cnpj = cnpj

    for n, v in enumerate(cnpj):
        multiplicador.append(cnpj[n] * validar_primeiro_digito[n])
        soma += multiplicador[n]
    resultado = (11 - (soma % 11))

    if resultado > 9:
        resultado = 0
        cnpj.append(resultado)
    else:
        cnpj.append(resultado)

    return cnpj