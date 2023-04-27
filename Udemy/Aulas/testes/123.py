def LongestWord(sen):

  sen = str(sen).split()
  tam_palavras = list()

  for palavra in sen:
    tam_palavras.append(len(palavra))

  maior = max(tam_palavras)

  for a, b in zip(sen, tam_palavras):
    if b == maior:
      sen = a

  return sen

# keep this function call here
print(LongestWord(input('Digita: ')))

