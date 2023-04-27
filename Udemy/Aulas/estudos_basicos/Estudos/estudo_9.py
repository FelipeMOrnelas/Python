# Exemplo 1
# logado = False
#
# msg = 'Usuário Logado!' if logado else 'Usuário precisa fazer login!'
#
# print(msg)

# Exemplo 2
# idade = 17
# maior_idade = (idade >= 18)
# msg = 'Pode acessar' if maior_idade else 'Não pode acessar'
# print(msg)

# Exemplo 3
senha = 'FMO'
senha_entrada = input("Digite a senha para entrar: ")
acesso = (senha == senha_entrada)
msg = 'Senha correta' if acesso else 'Senha incorreta'

print(msg)