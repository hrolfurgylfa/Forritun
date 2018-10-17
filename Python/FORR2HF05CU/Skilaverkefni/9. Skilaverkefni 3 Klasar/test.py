#!!!Til þess að uppfæra lagerhlutir.csv í text editor þarf að endurræsa forritið til þess að það taki eftir breytingunum eða fara í lið 1!!!
'''
Skilaverkefni 3 Klasar
Hrólfur Gylfason
8/10/2016
'''
import sys, csv
from minir_klasar import Lagerhlutur

def opnaSkra():#Þetta fall á að opna skrána lagerhlutir.csv. Lesa skrána.Því næst býr fallið til tilvik(object,hlut) úr hverri línu skráarinnar og setur í lista. Listinn innheldur þá hluti sem gerðir eru úr klasanum Lagerhlutur.
    with open("lagerhlutir.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter = ";")
        
        lagerhlutir = []

        for row in reader:
            hlutur = Lagerhlutur(row[0], row[1], row[2], row[3])
            lagerhlutir.append(hlutur)

    return lagerhlutir

def skrifaSkra(lagerhlutir):# Skrifar í skrána.
    skra = open("lagerhlutir.csv", "w")
    for lina in lagerhlutir:
        skra.write(str(lina.numer)+";"+str(lina.tegund)+";"+str(lina.fjoldi)+";"+str(lina.verd)+"\n")
    skra.close()

def nyrLagerhlutur(lagerhlutir, numer, tegund, fjoldi, verd):# bætir inn nýju tilviki(object,hluti)
    hlutur = Lagerhlutur(numer, tegund, fjoldi, verd)
    lagerhlutir.append(hlutur)

    return lagerhlutir

def eydaLagerhlut(lagerhlutir, numer):# eyðir tilviki(object,hluti)
    lagerhlutir2 = []
    for hlutur in lagerhlutir:
        if hlutur.numer != numer:
            lagerhlutir2.append(hlutur)

    return lagerhlutir2

def breytaLagerhlut(lagerhlutir, numer, tegund, fjoldi, verd):# breytir tilviki(object,hluti)
    lagerhlutir2 = []
    for hlutur in lagerhlutir:
        if hlutur.numer == numer:
            hlutur2 = Lagerhlutur(numer, tegund, fjoldi, verd)
            lagerhlutir2.append(hlutur2)
        else:
            lagerhlutir2.append(hlutur)

    return lagerhlutir2

def prentaLager(lagerhlutir):# skrifar á skjáinn allt sem er í skránni(innhald listans af tilvikum)
    for hlutur in lagerhlutir:
        print("Númer:",hlutur.numer)
        print("Númer:",hlutur.tegund)
        print("Fjöldi:",hlutur.fjoldi)
        print("Verð:",hlutur.verd)
        print()

def heildarverdHlutar(lagerhlutir):# skrifar á skjáinn heildarverð hverrar tegundar fyrir sig
    print("Heildarverð hluta:")
    for hlutur in lagerhlutir:
        hoppa_yfir = False
        try:
            hlutur_fjoldi = int(hlutur.fjoldi)
            hlutur_verd = int(hlutur.verd)
        except:
            print("Það verða að vera tölur í dálk þrjú og fjögur í lagerhlutir.csv")
            hoppa_yfir = True

        if hoppa_yfir is not True:
            hlutur_HVH = hlutur_fjoldi * hlutur_verd
            print(str(hlutur.tegund)+": "+str(hlutur_HVH))

def heildarverdLager(lagerhlutir):# skrifar á skjáinn heildarverð allra hluta á lager
    allirHlutir = 0
    for hlutur in lagerhlutir:
        try:
            hlutur.verd = int(hlutur.verd)
        except ValueError:
            print("Það verða að vera tölur í lagerhlutir.csv, fjórða dálk sem er verð")
        
        allirHlutir += hlutur.verd
    
    print("Verð allra hluta á lager:",allirHlutir)

def vorurKeyptar(lagerhlutir, numer, magn_hluta_keyptir):#Þetta fall tekur inn listann með vörunum, númer hvað hluturinn sem á að breyta er og magn hluta sem voru keyptir og svo skilar þetta tuple vegna þess að það þarf aldrei að breyta þessu með listanum af öllum klasa tilvikunum og False ef það virkaði en magn hluta sem var hægt að selja (að 0) ef það virkaði ekki
    numer = str(numer)
    try:
        magn_hluta_keyptir = int(magn_hluta_keyptir)
    except ValueError:
        print('"Magn hluta keyptir" er ekki heiltala\nABORTING')
        return (lagerhlutir, False)

    for hlutur in lagerhlutir:
        if hlutur.numer == numer:
            try:
                hlutur.fjoldi = int(hlutur.fjoldi)
            except ValueError:
                print('í lagerhlutir.csv verður þriðji dálkur að vera heiltala\nABORTING')
                break

            if hlutur.fjoldi >= magn_hluta_keyptir:
                hlutur.fjoldi -= magn_hluta_keyptir
            else:
                haegt_ad_kaupa = hlutur.fjoldi
                hlutur.fjoldi = 0
                return (lagerhlutir, haegt_ad_kaupa)

    return (lagerhlutir, False)


valmynd = ""

lager = opnaSkra()# Þetta er það sem opnar skrána í fyrsta sinn og setir hana í klasann

while valmynd != "10":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að prenta klasan")
    print("Ýttu á 2 til þess að skrifa klasan í skrána")
    print("Ýttu á 3 til þess að bæta við nýrri vöru á lager")
    print("Ýttu á 4 til þess að eyða vöru á lager")
    print("Ýttu á 5 til þess að breyta vöru á lager")
    print("Ýttu á 6 til þess að prenta allar vörur á lager")
    print("Ýttu á 7 til þess að prenta heildarverð allra vara á lager")
    print("Ýttu á 8 til þess að prenta verð allra vara á lager lagt saman")
    print("Ýttu á 9 til þess að kaupa vörur")
    print("Ýttu á 10 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        lager = opnaSkra()
        print(lager)

    elif valmynd == "2":#Liður 2
        skrifaSkra(lager)
        
    elif valmynd == "3":#Liður 3
        print("Bæta við nýrri vöru á lager")

        tala1 = input("Númer\n---> ")
        tala2 = input("\nTegund\n---> ")
        tala3 = input("\nFjöldi\n---> ")
        tala4 = input("\nVerð\n---> ")

        lager = nyrLagerhlutur(lager, tala1, tala2, tala3, tala4)
        skrifaSkra(lager)

    elif valmynd == "4":#Liður 4
        print("Eyða vöru á lager")

        tala = input("Númer\n---> ")

        lager = eydaLagerhlut(lager, tala)
        skrifaSkra(lager)
        
    elif valmynd == "5":#Liður 5
        print("Breyta vöru á lager")

        tala1 = input("Númer\n---> ")
        tala2 = input("\nTegund\n---> ")
        tala3 = input("\nFjöldi\n---> ")
        tala4 = input("\nVerð\n---> ")

        lager = breytaLagerhlut(lager, tala1, tala2, tala3, tala4)
        skrifaSkra(lager)

    elif valmynd == "6":#Liður 6
        prentaLager(lager)

    elif valmynd == "7":#Liður 7
        heildarverdHlutar(lager)

    elif valmynd == "8":#Liður 8
        heildarverdLager(lager)

    elif valmynd == "9":#Liður 9 (mittFall)
        print("Kaupa vörur\n")

        tala1 = input("Númer vöru\n---> ")
        tala2 = input("\nFjöldi hluta keyptir\n---> ")

        lager_tup = vorurKeyptar(lager, tala1, tala2)

        lager = lager_tup[0]
        skrifaSkra(lager)
        
        if lager_tup[1] is not False:# Þetta gerist ef það var ekki til nóg af hlutum til þess að selja
            print("Það var bara hægt að kaupa",lager_tup[1])

    elif valmynd == "10":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 10" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 10")
