from functools import lru_cache

@lru_cache(maxsize=34)
def troca_sinal(func, n):
    """
    :param func: Função que gera e calcula pontos no polinômio de func
    :param n: Número de nós
    :return: Lista com intervalos em que ocorre a troca de sinal no polinômio
    Função que analisa o polinômio de func em busca
    de pontos em que ocorre a troca_sinal, para posteriormente
    refinar o resultado. Trata-se de uma aplicação do método da
    dicotomia"""
    k = n + 5 * n  # round(n / 2)  # Intervalo do passo do range
    # criamos a variável para armazenar os pontos em que a troca de sinais ocorre
    troca_sinal = []
    # criamos uma variável temporária para comparar o sinal da função a cada ponto
    temp0 = func(x=(0) / k, n=n)
    for i in range(0, k):
        temp1 = func(x=(i + 1) / k, n=n)
        if temp1 * temp0 < 0:
            troca_sinal.append([i / k, (i + 1) / k])
        temp0 = temp1
    return troca_sinal

def dicotomia(intervs, n, func):
    """
    :param intervs: lista com pares de intervalos em que ocorre a troca de sinal
    :param n: Número de nós
    :param func: Função que gera e calcula pontos no polinômio de legendre
    :return: None. Apenas manipula uma lista pre-existente
    Essa função foi escrita para refinar o método da dicotomia
    quando recebe uma lista com pares de intervalos, e executa o
    método sobre o polinômio de legendre"""
    for i in intervs:
        valor_medio = (i[0] + i[1]) / 2
        if func(valor_medio, n) * func(i[0], n) < 0:
            i[1] = valor_medio
        else:
            i[0] = valor_medio


def confere_precisao(lista, precisao_da_aproximacao, func1, n, func2):
    """
    :param lista: lista com pares de intervalos em que ocorre a troca de sinal
    :param precisao_da_aproximacao: Variável que dita qual a precisão da aproximação
    :param func1: Função que refina os intervalos encontrados reaplicando o método da dicotomia
    :return: None. Apenas manipula uma lista pre-existente
    Como foram feitos espaçamentos regulares, a precisão
    será igual para todos os termos e,para poupar
    processamento, será analisado apenas
    um dos valores de x[j].
    Esta função repete o método da dicotomia até que se
    alcance a precisão pretendida."""
    precisao = (lista[0][1] - lista[0][0]) / 2
    while precisao > precisao_da_aproximacao:
        func1(lista, n, func2)
        precisao = (lista[0][1] - lista[0][0]) / 2


