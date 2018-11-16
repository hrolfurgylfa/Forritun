'''
Skilaverkefni 5 - Lambda, þappaðir listar og endurkvæmni
Hrólfur Gylfason
9/11/2018
'''
import random

def faHeiltolu(magn, texti):# Þetta fall tekur inn magn talna sem notandinn þarf að slá inn og textanum sem notandinn sér og fær notandann svo til þess að slá tölurnar inn og skilar þeim í lista
    if magn < 1:
        return []
    else:
        listi = []
        for tel in range(magn):
            while True:
                try:
                    tala = int(input(texti))
                    listi.append(tala)
                    break
                except ValueError:
                    print("Vinsamlegast sláðu inn heiltölu")
        return listi

#Liður 1
def randomTolur(tala, byrja, enda):# Þetta fall skilar lista með random tölur á bilinu byrja og enda og jafn mörgum og tala segir til um
    listi = []
    for tel in range(tala):
        random_tala = random.randint(byrja, enda)
        listi.append(random_tala)
    return listi
def finnaSummu(talaNot,listi):# Þetta fall tékar hvort að talaNot gangi uppí tölurnar í listanum og bætir öllum tölunum sem talaNot gengur uppí við breytuna summa
    summa = 0
    for tala in listi:
        if tala % talaNot == 0:
            summa += tala
    return summa
def hverVann(summaNot, summaTol):# Þetta tékkar hvor talan sé hærri og skilar texta sem passar við það
    if summaNot > summaTol:
        return "Þú vannst tölvuna!!! Til hamingju!!!"
    if summaNot < summaTol:
        return "Þú tapaðir \U0001F641"
    else:
        return "Jafntefli"

#Liður 7
def margfaldaListaSaman(listi, summa = 0, tel = 0):# Þetta fall keyrir þangað til len() af listanum sem kom inn í byrjun er jafnt tel og þá eru öll stökin í listanum búin að fara í gegn um fallið og vera margfölduð með summa
    if len(listi) == tel:
        return summa
    else:
        if summa != 0:
            summa *= listi[tel]
        else:
            summa += listi[tel]
        tel += 1
        return margfaldaListaSaman(listi, summa, tel)

#Liður 8
def skilaListaIBitum(listi):# Prentar út einn hlut úr listanum sem kom inn þegar það er notað next() á fallið
    for hlutur in listi:
        print(hlutur)
        yield hlutur


valmynd = ""

while valmynd != "9":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að fá dæmi 4")
    print("Ýttu á 5 til þess að fá dæmi 5")
    print("Ýttu á 6 til þess að fá dæmi 6")
    print("Ýttu á 7 til þess að fá dæmi 7")
    print("Ýttu á 8 til þess að fá dæmi 8")
    print("Ýttu á 9 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        spilaAftur = "j"
        while spilaAftur.lower() == "j":#Þetta gerist á meðan maður segir j þegar maður er spurður hvort að hann vilji spila aftur
            random_tolur = randomTolur(20, 2, 100)

            tala_notenda = 0
            while tala_notenda > 10 or tala_notenda < 1:# Þetta er til þess að það sé spurt um tölu þangað til að það kemur tala sem virkar
                tala_notenda = faHeiltolu(1, "Sláðu inn heiltölu á milli 1 og 10\n--->")
                tala_notenda = tala_notenda[0]#Þetta er vegna þess að fallið faHeiltolu skilar lista með tölunum
            tala_tolvu = random.randint(1,10)

            summa_notanda = finnaSummu(tala_notenda, random_tolur)
            summa_tolvu = finnaSummu(tala_tolvu, random_tolur)

            print()
            print(summa_notanda)
            print(summa_tolvu)
            print()

            sigurtexti = hverVann(summa_notanda, summa_tolvu)
            print(sigurtexti)

            spilaAftur = input("\nViltu spila aftur? J/N\n--->")
            if spilaAftur.lower() == "j":#Prentar bara línu til þess að skilja að skiptin sem er spilað
                print("----------------------------------------")

    elif valmynd == "2":#Liður 2
        random_tolur = randomTolur(100, 200, 600)
        nyr_listi = list(filter(lambda x: x % 2 == 0, random_tolur))

        print(nyr_listi)
        
    elif valmynd == "3":#Liður 3
        random_tolur = randomTolur(20, 2, 100)
        listi2 = list(filter(lambda x: x % 5 == 0 and x > 350, random_tolur))

        print(listi2)

    elif valmynd == "4":#Liður 4
        random_tolur = randomTolur(200, 100, 900)
        listi2 = list(map(lambda x: x - 2, random_tolur))

        print(listi2)
        
    elif valmynd == "5":#Liður 5
        random_tolur = randomTolur(200, 1, 90)
        undir_6 = [x**3 for x in random_tolur if x < 6]

        print(undir_6)

    elif valmynd == "6":#Liður 6
        random_tolur = randomTolur(100, 1, 20)
        endar_a_0 = [x for x in random_tolur if str(x)[-1] == "0"]

        print(endar_a_0)

    elif valmynd == "7":#Liður 7
        random_tolur = randomTolur(5, 1, 20)
        print(random_tolur)
        summa = margfaldaListaSaman(random_tolur)

        print(random_tolur)
        print(summa)

    elif valmynd == "8":#Liður 8
        random_tolur = randomTolur(100, 50, 150)
        hlutur = skilaListaIBitum(random_tolur)
        for tel in range(100):
            next(hlutur)

    elif valmynd == "9":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 9" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 9")
