sen = input('Digite a frase: ').split()
tam_palavras = list()
for palavra in sen:
    tam_palavras.append(len(palavra))

maior = max(tam_palavras)
for a, b in zip(sen, tam_palavras):
    if b == maior:
        print(a)
