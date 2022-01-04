"""
Implementação do método de Gauss para integrais duplas.
Código auxiliar:
https://github.com/Hevenicio/Legendre-Polynomials-in-Python/blob/master/Legendre.py
Pseudo-código do livro Burden & Faires quanto à integral dupla do método de gauss
"""

def main(n, opcao_da_funcao):
    from time import time
    start = time()

    from math import sqrt, e, pi, erf

    from utils.legendre import legendre
    from utils.dicotomia import troca_sinal as troca_sinal_legendre
    from utils.dicotomia import dicotomia
    from utils.dicotomia import confere_precisao 
    from utils.pesos_raizes import completa_raizes
    from utils.pesos_raizes import pesos_Wi
    from utils.pesos_raizes import retifica
    from utils.integral import calcIntegral
    """
    Como encontrar as raízes do polinômio de legendre?
    Eu sei que o polinômio de legendre se torna estritamente
    crescente e maior do que 1 no ponto x=1 para qualquer 'n', 
    sei que as raízes são mais ou menos igualmente espaçadas,
    simétricas e que são em total n+1 raízes quando 'n' é ímpar.
    Então basta que eu caminhe de 0 a 1, com passos pequenos ecompatíveis.
    Com isso encontro os intervalos em que a função troca de sinal
    e a partir destes pontos aplico o método da dicotomia até
    que a precisão se faça suficiente.
    Quando 'n' é impar o zero é uma raíz. Quando 'n' é par não.
    A função está no diretório 'utils',
    """

    #####
    #n = 4
    #opcao_da_funcao = 4
    #####
    
    # intervalo de integração para os pesos
    a, b = -1, 1
    precisao_da_aproximacao = 1e-16
    string = f"""
O menor valor de 'n' aceitável para este programa é n=2. Não recomenda-se
testar valores de n > 20, pois o tempo de processamento se torna 
demasiadamente longo. Este programa foi construído para suportar até n=34, mas
não é recomendado, a não ser que sua máquina tenha um clock de processador
praticamente infinito e sua memória RAM seja maior do que 64GB.
A precisão utilizada é de {str(precisao_da_aproximacao)}.
"""
    #print(string)

    """
    n = int(
        input(
        "Diga quantos nós devem existir [são aceitos apenas números inteiros]: "
        )
        )
    while n not in range(2, 34):
        print("Escolha uma opção válida, um número inteiro de 2 a 34")
        n = int(
            input(
            "Diga quantos nós devem \
                    existir [são aceitos apenas números inteiros]: "
            )
            )
    """
    string = """Digite o número da função que você deseja executar:
Exemplo 1
Função f(x, y) = 1; limite inferior g(x) = 0; limite superior h(x) = 1           - Tecle [1]
Função f(x, y) = 1-x-y; limite inferior g(x) = 0; limite superior h(x) = 1-x     - Tecle [2]
Exemplo 2
f(x, y) = 1; limite inferior g(x) = 0; limite superior h(x) = 1 - x^2            - Tecle [3]
f(x, y) = 1; limite inferior g(x) = 0; limite superior h(x) = sqrt(1-x)          - Tecle [4]
Exemplo 3
f(x, y) = e^(y/x); limite inferior g(x) = x^3; limite superior h(x)=x^2          - Tecle [5]
f(x, y) = sqrt( (((y*(e^(y/x)))/(x^2))^2) + (((e^(y/x))/x)^2) + 1); 
limite inferior g(x) = x^3; limite superior h(x)=x^2                            - Tecle [6]
Exemplo 4
f(x, y) = |x|; limite inferior g(x) = 3/4; limite superior h(x) = sqrt(1-x^2)    - Tecle [7]
f(x, y) = |y|; limite inferior g(x) = 0; limite superior h(x) = e^-x^2           - Tecle [8]"""
    #print(string)


    # opcao_da_funcao = int(input("Sua escolha: "))
    while opcao_da_funcao not in range(1, 9):
        print("Escolha uma função válida, um número inteiro de 1 a 8")
        opcao_da_funcao = int(input("Sua escolha: "))



    # Garantimos que caso a função seja impar o 0 estará entre suas raízes
    # a variável raiz funciona como uma flag do tipo True/False
    """if n % 2 != 0:
        raiz = 1
    else:
        raiz = 0"""
    flag = 1 if n%2 !=0 else 0
    # Armazenamos as trocas de sinal do polinômio de legendre
    raiz = troca_sinal_legendre(legendre, n)
    # e refinamos o resultado
    confere_precisao(raiz, precisao_da_aproximacao, 
            dicotomia, n, legendre)

    # Agora vamos nos preocupar com as raízes, 
    # a começar por completá-las e organizá-las.
    raiz = completa_raizes(raiz, flag)

    # liberamos um pouquinho de memória
    del flag

    # Começamos a tratar a precisão aqui ----------------
    precisao_invertida = int(1 / precisao_da_aproximacao)
    if precisao_invertida % 2 == 1:
        precisao_invertida += 1
    # liberamos um pouquinho de memória
    del precisao_da_aproximacao
    # Vamos tratar nossa variável para que ela nos arredonde 
    # as casas decimais que queremos
    valor_round = 0
    # Inicio meu contador
    while precisao_invertida >= 10:
        precisao_invertida = precisao_invertida / 10
        valor_round = valor_round + 1
    
    # liberamos um pouquinho de memória
    del precisao_invertida

    # Aplicamos o arredondamento às raízes
    for i in range(len(raiz)):
        raiz[i] = round(raiz[i], valor_round)

    # Hora de calcular os pesos.
    # intervalo de integração: [a, b] definido no começo do programa.
    # armazenamos os pesos numa variável
    pesos = pesos_Wi(raiz, n, a, b)
    # Arredondamos os valores de cada um dos pesos
    for i in range(len(pesos)):
        pesos[i] = round(pesos[i], valor_round)

    # Exemplo 1
    dicio1 = {
            "limA" : 0,
            "limB" : 1,
            "f_xy" : lambda x, y : 1,
            "g_x" : lambda x : 0,
            "h_x" : lambda x : 1,
            "resultado_exato" : 1
            }

    dicio2 = {
            "limA" : 0,
            "limB" : 1,
            "f_xy" : lambda x, y : 1 - x - y,
            "g_x" : lambda x : 0,
            "h_x" : lambda x : 1 - x,
            "resultado_exato" : 1 / 6
            }

    # Exemplo 2
    dicio3 = {
            "limA" : 0,
            "limB" : 1,
            "f_xy" : lambda x, y : 1,
            "g_x" : lambda x : 0,
            "h_x" : lambda x : 1 - x ** 2,
            "resultado_exato" : 2 / 3
            }

    dicio4 = {
            "limA" : 0,
            "limB" : 1,
            "f_xy" : lambda x, y : 1,
            "g_x" : lambda x : 0,
            "h_x" : lambda x : sqrt(1 - x),
            "resultado_exato" : 2 / 3
            }

    # Exemplo 3
    dicio5 = {
            "limA" : 0.1,
            "limB" : 0.5,
            "f_xy" : lambda x, y : e ** (y/x),
            "g_x" : lambda x : x ** 3,
            "h_x" : lambda x : x ** 2,
            "resultado_exato" : 0.0333056
            }

    dicio6 = {
            "limA" : 0.1,
            "limB" : 0.5,
            "f_xy" : lambda x, y : \
                    sqrt((((y * (e ** (y / x))) / (x ** 2)) 
                    ** 2) + (((e ** (y / x)) / x) ** 2) + 1),
            "g_x" : lambda x : x ** 3,
            "h_x" : lambda x : x ** 2,
            "resultado_exato" : 0.105498
            }

    # Exemplo 4
    dicio7 = {
            "limA" : 0,
            "limB" : sqrt(7)/ 4,
            "f_xy" : lambda x, y : 2 * pi * abs(x), 
            "g_x" : lambda x : 3/4,
            "h_x" : lambda x : sqrt(1 - (x ** 2)),
            "resultado_exato" : (1 / (3 * 16)) * (3 - (1 / 4)) * pi
            }


    dicio8 = {
            "limA" : -1,
            "limB" : 1,
            "f_xy" : lambda x, y : 2 * pi * abs(y), 
            "g_x" : lambda x : 0,
            "h_x" : lambda x : e ** (- (x ** 2)),
            "resultado_exato" : (sqrt(2) / 2) * (pi ** (3 / 2)) * erf(sqrt(2))
            }

    # Implementamos uma tupla para facilitar a montagem do menu de funções
    funcoes_exemplo = (dicio1, dicio2, dicio3, dicio4, 
                        dicio5, dicio6, dicio7, dicio8)

    funcao = funcoes_exemplo[opcao_da_funcao - 1]
    string_final = \
f"""O valor calculado da integral é: {str(calcIntegral(dicio=funcao,
retifica=retifica, raiz=raiz, pesos=pesos, valor_round=valor_round
))}
O valor exato da integral é:     {str(funcao["resultado_exato"])}
O valor de 'n' que você escolheu é: {n}
O tempo gasto foi de {round(time() - start, 2)} segundos"""
    #print(string_final)
    print(f"\nO tempo gasto foi de {round(time() - start, 4)} segundos \
            \nn={n} e \
            \nopcaofuncao = {opcao_da_funcao}\
            \nvalorIntegral = {str(calcIntegral(dicio=funcao ,retifica=retifica, raiz=raiz, pesos=pesos, valor_round=valor_round))}"
        )

for i in range(2, 34):
    main(n=i, opcao_da_funcao=5)
# input("O programa terminou. Tecle enter para sair")
