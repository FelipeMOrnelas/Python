import Jogo_Foca
import Jogo_Adivinhacao
import os

def escolha_jogo():
    print("\n*********************************")
    print("      Escolha o seu Jogo!!")
    print("*********************************")


    print("\n(1)Adivinhação   (2)Forca")
    jogo = input("Qual? ")

    if jogo.isnumeric():
        jogo = int(jogo)
        if jogo == 1:
            print("\nCarregando Jogo da Adivinhação")
            os.system("cls")
            Jogo_Adivinhacao.start_adivinhacao()
        elif jogo == 2:
            print("\nCarregando Jogo da Forca")
            os.system("cls")
            Jogo_Foca.start_foca()
        else:
            input("\nOpção Inválida!")
            os.system("cls")
            escolha_jogo()
    else:
        input("\nOpção Inválida!")
        os.system("cls")
        escolha_jogo()

if __name__ == "__main__":
    escolha_jogo()