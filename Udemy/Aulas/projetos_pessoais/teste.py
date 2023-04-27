lista = 'XLIV'
opa = []
fim = len(lista)
for i, n in enumerate(lista):
    if i+1 == fim:
        print('acabou')
        continue
    else:
        if lista[i:i+1+1] == 'IV':
            print(lista[i:i+1+1])
            opa.append(lista[i:i+1+1])
            lista = lista.replace('I','', i)
            lista = lista.replace('V','', i+1)
        elif lista[i:i+1+1] == 'XL':
            print(lista[i:i+1+1])
            opa.append(lista[i:i+1+1])
            lista = lista.replace('X','', i)
            lista = lista.replace('L','', i+1)
        elif lista[i] == 'X':
            print(lista[i])
            opa.append(lista[i])
        elif lista[i] == 'V':
            print(lista[i])
            opa.append(lista[i])
        elif lista[i] == 'I':
            print(lista[i])
            opa.append(lista[i])

print(opa)

# ----------------------------------------------------------
# lista = ['M','M','C','M','X','C','I','X']
#
# for i, n in enumerate(lista):
#     if lista[i] + lista[i+1] == 'IV':
#         lista.pop(i)
#         lista.pop(i)
#         lista.insert(i, 'IV')
#     elif lista[i] + lista[i+1] == 'IX':
#         lista.pop(i)
#         lista.pop(i)
#         lista.insert(i, 'IX')
#     elif lista[i] + lista[i+1] == 'XL':
#         lista.pop(i)
#         lista.pop(i)
#         lista.insert(i, 'XL')
#     elif lista[i] + lista[i+1] == 'XC':
#         lista.pop(i)
#         lista.pop(i)
#         lista.insert(i, 'XC')
#     elif lista[i] + lista[i+1] == 'CD':
#         lista.pop(i)
#         lista.pop(i)
#         lista.insert(i, 'CD')
#     elif lista[i] + lista[i+1] == 'CM':
#         lista.pop(i)
#         lista.pop(i)
#         lista.insert(i, 'CM')
# ---------------------------------------------------------------
#
# for i, n in enumerate(lista2):
#     if lista2[i] + lista2[i+1] == 'IV':
#         lista2.pop(i)
#         lista2.pop(i)
#         lista2.insert(i, 'IV')
#     elif lista2[i] + lista2[i+1] == 'IX':
#         lista2.pop(i)
#         lista2.pop(i)
#         lista2.insert(i, 'IX')
#     elif lista2[i] + lista2[i+1] == 'XL':
#         lista2.pop(i)
#         lista2.pop(i)
#         lista2.insert(i, 'XL')
#     elif lista2[i] + lista2[i+1] == 'XC':
#         lista2.pop(i)
#         lista2.pop(i)
#         lista2.insert(i, 'XC')
#     elif lista2[i] + lista2[i+1] == 'CD':
#         lista2.pop(i)
#         lista2.pop(i)
#         lista2.insert(i, 'CD')
#     elif lista2[i] + lista2[i+1] == 'CM':
#         lista2.pop(i)
#         lista2.pop(i)
#         lista2.insert(i, 'CM')

# print(lista)
# print(lista2)




# lista = ['j','l','k','M', 'j']
# contador = 0
# teste = 'jl'
# ultimo = len(lista)
# ultimo -= 1
#
# for n, i in enumerate(lista):
#     if n == ultimo:
#         print('ultimo')
#         contador += 1
#         print(contador)
#     elif lista[n] + lista[n+1] == 'jl':
#         print('oi')
#         n += 3
#         print(n)
#         contador -= 1
#         print(contador)
#     elif lista[n] == 'j':
#         contador += 1
#         print(contador)
#     elif lista[n] == 'l':
#         contador += 1
#         print(contador)
#     elif lista[n] == 'k':
#         contador += 1
#         print(contador)
#     elif lista[n] == 'M':
#         contador += 1
#         print(contador)
#     elif lista[n] == 'j':
#         contador += 1
#         print(contador)
#
# print(f'Final {contador}')

# numero = 'IIV'
# contador = 0
#
# for n, i in enumerate(numero):
#     if numero[n] == 'I':
#         contador += 1
#     elif numero[n] == 'V':
#         contador += 5
#     elif numero[n] == 'X':
#         contador += 10
#     elif numero[n] == 'L':
#         contador += 50
#     elif numero[n] == 'C':
#         contador += 100
#     elif numero[n] == 'D':
#         contador += 500
#     elif numero[n] == 'M':
#         contador += 1000
#
# print(contador)