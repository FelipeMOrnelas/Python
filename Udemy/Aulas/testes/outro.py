def LongestWord(sen):
    sen = str(sen)
    tam_palavras = list()
    caracteres = '!@#$%¨&*()'

    for letra in range(len(caracteres)):
        sen = sen.replace(caracteres[letra], "")

    sen = sen.split()

    for palavra in sen:
        tam_palavras.append(len(palavra))

    maior = max(tam_palavras)
    print(maior)

    for a, b in zip(sen, tam_palavras):
        print(f'Epa:{a}')
        if b == maior:
            sen = a

    


# keep this function call here
print(LongestWord(input("Digita: ")))

