'''
Skilaverkefni 4 Skráarvinnsla
Hrólfur Gylfason
9/3/2018
'''
def buaTilListaSlettarTolur(byrja,enda):
    slettar_tolur_undir_1000 = []

    for tala in range(1,1001):
        if tala % 2 == 0:
            slettar_tolur_undir_1000.append(tala)

    return slettar_tolur_undir_1000

def buaTilSkraUrLista(skraarnafn,listi):
    strengur = ""

    skra = open(str(skraarnafn)+".txt","w")
    for tala in listi:
        strengur += str(tala)+"|"

    skra.write(strengur)
    skra.close()

def lesaSkraEinLinaTolur(skraarnafn):
    skra = open(str(skraarnafn)+".txt","r")

    for line in skra:
        lina = line.split("|")

    tolu_listi = lina
    tolu_listi.pop()
    tolu_listi = list(map(int,tolu_listi))

    return tolu_listi

def medaltalLista(listi):
    return sum(listi)/len(listi)

valmynd = ""

while valmynd != "5":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að fá dæmi 4")
    print("Ýttu á 5 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        buaTilSkraUrLista("Slettartolur",buaTilListaSlettarTolur(1,1001))

        slettar_tolur_listi = lesaSkraEinLinaTolur("Slettartolur")

        print("A. Prennta út allan listann:")
        print(slettar_tolur_listi)
        print()

        print("B. Meðaltal listans með tveimur aukastöfum:")
        print(medaltalLista(slettar_tolur_listi))
        print()

        print("C. Prennta út listann með tölum sem ganga upp í átta:")
        ganga_uppi_8 = 

    elif valmynd == "2":#Liður 2
        pass
        
    elif valmynd == "3":#Liður 3
        pass

    elif valmynd == "4":#Liður 4
        pass

    elif valmynd == "5":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 5" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 5")
