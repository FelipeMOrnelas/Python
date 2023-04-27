l2 = ['Felipe', 'Laiane', 'Talita']
ex2 = [v.replace('e', '@').upper() for v in l2]
b = 0

l1 = ['1','2','3','1','1']
ex1 = [v.replace('1', '0') for v in l1]
teste = [a for a in ex1 if a != '0']

l3 = list(range(100))
ex3 = [v for v in l3 if v % 2 == 0]


l4 = list(range(100))
ex4 = [v for v in l4 if v % 3 == 0 if v % 8 == 0]

i = 1

while i <= 3:
    l5 = input('Digite um número: ')
    ex5 = 'Numero Invalido' if not l5.isdigit() else 'Par' if int(l5) % 2 == 0 else 'Impar'
    print(ex5)
    i += 1