#Código para práticar IF/ELSE/AND

nome = input("Qual o seu nome? ")
idade = int(input("Qual é a sua idade? "))

maior_idade = 65
menor_idade= 20

if idade >= menor_idade and idade <= maior_idade:
    print(f"{nome} pode pegar um emprestimo")
else:
    print(f"{nome} não pode pegar um emprestimo")



