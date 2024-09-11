from random import randint
import os

#cores para deixar o terminal bonitin


#reset cor
res='\033[0;00;00m'
#vermelho 
verm='\033[1;31;40m'
#verde
verd='\033[1;32;40m'
#amarelho
amar='\033[1;33;40m'

#lista de Mobs, tá mob pq é muita coisa pra muda, depois eu mudo isso para listaMobs
listaMobs=[]

#player
player={
    "nome": "Lotus",
    "level":20,
    "exp":0,
    "expMax":100,
    "hp":9000,
    "hpMax":9000,
    "dano":100
}

#menu principal
menuIniciar=[
    f"{verd}1. Iniciar batalha{res}",
    "2. Editar personagem",
    f"{verm}3. Sair{res}"
]
#menu de pause
menuPause=[
    "1. Voltar a batalha",
    "2. Reiniciar batalha",
    "3. Voltar ao menu incial",
    "4. Sair do jogo"
]

#lista de eventos
listaEventos=[]
#lista dos ultimos 2 eventos, ou seja, os ultimos movimentos
ultimosMov=[]

#mostrar menu inciar
def menuInicio():
    print("----------------------------")
    for opc in menuIniciar:
        print(opc)
    print("----------------------------")
#mostrar menu pause
def pause():
    print("----------------------------")
    for opc in menuPause:
        print(opc)
    print("----------------------------")

#cria um mob de um level aleatório da metade ao maximo do level do player
#apenas cria e retorna o mob
def criarMob(num, lvl):
    level=randint(lvl/2,lvl)
    novoMob={
        "nome":f"Mob #{num}", 
        "level":level,
        "dano": 5*level,
        "hp": 100*level,
        "hpMax": 100*level, 
        "exp":5*level     #quanto xp vai dropa
    }
    return novoMob


#gera uma quantidade de mobs e adiciona os na lista de mobs
#a quantidade de mobs depende do level do player
#por enquanto sera decidido manualmente
def gerarMobs(quant, lvl):
    num=0
    for i in range(quant):
        num+=1
        novoMob = criarMob(num, lvl)
        listaMobs.append(novoMob)


#esta função servira como um TAB para o usuário
#irá mostrar as informações dos mobs
def mostrarMobs():
    corVida=verd
    print("\n------------------------------------------------------------")
    for mob in listaMobs:

        #quando a vida do mob chega na metade ela fica amarela e quando chega na metade da metade fica
        if mob['hp']<=mob['hpMax']/2:
            if mob['hp']<=(mob['hpMax']/2)/2:
                corVida=verm
            else:
                corVida=amar
        else:
            corVida=verd

        #vo aproveitar um bug que ta dando para dar mais uma caracteristica ao meu jogo
        #remove o mob derrotado
        if mob['hp']<=0:
            listaMobs.remove(mob)
            os.system('cls')
            mostrarMobs()
            mob['hp']="DERROTADO"
            mob['hpMax']=""

        #mostra os mobs
        print(f"| Nome: {verm}{mob['nome']}{res} || Level: {mob['level']} || Dano: {mob['dano']} || HP: {corVida}{mob['hp']}{res} / {verd}{mob['hpMax']}{res} |\n------------------------------------------------------------")


#atacar o mob
def atacarMob(mob):
    mob['hp'] -= player['dano']
#atacar o player
def atacarPlayer(mob):
    player['hp'] -= mob['dano']


#a inteface do player
def hud():
    #quando a vida do player chega na metade ela fica amarela e quando chega na metade da metade fica
    if player['hp']<=player['hpMax']/2:
        if player['hp']<=(player['hpMax']/2)/2:
            corVida=verm
        else:
            corVida=amar
    else:
        corVida=verd
    print("------------------------------------------------------------")
    print(f" /-----\ \n | <*> | \n | /|\ |  Player HP: {corVida}{player['hp']}{res} / {player['hpMax']}  \n | / \ | \n \-----/")
    print("------------------------------------------------------------\n")


#acabei de lembra isso só vai da certo depois de fazer os mobs atacar
#hud de eventos, mostra as ações realizadas nos ultimos 2 turnos e, armazena todas as ações em uma ultra lista 
def eventos():
    print("a")


#batalha
def batalha():
    mobvivo=False
    for i in listaMobs:
        if i['hp']>0:
            mobvivo=True

    while player['hp']>0 and mobvivo==True:
        hud()
        while True:
            try:
                mob=int(input("Escolha qual mob atacar : "))-1
                selecionarMob = listaMobs[mob]
            except:
                os.system('cls')
                mostrarMobs()
                hud()
                continue
            else:
                break

        atacarMob(selecionarMob)
        os.system('cls')
        mostrarMobs()
        atacarPlayer(selecionarMob)
        mobvivo=0
        mobvivo=False
        for i in listaMobs:
            if i['hp']>0:
                mobvivo=True
        

#tela de vitória e scoore da wave
def win():
    hud()
    print("------------------------------------------------------------")
    print(f"{verd}Parabens você derrotou a wave{res}")
    print("------------------------------------------------------------\n")

#tela de derrota e scoore da wave
def lose():
    hud()
    print("-------------------------------------------------------------------------")
    print(f"{verm}Você pode ter perdido a batalha mas não guerra vá e conquiste sua vitória{res}")
    print("-------------------------------------------------------------------------\n")


#por enquanto será decidido manualmnet o level do player
#o código começa aqui
def inicio():
    os.system('cls')
    while True:
        print("----------------------------")
        print(f"       {verm}TERMINAL-GAME{res}     ")
        menuInicio()
        opc=input("             ")
        if opc == "1":
            while True:
                os.system('cls')
                lvl=player["level"]
                quant=int(lvl/10)
                gerarMobs(quant, lvl)
                mostrarMobs()
                batalha()
                os.system('cls')
                if player["hp"]>0:
                    win()
                    break
                else:
                    lose()
                    break
            listaMobs.clear()
        elif opc == "2":
            os.system('cls')
            print("(isso ainda não foi desenvovido, em breve estara pronto)")
        elif opc == "3":
            print("Saindo...")
            break
        else:
            os.system('cls')
            print(f"'{verm}{opc}{res}' é um código invalido")
            continue


#começa o código
inicio()