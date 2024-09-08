import os
mensagem=[]
nome=input("\nNome: ")

while True:
    #limpando o terminal
    os.system('cls')
    if len(mensagem)>0:
        for m in mensagem:
            print(m['nome'], "-", m['texto'])
    print("________________________________")

    #obtendo texto
    texto=input("mensagem: ")
    if texto == "fim":
        break

    #adiciona uma mensagem na lista
    mensagem.append({
        "nome": nome,
        "texto": texto
    })