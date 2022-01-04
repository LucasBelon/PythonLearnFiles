def calcIntegral(dicio, retifica, raiz, pesos, valor_round):
    """
    :param dicio: Retorna funções e o valor da integral exata
    :param retifica: Função de transporte linear de [a,b] para [-1, 1]
    :param raiz: lista de raízes de legendre (calculado de -1 a 1)
    :param pesos: lista de pesos (calculado de -1 a 1)
    :return: Valor da integral dupla definida
    """
    # iniciamos uma variável que irá somar o valor de
    # cada parcela da integral externa
    somatorio = 0
    # Obtemos o coeficiente a ser aplicado na parcela da integral
    coef_alpha_tr_lin_ext = (dicio["limB"] - dicio["limA"]) / 2
    # Obtemos a lista de raizes retificadas que serão usadas
    # como variável x nas funções
    raiz_retificadaX = retifica(
            lista=raiz, a=dicio["limA"], b=dicio["limB"])
    for i in range(len(raiz)):
        # Iniciamos uma variável que irá somar o valor de cada
        # parcela da integral interna
        somatorio_interno = 0
        # selecionamos a raiz que nos interessa e, para facilidade de 
        # notação, a nomeamos de x
        x = raiz_retificadaX[i]
        # print("Valores para X= ",x,sep='')
        # Obtemos o coeficiente a ser aplicado na parcela da integral
        coef_alpha_tr_lin_int = (dicio["h_x"](x) - dicio["g_x"](x)) / 2
        # Obtemos a lista de raizes retificadas que serão usadas como 
        # variável y nas funções
        raiz_retificadaY = retifica(
                lista=raiz, a=dicio["g_x"](x), b=dicio["h_x"](x))
        for j in range(len(raiz)):
            # selecionamos a raiz que nos interessa e, para facilidade de
            # notação, a nomeamos de y
            y = raiz_retificadaY[j]
            # print(f"Y = {y}; ")
            # Incrementamos nossas parcelas de integral à variável
            somatorio_interno += pesos[j] * dicio["f_xy"](x, y)
            # print(f"JX= {somatorio_interno}")
        # Aplicamos o coeficiente, e o peso correto à parcela da 
        # integral interna, e adicionamos à integral externa
        somatorio += pesos[i] * coef_alpha_tr_lin_int * somatorio_interno
        # print(f"J= {somatorio}")
    # Aplicamos o coeficiente alpha à integral
    somatorio = somatorio * coef_alpha_tr_lin_ext
    # print(f"Somatório com o coef aplicado = {somatorio}")
    return round(somatorio, valor_round)

