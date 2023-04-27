login = dict(Felipe = 'FMO', Igor = 'IGR')
verificado = 0
resposta1 = 'n/a'

print('----Login----')

while True:

    usuario_digitado = input('\nDigite o Usuárioa: ')
    senha_digitada = input('Digite a senha: ')

    for k, v in login.items():
        if usuario_digitado == k and senha_digitada == v:
            verificado = k
            break
        else:
            verificado = 0

    if verificado == 0:
        print('\nInválido!')
        continue
    else:
        print(f'\nBem Vindo {verificado}\n')
        resposta1 = input('Deseja alterar a senha? ')

    if resposta1 == 'sim':
        nova_senha = input('Digite uma nova senha: ')
        login[verificado] = nova_senha
        print(f'\nSua nova senha é: {login[verificado]}')
        verificado = 0
        continue
    else:
        print('\nAté Logo!')
        print('Saindo...')
        verificado = 0



