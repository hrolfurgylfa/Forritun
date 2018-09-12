'''
-----Verkefni-----
Hrólfur Gylfason
-----Dagsetning-----
'''
def saeti(heiltala):
    if heiltala == 1:
        return "Gull"
    elif heiltala == 2:
        return "Silfur"
    elif heiltala == 3:
        return "Brons"


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
        pass
        
    elif valmynd == "3":#Liður 3
        pass

    elif valmynd == "4":#Liður 4
        pass
        
    elif valmynd == "5":#Liður 5
        pass

    elif valmynd == "6":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 6" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 6")
