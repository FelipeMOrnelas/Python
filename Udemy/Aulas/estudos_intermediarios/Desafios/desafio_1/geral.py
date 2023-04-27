def remover_caracteres(respostas):
    respostas = respostas.replace('/', '')
    respostas = respostas.replace('.', '')
    respostas = respostas.replace('-', '')

    if respostas.isdigit():
        lista = []
        respostas = str(respostas)
        for n,v in enumerate(respostas):
            lista.append(int(v))
        respostas = lista
        return respostas
    else:
        respostas = 'nada'
        return respostas

def remover_dois_ultimos(validado):
    remover = list(validado)
    remover.pop(-1)
    remover.pop(-1)
    return remover

