import os
import Jogos

def start_foca():

    imprima_mensagem_abertura()

    palavra_secreta = carregando_palavra_secreta()

    imprima_mensagem_abertura()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    erro = 0

    enforcou = False
    acertou = False
    print("\n{} \n".format(letras_acertadas))


    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
           erro += 1
           desenha_forca(erro)
        enforcou = erro == 7
        acertou = "_" not in letras_acertadas
        print("{}\n".format(letras_acertadas))


    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    input('\nSair')
    os.system("cls")
    Jogos.escolha_jogo()


def imprima_mensagem_abertura():
    print("\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def carregando_palavra_secreta():
    palavra_secreta = input("\nDigite uma frase para o amigo tentar acertar: ").upper()
    os.system("cls")
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if letra == chute:
            letras_acertadas[posicao] = letra
        posicao += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    start_foca()