'''
Skilaverkefni 4 klasatré
Hrólfur Gylfason
24/10/2018
'''
from Skilaverkefni_4_klasar import *


valmynd = ""

#Hérna bý ég til öll tilvik klasana til þess að geta notað tilvikin í nokkrum mismunandi liðum
tilvik1 = Nemi(2109013290, "Hrólfur", "kk", "Holtagerði 7", 6155549, "hrolfurgylfa@protonmail.com")
tilvik2 = Grunnskolanemi(2109013290, "Hrólfur", "kk", "Holtagerði 7", 6155549, "hrolfurgylfa@protonmail.com", "Gylfi", "Kársnesskóli")
tilvik3 = Framhaldsskolanemi(2109013290, "Hrólfur", "kk", "Holtagerði 7", 6155549, "hrolfurgylfa@protonmail.com", "Forritun")
tilvik4 = Haskolanemi(2109013290, "Hrólfur", "kk", "Holtagerði 7", 6155549, "hrolfurgylfa@protonmail.com", 3, 1450000)

while valmynd != "3":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá __str__ föll")
    print("Ýttu á 2 til þess að fá get og set föll")
    print("Ýttu á 3 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#__str__ föll
        print("Nemi:")
        print(tilvik1)
        print()#Enter

        print("Grunnskólanemi:")
        print(tilvik2)
        print()#Enter

        print("Framhaldsskóli:")
        print(tilvik3)
        print()#Enter

        print("Háskóli:")
        print(tilvik4)

    elif valmynd == "2":#get og set föll
        tilvik1.netfang_set("hrolfurgylfa@hrolfurgylfa.is")
        print("Nemi netfang:",tilvik1.netfang_get())

        tilvik2.forradamadur_set("Helga")
        print("Grunnskoli forráðamaður:",tilvik2.forradamadur_get())

        tilvik3.brautarheiti_set("Nát")
        print("Framhaldsskólanemi brautarheiti:",tilvik3.brautarheiti_get())

        tilvik4.namslan_set("Nei")
        print("Háskóli námslán:",tilvik4.namslan_get())

    elif valmynd == "3":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 3" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 3")