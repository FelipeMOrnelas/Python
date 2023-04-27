login = dict(Felipe = 'FMO', Igor = 'IGR')
verificado = 0

usuario_digitado = input('Digite o Usuarioa: ')
senha_digitada = input('Digite a senha: ')

for k, v in login.items():
    if usuario_digitado == k and senha_digitada == v:
        verificado = k
        break
    else:
        verificado = 0

if verificado == 0:
    print('\nInvalido!')
else:
    print(f'\nBem Vindo {verificado}')