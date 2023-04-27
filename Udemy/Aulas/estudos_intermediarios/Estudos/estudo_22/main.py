from vendas.calc_preco import reducao, aumento

valor = 10

preco_com_aumento = aumento(valor=valor, porcentagem=50, v=True)
preco_com_reducao = reducao(valor=valor, porcentagem=50, v=True)

print(preco_com_aumento)
print(preco_com_reducao)

