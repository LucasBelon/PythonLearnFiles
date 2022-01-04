"""Esta é a função obtida pelo site do github, não é da autoria do grupo.
Calcula o valor do polinômio de Legendre de qualquer grau utilizando a fórmula
de Bonnet:
$$(n + 1) P_{n+1}(x) = (2n + 1) x P_n(x) - n P_{n-1}$$"""
from functools import lru_cache

@lru_cache(maxsize=34)
def legendre(x, n):
    """
    Params:
    x: (float) Ponto da reta real no qual o polinômio será calculado.
    n: (int) Grau do polinômio.
    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * legendre(x, n - 1) - (n - 1) * 
                legendre(x, n - 2)) / n


