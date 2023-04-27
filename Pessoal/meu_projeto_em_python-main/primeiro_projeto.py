import random

intervalo1 = int(input("Digite o primeiro intervalo: ")) #primeiro intervalo
intervalo2 = int(input("Digite o segundo intervalo: ")) #segundo intervalo

aleatorio = random.randrange(intervalo1, intervalo2) #Gerar um número aleatório nos intervalos fornecidos
print(aleatorio)

print("\nDescubra qual número eu escolhi nos intervalos", intervalo1, "e", intervalo2) #Digitar um numero
u = int(input("R: "))

while u != aleatorio: # u for diferente de aleatorio
    print("\nVocê errou")
    if u < aleatorio: # se o numero digitado for menor que o aleatorio
        for i in range(intervalo2):
            if i == aleatorio: # se i for igual ao aleatorio
                proximo = random.randrange(u, i) # gerar um numero aleatorio para orientar, para facilitar
                if proximo == u and aleatorio - proximo == 1: # se o numero gerado for igual ao numero que já foi digitado
                    print("Está entre",proximo, "e",proximo+2,"!")
                else:
                    print("\nEstá mais próximo de", proximo) # se o numero gerado for menor que o u
                u = int(input("Tenta Novamente: "))
                while u > aleatorio: # se  numero gerado for maior que o u
                    print("\nNumero muito alto")
                    u = int(input("Tenta Novamente, mas dessa vez um número menor: "))
    if u > aleatorio:
        while u > aleatorio:  # se  numero gerado for maior que o u
            print("\nNumero muito alto")
            u = int(input("Tenta Novamente, mas dessa vez um número menor: "))

print("\nVc venceu!!")



