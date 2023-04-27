def adicionar_lista(tarefa):
    lista_de_tarefas.append(tarefa)
    return lista_de_tarefas

def remover(tarefa):
    tarefa.pop()
    return tarefa

def refazendo_tarefa(lista_de_tarefas, refazer):
    lista_de_tarefas.pop(-1)
    lista_de_tarefas.append(refazer)
    return lista_de_tarefas

lista_de_tarefas = []


while True:
    print('---Lista de Tarefas---')
    print('1 - Adicionar\n2 - Visualizar\n3 - Remover\n4 - Refazer\n5 - Encerrar')
    resposta = input('R: ')
    print('\n')

    if resposta.isdigit():
        resposta = int(resposta)
    else:
        print('Opção invalida')
        print('Tenta de novo...\n')
        continue

    if resposta == 1:
        tarefa = input('Digite a Tarefa que deseja adicionar: ')
        adicionar_lista(tarefa)
        print('Tarefa adicionada com sucesso!\n')
        continue
    elif resposta == 2:
        if len(lista_de_tarefas) == 0:
            print('Lista de Tarefas Vazia!')
        else:
            print('Lista de Tarefas: ')
            for numerar, visualizar in enumerate(lista_de_tarefas):
                print(f'\t{numerar+1} - {visualizar}')
        print('\n')
        continue
    elif resposta == 3:
        if len(lista_de_tarefas) == 0:
            print('Lista de Tarefas Vazia\nNão tem o que remover aqui!\nVoltando para o início...\n')
            continue
        else:
            print('Removendo a última tarefa...')
            remover(lista_de_tarefas)
            print('Removido com sucesso!\n')
    elif resposta == 4:
        if len(lista_de_tarefas) == 0:
            print('Lista de Tarefas Vazia\nNão tem o que alterar aqui!\nVoltando para o início...\n')
            continue
        else:
            print(f'Refazendo a última tarefa adicionada ({lista_de_tarefas[-1]})')
            refazer = input('Digite a nova terafa no lugar da última tarefa: ')
            refazendo_tarefa(lista_de_tarefas, refazer)
            print('Refeito com sucesso!\n')
    elif resposta == 5:
        print('Até Logo!')
        break
    else:
        print('Opção invalida')
        print('Tenta de novo...\n')
        continue