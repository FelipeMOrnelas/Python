#Código para práticar IF/ELSE/IN

lista = "Felipe", "Igor", "Tiago"
nome = input("Digite o nome que voce queira verificar: ")

if nome in lista:
    print(f"{nome} esta na lista")
else:
    print(f"{nome} não está na lista")