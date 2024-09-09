from random import randint
import os
#lista de Mobs, tá npc pq é muita coisa pra muda, depois eu mudo isso para listaMOBs
listaNPCs=[]

#player
player={
    "nome": "Lotus",
    "level":10,
    "exp":0,
    "expMax":100,
    "hp":100,
    "hpMax":100,
    "dano":100
}

#menu principal
menuIniciar=[
    "1. Iniciar batalha",
    "2. Editar personagem",
    "3. Sair"
]

#mene de pause
menuPause=[
    "1. Voltar a batalha",
    "2. Reiniciar batalha",
    "3. Voltar ao menu incial",
    "4. Sair do jogo"
]

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


#gera uma quantidade de mobs e adiciona os na lista de NPCs
#a quantidade de mobs depende do level do player
#por enquanto sera decidido manualmente
def gerarMobs(quant, lvl):
    num=0
    for i in range(quant):
        num+=1
        novoMob = criarMob(num, lvl)
        listaNPCs.append(novoMob)


#esta função servira como um TAB para o usuário
#irá mostrar as informações dos mobs
def mostrarMobs():
    print("\n------------------------------------------------------------")
    for npc in listaNPCs:
        print(f"| Nome: {npc['nome']} || Level: {npc['level']} || Dano: {npc['dano']} || HP: {npc['hp']} / {npc['hpMax']} |\n------------------------------------------------------------")


#atacar o mob
def atacarMob(mob):
    mob['hp'] -= player['dano']
#atacar o player
def atacarPlayer(mob):
    player['hp'] -= mob['dano']


#a inteface do player
def hud():
    print("------------------------------------------------------------")
    print(f" /-----\ \n | <*> | \n | /|\ |  Player HP: {player['hp']} / {player['hpMax']}  \n | / \ | \n \-----/")
    print("------------------------------------------------------------\n")

#batalha
def batalha():
    mobvivo=False
    for i in listaNPCs:
        if i['hp']>0:
            mobvivo=True

    while player['hp']>0 and mobvivo==True:
        hud()
        while True:
            try:
                mob=int(input("Escolha qual mob atacar : "))-1
                selecionarMob = listaNPCs[mob]
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
        mobvivo=0
        mobvivo=False
        for i in listaNPCs:
            if i['hp']>0:
                mobvivo=True
        

#tela de vitória e scoore da wave
def win():
    hud()
    print("------------------------------------------------------------")
    print("Parabens você derrotou a wave")
    print("------------------------------------------------------------\n")

#tela de derrota e scoore da wave
def lose():
    hud()
    print("-------------------------------------------------------------------------")
    print("Você pode ter perdido a batalha mas não guerra vá e conquiste sua vitória")
    print("-------------------------------------------------------------------------\n")


#por enquanto será decidido manualmnet o level do player
#o código começa aqui
def inicio():
    os.system('cls')
    while True:
        print("----------------------------")
        print("       TERMINAL-GAME     ")
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
            listaNPCs.clear()
        elif opc == "2":
            os.system('cls')
            print("(isso ainda não foi desenvovido, em breve estara pronto)")
        elif opc == "3":
            print("Saindo...")
            break
        else:
            os.system('cls')
            print(f"'{opc}' é um código invalido")
            continue


#começa o código
inicio()