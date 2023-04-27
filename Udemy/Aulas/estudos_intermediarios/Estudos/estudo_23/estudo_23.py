'''
Trabalhando com a Criação de Aqruivos
w = apaga tudo que contem e escreve o novo
a = escreve tudo no final da linha
r = ler
'a ou w' com + = escrever e ler
'''

with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.seek(0)
    print(file.read())


# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha 1')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()