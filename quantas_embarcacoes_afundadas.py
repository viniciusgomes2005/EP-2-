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