def define_posicoes(linha,coluna,orientacao,tamanho):
    posicao_ocupada=[]
    for y in range(tamanho):
        if orientacao =='vertical':
            posicao_ocupada.append([linha+y,coluna])
        if orientacao =='horizontal':
            posicao_ocupada.append([linha,coluna+y])
    return posicao_ocupada