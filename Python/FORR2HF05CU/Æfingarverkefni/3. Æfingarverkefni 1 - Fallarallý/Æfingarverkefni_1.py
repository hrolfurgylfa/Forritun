'''
-----Verkefni-----
Hrólfur Gylfason
-----Dagsetning-----
'''
import math

def saeti(heiltala):
    if heiltala == 1:
        return "Gull, þú lentir í fyrsta sæti, til hamingju!!!"
    elif heiltala == 2:
        return "Silfur, þú lentir í öðru sæti, til hamingju!!!"
    elif heiltala == 3:
        return "Brons, þú lentir í þriðja sæti, til hamingju!!!"
    else:
        return "Þú fékst hvorki gull, silfur né brons 😞"

def kynjaskinjari(kyn):
    if kyn.lower() == "kk":
        return "Þú ert karlmaður"
    elif kyn.lower() == "kvk":
        return "Þú ert kvennmaður"
    else:
        utskyring = input("Hvað þýðir "+str(kyn)+"?\n--->")
        print()

        return utskyring

def radiusUrUmmali(ummal):
    radius = ummal / (2 * math.pi)
    return radius

def flatarmalUrRadius(radius):
    flatarmal = math.pi * (radius ** 2)
    return flatarmal


valmynd = ""

while valmynd != "6":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að fá dæmi 4")
    print("Ýttu á 5 til þess að fá dæmi 5")
    print("Ýttu á 6 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        tala = int(input("Sláðu inn 1, 2 eða 3\n--->"))
        print()

        print(saeti(tala))

    elif valmynd == "2":#Liður 2
        kyn = input("Sláðu inn kyn\n--->")
        print()

        kyn_notenda = kynjaskinjari(kyn)

        if kyn_notenda != "Þú ert karlmaður" and kyn_notenda != "Þú ert kvennmaður":
            print(kyn_notenda.upper())

        else:
            print(kyn_notenda)
        
    elif valmynd == "3":#Liður 3
        ummal = int(input("Sláðu inn ummál hrings\n--->"))
        print()
        
        radius = radiusUrUmmali(ummal)
        flatarmal = flatarmalUrRadius(radius)

        print("Flatarmál hringsins er",flatarmal)

    elif valmynd == "4":#Liður 4
        pass
        
    elif valmynd == "5":#Liður 5
        pass

    elif valmynd == "6":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 6" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 6")
