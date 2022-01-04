from itertools import combinations

def completa_raizes(lista, flag):
    """
    A partir dos pontos obtidos em que há a troca de sinal utilizamos essa
    função para criar uma lista completa com todas as raízes.
    Foi economizado processamento para obter as raízes, agora basta espelhá-las
    e adicionar o zero, se necessário.

    :param flag: Lista de raízes positivas não nulas do polinômio de legendre
    :return: raizes - lista com todas as raízes, incluindo as não positivas e nulas
    do polinômio de legendre
    Esta função foi escrita com fim de obter uma lista com todas as raízes do polinômio de legendre
    """
    raizes = []
    for i in range(len(lista)):
        raizes.append(-(lista[-i - 1][0] + lista[-i - 1][1]) / 2 )
    if flag == 1:
        # Esta é a flag anteriormente definida para a existência do zero como raiz.
        raizes.append(0)
    for i in range(len(lista)):
        raizes.append((lista[i][0] + lista[i][1]) / 2)
    return raizes

def pesos_Wi(lista, n, a, b):
    """
    Esta função utiliza-se das raízes para realizar uma integração polinomial a
    fim de se obter os pesos necessários para se aplicar ao algoritmo de gauss.

    :param lista: lista com todas as raízes do polinõmio de legendre do n em questão
    :param n: Número de nós, usado como range do loop
    :param a: limite inferior da integral
    :param b: limite superior da integral
    :return: lista com os pesos ordenados, com índice alinhado ao índice das raízes
    Essa função foi montada a fim de obter os pesos sejam quais forem, para qualquer número de nós
    """
    pesos = []
    for w in range(n):
        cte = 1
        listatemp = []
        integral = 0
        for g in range(n - 1):
            listatemp.append(lista[w - g - 1])
            cte = cte * (lista[w] - listatemp[g])
        # lista temp funciona bem
        # CTE funciona bem
        for g in range(n):
            termo = ((b ** (n - g)) - (a ** (n - g))) / (n - g)
            if g % 2 == 1:
                termo = termo * -1
            # termo está ok. Faltam as somatórias
            soma = 0
            for i in combinations(listatemp, g):
                mult = 1
                for j in i:
                    mult = mult * j
                soma += mult
            # soma está check
            integral += soma * termo
        pesos.append(integral / cte)
    return pesos


def retifica(lista, a, b):
    """
    Essa função realiza o transporte linear das raízes do polinômio de legendre
    para o devido intervalo de integração, como visto no desenvolvimento 
    teórico do trabalho.

    :param lista: lista de raízes do polinômio de legendre original
    :param a: limite inferior de integração
    :param b: limite superior de integração
    :return: Lista com o transporte linear de cada raiz da função
    """
    retificado = []
    for i in lista:
        retificado.append(((b - a) * i + b + a) / 2)
    return retificado



