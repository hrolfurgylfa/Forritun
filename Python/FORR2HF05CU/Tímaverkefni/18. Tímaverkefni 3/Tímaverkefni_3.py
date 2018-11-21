'''
Tímaverkefni 3
Hrólfur Gylfason
21/11/2018
'''
def sununingsSamlagning(tala1, tala2):
    for tala in [tala1, tala2]:
        tala = str(tala)
        tala = int(tala[::-1])
    summa = tala1 + tala2
    return summa

def gangaUppI5(listi):
    skila_listi = list(filter(lambda x: x > 350 and x % 5 == 0, listi))
    return skila_listi

def setjaI3Veldi(*tolur):
    skila_listi = [x**3 for x in tolur]

    tel = 0
    for hlutur in skila_listi:
        if tel + 1 != len(skila_listi):
            print(hlutur,end=", ")
            tel += 1
        else:
            print(hlutur)


valmynd = ""

while valmynd != "4":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        print(sununingsSamlagning(12, 31))

    elif valmynd == "2":#Liður 2
        listi = [385, 230, 343, 580]
        print(gangaUppI5(listi))
        
    elif valmynd == "3":#Liður 3
        setjaI3Veldi(1, 2, 3, 4, 5, 6, 7, 8, 9)

    elif valmynd == "4":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 4")
