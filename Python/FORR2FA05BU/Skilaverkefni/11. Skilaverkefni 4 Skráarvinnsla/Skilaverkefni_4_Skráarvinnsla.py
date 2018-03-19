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

    skra = open(skraarnafn,"w")
    for tala in listi:
        strengur += str(tala)+"|"

    skra.write(strengur)
    skra.close()

def lesaSkraEinLinaTolur(skraarnafn):
    skra = open(skraarnafn,"r")

    for line in skra:
        lina = line.split("|")

    tolu_listi = lina
    tolu_listi.pop()
    tolu_listi = list(map(int,tolu_listi))

    return tolu_listi

def medaltalLista(listi):
    return sum(listi)/len(listi)

def gangaUppI8(listi):
    gangaUppI8_listi = []

    for tala in listi:
        if tala % 8 == 0:
            gangaUppI8_listi.append(tala)

    return gangaUppI8_listi

def skraarPrentari(skraarnafn):
    skra = open(skraarnafn,"r")
    skraar_listi = []
    tel = 0

    for line in skra:
        lina = line.split("|")
        lina.pop()
        for hlutur in lina:
            skraar_listi.append(hlutur)

    for hlutur in skraar_listi:
        tel += 1
        if tel == 11:
            print("\n")
            tel = 1
        print(hlutur,end=" ")
    print()

def frumToluLeitari(byrjun,endir):
    frum_tolu_listi = []

    for tala in range(byrjun,endir + 1):
        if tala > 1:
            for tala2 in range(2,tala):
                if tala % tala2 == 0:
                    break
            else:
                frum_tolu_listi.append(tala)
    return frum_tolu_listi

def listaPrentari(listi):
    teljari = 0
    for hlutur in listi:
        teljari += 1
        if teljari == len(listi):
            print(hlutur)
        else:
            print(hlutur,end=", ")

def sjouPrentari_int(listi):
    listi = list(map(str,listi))

    for hlutur in listi:
        if "7" in hlutur:
            print(hlutur,end=" ")
    print()

def fjordaHver(listi):
    fjorda_hver_listi = []
    tel = 0

    for hlutur in listi:
        tel += 1
        if tel == 4:
            fjorda_hver_listi.append(hlutur)
            tel = 0

    return fjorda_hver_listi

def nyTuple():
    return ("123456","password","12345678","qwerty","12345","123456789","letmein","1234567","football","iloveyou")

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
        buaTilSkraUrLista("Slettartolur.txt",buaTilListaSlettarTolur(1,1001))

        slettar_tolur_listi = lesaSkraEinLinaTolur("Slettartolur.txt")

        print("A. Prennta út allan listann:")
        print(slettar_tolur_listi)
        print()

        print("B. Meðaltal listans með tveimur aukastöfum:")
        print(round(medaltalLista(slettar_tolur_listi),2))
        print()

        print("C. Prennta út listann með tölum sem ganga upp í átta:")
        ganga_upp_i_8 = gangaUppI8(slettar_tolur_listi)
        print(ganga_upp_i_8)
        print()

        print("D. Listi úr C skrifaður í skjal")
        buaTilSkraUrLista("sumarslettartolur.txt",ganga_upp_i_8)
        print()

        print("E. Prenta út skránna með bil milli talnana og 10 tölum í línu")
        skraarPrentari("sumarslettartolur.txt")

    elif valmynd == "2":#Liður 2
        buaTilSkraUrLista("frumtolur.txt",frumToluLeitari(1,100))

        print("A. Lesa skránna og skila lista")
        frumtolur = lesaSkraEinLinaTolur("frumtolur.txt")
        print()

        print("B. Prenta út listann")
        listaPrentari(frumtolur)
        print()

        print("C. Prennta út allar tölurnar sem eru með 7 í þeim")
        sjouPrentari_int(frumtolur)
        print()

        print("D. Taka listann úr A, prennta út fjórðu hverja tölu og setja svo inn í aðra skrá")
        fjordaHverFrumtala_listi = fjordaHver(frumtolur)
        listaPrentari(fjordaHverFrumtala_listi)
        buaTilSkraUrLista("fjordaHverFrumtala.txt",fjordaHverFrumtala_listi)
        print()

        print("E. Prenta út skránna í D")
        skraarPrentari("fjordaHverFrumtala.txt")
        print()
        
    elif valmynd == "3":#Liður 3
        tuple_1 = (1,2,3,4,5,6,7,8,9)
        tuple_2 = ("a","b","c","d","e","f","g","h")
        tuple_3 = ("konni",123,"sponni",234)

        print("A. Prenta út tuplein")
        listaPrentari(tuple_1)
        listaPrentari(tuple_2)
        listaPrentari(tuple_3)
        print()

        print("B. Bæta við nýrri tuple að eigin vali")
        tuple_4 = nyTuple()
        print(tuple_4)
        print()

        print("C. Finna meðaltal fyrstu tuplunar")
        print(medaltalLista(tuple_1))

    elif valmynd == "4":#Liður 4
        print("GIT test")#TEST
        TEST = "TEST"

    elif valmynd == "5":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 5" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 5")
