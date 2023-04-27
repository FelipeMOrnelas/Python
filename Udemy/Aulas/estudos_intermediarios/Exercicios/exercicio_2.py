def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

rodando1 = mestre(fala_oi, 'Felipe')
rodando2 = mestre(saudacao, 'Felipe', saudacao = 'Bom dia')
print(rodando1)
print(rodando2)