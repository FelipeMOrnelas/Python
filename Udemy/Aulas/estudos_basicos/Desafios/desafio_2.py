# Desafio_2
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada.
"""

horario = input("Digite um horario (0-23): ")

if horario.isdigit():
    horario = int(horario)
    if(horario > 23):
        print("O horário não existe!")
    else:
        if(horario >= 6 and horario <= 11):
            print("Bom Dia!")
        elif(horario >= 12 and horario <= 17):
            print("Boa Tarde!")
        elif(horario >= 18 and horario <= 23):
            print("Boa Noite!")
        else:
            print("Boa Madrugada!")
else:
    print("Digitou errado")