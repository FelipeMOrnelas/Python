#Código para práticar LEN

usuario = input("Digite um nome para o usuario: ")
senha = input("Digite uma senha com pelo meno 6 caracteres: ")

validacao = len(senha)

if validacao >= 6:
    print("Cadastro criado")
else:
    print("Cadrastro não criado")