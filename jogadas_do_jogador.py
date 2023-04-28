def preenche_frota(dic_frota,nome_navio,linha,coluna,orientacao, tamanho):
    if len(dic_frota)==0:
        dic_frota[nome_navio]=[define_posicoes(linha,coluna,orientacao, tamanho)]
        return dic_frota
    for variavel, variavel1 in dic_frota.items():
        if nome_navio not in dic_frota:
            dic_frota[nome_navio]=[define_posicoes(linha,coluna,orientacao,tamanho)]
            return dic_frota
        elif nome_navio == variavel:
            variavel1.append(define_posicoes(linha,coluna,orientacao, tamanho))
    return dic_frota