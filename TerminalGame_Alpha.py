with open("teste.txt","r",encoding="utf-8") as arquivo:
        nomeSalario=arquivo.readlines()

quem=input("Quem deseja procurar : ")
for linha in nomeSalario:
        if quem in linha:
            print(linha)

