secreto = 'Felipe'
digitados = []
chances = 8

print("*** Bem Vindo ao Jogo Encontre o Nome ***")
print("Objetivo do jogo é você encontrar um nome que eu estou pensando!")
print(f"Você terá somente {chances} chances!")

while True:

    if chances <= 0:
        print("-------------")
        print("Você perdeu!!")
        print("-------------")
        break

    letra = input("\nDigite uma letra: ")

    if len(letra) > 1:
        print("\nDigite somente uma letra!")
        print("Tente Novamente")
        continue

    digitados.append(letra)

    if letra in secreto:
        print(f"Letra {letra} existe no nome secreto!")
    else:
        print(f"Letra {letra} infelizmente não existe no nome secreto!")
        digitados.pop()

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print("\n")
        print("***********************")
        print("Que legal, você ganhou!")
        print("***********************")
        print(f"\nO nome secreto é {secreto}")
        break
    else:
        print(f"O nome secreto ficou assim {secreto_temporario}")

    if letra not in secreto:
        chances -= 1

    print(f"\nVocê ainda tem {chances} chances.\n")
