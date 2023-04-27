import random
import os
import Jogos

def nivel(niveis):
    while niveis == 0:
        print("Antes defina o nível do jogo!")
        print("(1)Fácil  (2)Normal  (3)Difícil")
        nivel = input("Escolha: ")

        if nivel.isnumeric():
            nivel = int(nivel)
            if nivel == 1:
                tentativas = 20
                break
            elif nivel == 2:
                tentativas = 10
                niveis = 1
            elif nivel == 3:
                tentativas = 5
                break
            else:
                input("\nOpção Inválida!")
                os.system("cls")
        else:
            input("\nVocê não digitou o número correspondente das opções!")
            os.system("cls")
    return tentativas

def start_adivinhacao():
    escolha = 1

    while escolha == 1:

        niveis = 0
        escolha2 = 1
        numero_secreto = random.randint(1, 101)
        rodadas = 0

        print("\n*********************************")
        print("Bem vindo ao jogo de Adivinhação!")
        print("*********************************")

        tentativas = nivel(niveis)


        while rodadas < tentativas:
            print("\nVocê tem {} tentativas!".format(tentativas-rodadas))
            rodadas += 1
            chute = input("Digite um número que deve está entre 1 a 100: ")

            if chute.isnumeric():
               chute = int(chute)
               if chute < 1 or chute >100:
                   print("Digite um número entre 1 a 100!")
                   continue

            else:
                print("\033[0;31mIsso não é um número ou é menor do que 0!\033[m")
                continue

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if(maior):
                print("\nO seu chute foi maior do que o número secreto!")
            elif(menor):
                print("\nO seu chute foi menor do que o número secreto!")

            if(acertou):
                print("\nVocê é o Vencedor!")
                print("Parabéns! Você acertou!")
                break
            elif(rodadas == tentativas):
                print("\033[0;31m\nVocê perdeu!\033[m")
                break


        print("\033[0;33m\n***Gabarito***\033[m")
        print("Número Secreto é:", numero_secreto)

        while escolha2 == 1:
            print("-> 1 Continuar")
            print("-> 2 Sair")
            opcoes = input("Escolha: ")

            if opcoes.isnumeric():
                opcoes = int(opcoes)
                if opcoes == 1:
                    escolha2 = 2
                    break
                elif opcoes == 2:
                    escolha = 2
                    os.system("cls")
                    Jogos.escolha_jogo()
                else:
                    print("Opção Inválida!")

            else:
                print("Você não digitou um número!")
                print("Tenta de novo!")


        print("\nFim do jogo")

if __name__ == "__main__":
    start_adivinhacao()
