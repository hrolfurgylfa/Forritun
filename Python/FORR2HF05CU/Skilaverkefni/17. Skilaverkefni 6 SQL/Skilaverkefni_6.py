'''
Skilaverkefni 6 MySQL
Hrólfur Gylfason
16/11/2018
'''
from skraning import Skraning

s = Skraning()
valmynd = ""

while valmynd != "8":

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
    print("Ýttu á 8 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        s.nyr_medlimur("Hrólfur")

    elif valmynd == "2":#Liður 2
        s.nyr_afangi("HRÓL1HF05AU")
        
    elif valmynd == "3":#Liður 3
        s.prenta("namskeid")

    elif valmynd == "4":#Liður 4
        afangar_nemanda = s.skradurIafanga("Konráð Guðmundsson")

        tel = 0
        for afangi in afangar_nemanda:
            tel += 1
            for a in afangi:
                key = a
            if tel <= len(afangar_nemanda) - 2:
                print(afangi[key],end=", ")
            elif tel == len(afangar_nemanda) - 1:
                print(afangi[key],end=" og ")
            else:
                print(afangi[key])
        
    elif valmynd == "5":#Liður 5
        s.skraning("Konráð Guðmundsson", "HRÓL1HF05AU")

    elif valmynd == "6":#Liður 6
        pass

    elif valmynd == "7":#Liður 7
        pass
        
    elif valmynd == "8":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 8" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 8")
