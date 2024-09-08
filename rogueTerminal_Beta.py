from random import randint
import os

listaNPCs=[]
player={
    "nome": "Lotus",
    "level":10,
    "exp":0,
    "expMax":100,
    "hp":100,
    "hpMax":100,
    "dano":100
}



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
    mobvivo=0
    for i in listaNPCs:
        if i['hp']>0:
            mobvivo+=1

    while player['hp']>0 and mobvivo>0:
        hud()
        mob=int(input("Escolha qual mob atacar : "))-1
        selecionarMob = listaNPCs[mob]
        atacarMob(selecionarMob)
        os.system('cls')
        mostrarMobs()
        mobvivo=0
        for i in listaNPCs:
            if i['hp']>0:
                mobvivo+=1
            else:
                mobvivo-=1
        

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
        else:
            lose()


inicio()