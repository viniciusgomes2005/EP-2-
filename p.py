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
    while not posicao_valida(frota,linhac,colunac,"horizontal",1):
        print("Esta posição não está válida!")
        print("Insira as informações referentes ao navio submarino que possui tamanho 1")
        linhas=int(input("Qual a linha?"))
        colunas=int(input("Qual a coluna"))
    frota=preenche_frota(frota,"submarino",linhas,colunas,"horizontal",1)
#------------------------------------------
print(frota)
