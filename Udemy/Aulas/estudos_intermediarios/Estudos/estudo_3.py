login = dict(usuario = 'Felipe', senha = 'FMO')

usuario_digitado = input('Digite o Usuarioa: ')
senha_digitada = input('Digite a senha: ')

if login['usuario'] == usuario_digitado:
    if login['senha'] == senha_digitada:
        print(f'Bem-Vindo {login["usuario"]}')
    else:
        print('Senha Invalida!')
else:
    print('Usuario não existe')