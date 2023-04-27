def func1(nome):
    print(nome)

def func2(name):
    nome = input('Digite seu nome: ')
    return nome

name = 'N/A'
nome = func2(name)
func1(nome)