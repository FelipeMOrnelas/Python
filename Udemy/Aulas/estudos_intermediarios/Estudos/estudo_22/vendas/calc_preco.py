from Python.estudos_intermediarios.Estudos.estudo_22.vendas.formatar import preco

def aumento(valor, porcentagem, v=False):
    r = valor + (valor * (porcentagem / 100))

    if v:
        return preco.real(r)
    else:
        return r

def reducao(valor, porcentagem, v=False):
    r = valor - (valor * (porcentagem / 100))

    if v:
        return preco.real(r)
    else:
        return r

