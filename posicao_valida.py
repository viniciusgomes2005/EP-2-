def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    novo_navio=define_posicoes(linha,coluna,orientacao,tamanho)
    for posisao in novo_navio:
        if posisao[0]>9 or posisao[0]<0:
            return False
        if posisao[1]>9 or posisao[1]<0:
            return False
    for navios in frota.values():
        for navio in navios:
                for posisao in novo_navio:
                    if posisao in navio:
                        return False
    return True