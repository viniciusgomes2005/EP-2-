def define_posicoes(linha,coluna,orientacao,tamanho):
    posicao_ocupada=[]
    for y in range(tamanho):
        if orientacao =='vertical':
            posicao_ocupada.append([linha+y,coluna])
        if orientacao =='horizontal':
            posicao_ocupada.append([linha,coluna+y])
    return posicao_ocupada
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
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    else:
        tabuleiro[linha][coluna]='-'
    return tabuleiro
def posiciona_frota(frota):
    grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],]
    for variavel0 in frota.values():
        for variavel1 in variavel0:
            for variavel2 in variavel1:
                linha=variavel2[0]
                coluna=variavel2[1]
                grid[linha][coluna]=1
    return grid
def afundados(frota,grid):
    naviosf=0
    for navios in frota.values():
        for navio in navios:
            variavel3=0
            while variavel3<len(navio):
                localizacao=navio[variavel3]
                linha= localizacao[0]
                coluna=localizacao[1]
                if grid[linha][coluna]=='X':
                    del navio[variavel3]
                    variavel3-=1
                variavel3+=1
            if navio==[]:
                naviosf+=1
    return naviosf
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
#porta aviões
print("Insira as informações referentes ao navio porta-aviões que possui tamanho 4")
linhapa=int(input("Qual a linha?"))
colunapa=int(input("Qual a coluna"))
orientacaopa=int(input("Qual a orientação"))
if orientacaopa==1:
    orientacaopa='vertical'
elif orientacaopa==2:
    orientacaopa="horizontal"
while not posicao_valida(frota,linhapa,colunapa,orientacaopa,4):
    print("Esta posição não está válida!")
    print("Insira as informações referentes ao navio porta-aviões que possui tamanho 4")
    linhapa=int(input("Qual a linha?"))
    colunapa=int(input("Qual a coluna"))
    orientacaopa=int(input("Qual a orientação"))
    if orientacaopa==1:
        orientacaopa='vertical'
    elif orientacaopa==2:
        orientacaopa="horizontal"
frota=preenche_frota(frota,"porta-aviões",linhapa,colunapa,orientacaopa,4
)
for i in range(2):
    #navio tanque
    print("Insira as informações referentes ao navio navio-tanque que possui tamanho 3")
    linhant=int(input("Qual a linha?"))
    colunant=int(input("Qual a coluna"))
    orientacaont=int(input("Qual a orientação"))
    if orientacaont==1:
        orientacaont='vertical'
    elif orientacaont==2:
        orientacaont="horizontal"
    while not posicao_valida(frota,linhant,colunant,orientacaont,3):
        print("Esta posição não está válida!")
        print("Insira as informações referentes ao navio navio-tanque que possui tamanho 3")
        linhant=int(input("Qual a linha?"))
        colunant=int(input("Qual a coluna"))
        orientacaont=int(input("Qual a orientação"))
        if orientacaont==1:
            orientacaont='vertical'
        elif orientacaont==2:
            orientacaont="horizontal"
    frota=preenche_frota(frota,"navio-tanque",linhant,colunant,orientacaont,3)
#contratorpedeiro
for i in range(3):
    print("Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2")
    linhac=int(input("Qual a linha?"))
    colunac=int(input("Qual a coluna"))
    orientacaoc=int(input("Qual a orientação"))
    if orientacaoc==1:
        orientacaoc='vertical'
    elif orientacaoc==2:
        orientacaoc="horizontal"
    while not posicao_valida(frota,linhac,colunac,orientacaoc,2):
        print("Esta posição não está válida!")
        print("Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2")
        linhac=int(input("Qual a linha?"))
        colunac=int(input("Qual a coluna"))
        orientacaoc=int(input("Qual a orientação"))
        if orientacaoc==1:
            orientacaoc='vertical'
        elif orientacaoc==2:
            orientacaoc="horizontal"
    frota=preenche_frota(frota,"contratorpedeiro",linhac,colunac,orientacaoc,2)
#submarino
for i in range(4):
    print("Insira as informações referentes ao navio submarino que possui tamanho 1")
    linhas=int(input("Qual a linha?"))
    colunas=int(input("Qual a coluna"))
    while not posicao_valida(frota,linhas,colunas,"horizontal",1):
        print("Esta posição não está válida!")
        print("Insira as informações referentes ao navio submarino que possui tamanho 1")
        linhas=int(input("Qual a linha?"))
        colunas=int(input("Qual a coluna"))
    frota=preenche_frota(frota,"submarino",linhas,colunas,"horizontal",1)
#------------------------------------------
#------------------------------------------
#------------------------------------------
#------------------------------------------
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiro_oponente=posiciona_frota(frota_oponente)
