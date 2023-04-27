from time import time
from time import sleep

def velocidade(funcao):
    """
    Função decoradora: Verifica o tempo que uma função leva para executar
    """
    def envolve(*args, **kwargs):
        """ Função que envolve e executa outra função """
        # Tempo inicial
        start = time()
        # Executa a função
        resultado = funcao(*args, **kwargs)
        # Tempo final
        end = time()
        # Resultado de tempo em ms
        tempo = (end - start) * 1000
        # Mostra o tempo
        print(f'\nA função levou {tempo:.2f}ms para ser executada.')
        # Retorna a função original executada
        return resultado
    # Retorna a função que envolve
    return envolve


@velocidade
def demora(qtd):
    """ Função decorada """
    for i in range(qtd):
        print(i, end='')


# Executa a função decorada
demora(10000)