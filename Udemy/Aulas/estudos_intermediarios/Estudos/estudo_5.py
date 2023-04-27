clientes = dict({'Clientes1' : {'nome':'Luis', 'sobrenome':'Ferreira'},
                 'Clientes2' : {'nome':'Felipe', 'sobrenome':'Ornelas'},})

for cliente_k, cliente_v in clientes.items():
    print(f'\nExibindo {cliente_k}')
    for dados_k, dados_v in cliente_v.items():
        print(f'\t{dados_k}: {dados_v}')
