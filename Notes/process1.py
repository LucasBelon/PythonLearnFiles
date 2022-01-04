def main():
    # coding: utf-8

    # Calculando números primos
    """
    lista = []
    for n in range(2,1001):
        for x in range(2,n):
            if n % x == 0:
                print(f"{n} é igual a {x} * {n//x}")
                break
        else:
            print(f"{n} é primo")
    """

    # Compreensão de dicionários
    amigos = ['Gabriel Beltrame', 'Karina Lazari',
                'Mateus Brito', 'Heitor Borges']
    indice_afinidade = [10, 8, 5, 8]
    dicionario = {
        amigos[i]: indice_afinidade[i]
        for i in range(len(amigos))
        if indice_afinidade[i] >= 5
    }
    print(dicionario)
    dicionario2 = dict(zip(amigos, indice_afinidade))
    print(dicionario2)
