nome = input("Digite seu nome: ")

def carregar(nome):
    print(f"\n{nome}")
    print(f"Nome reverso: {nome[::-1]}")

carregar(nome)

carregar('Heitor')