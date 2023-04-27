perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'Quanto que é 2+2? ',
        'respostas' : {'a' : '4', 'b' : '5', 'c' : '3',},
        'resposta_certa' : 'a',
    },
    'Pergunta 2' : {
        'pergunta' : 'Quanto que é 2*3? ',
        'respostas' : {'a' : '4', 'b' : '10', 'c' : '6',},
        'resposta_certa' : 'c',
    },
}

respostas_certas = 0

print('\n---Prova de Múltipla Escolha---')

for pk, pv in perguntas.items():
    print(f'\n{pk}\n {pv["pergunta"]}')
    print('\tEscolha:')
    for rk, rv in pv["respostas"].items():
        print(f'\t[{rk}] : {rv}')

    resposta_digitada = input('\tR: ')

    if resposta_digitada == pv['resposta_certa']:
        respostas_certas += 1

quantidades_perguntas = len(perguntas)
porcentagem_certas = respostas_certas / quantidades_perguntas * 100

if porcentagem_certas >= 60:
    print(f'\nAprovado com {porcentagem_certas}%')
    print('Parabens!')
elif porcentagem_certas <= 59 or porcentagem_certas >= 50:
    print(f'\nSua nota foi {porcentagem_certas}%, você está de recuperação!')
else:
    print(f'\nSua nota foi {porcentagem_certas}%, você está reprovado!')