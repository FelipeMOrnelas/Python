# Desafio_1
"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

n1 = input("Digite um número inteiro: ")

if n1.isdigit():
    n1 = int(n1)
    if n1 % 2 == 0:
        print(f"{n1} é par!")
    else:
        print(f"{n1} é impar!")
else:
    print("Não é um número inteiro!")
