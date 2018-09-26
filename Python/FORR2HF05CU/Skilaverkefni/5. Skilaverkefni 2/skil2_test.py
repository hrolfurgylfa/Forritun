'''
Skilaverkefni 2
Hrólfur Gylfason
26/9/2018
'''
import sys
from skil2_foll import *

valmynd = ""

while valmynd != "7":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að fá dæmi 4")
    print("Ýttu á 5 til þess að fá dæmi 5")
    print("Ýttu á 6 til þess að fá dæmi 6")
    print("Ýttu á 7 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        print("Þetta forrit hjálpar við það að reikna langhlið á rétthyrndum þríhyrningi")
        print("Sláðu inn mínustölu til þess að hætta\n")
        while True:
            try:
                print("----------")
                a = float(input("a = "))
                if a < 0:
                    raise Exception("Bless")
                b = float(input("b = "))
                if a < 0:
                    raise Exception("Bless")

                c = langhlid(a, b)
                print("\nc =",round(c,3))
            
            except ValueError:
                print("vinsamlegast sláðu inn tölu")

            except Exception as error:
                print(error)
                break

    elif valmynd == "2":#Liður 2
        print("Þetta forrit finnur út hvort að tala 2 sé margfeldi af tölu 1")
        print("Sláðu inn 0 í tölu 1 til þess að hætta\n")
        while True:
            try:
                print("----------")
                tala1 = int(input("Tala 1 = "))
                if tala1 == 0:
                    raise Exception("Bless")
                tala2 = int(input("Tala 2 = "))
                if tala2 == 0:
                    raise Exception("Bless")

                svar = margfeldi_af(tala1, tala2)
                print()
                if svar is True:
                    print(tala2,"er margfeldi af",tala1)
                else:
                    print(tala2,"er ekki margfeldi af",tala1)
            
            except ValueError:
                print("vinsamlegast sláðu inn heiltölu")

            except Exception as error:
                print(error)
                break
        
    elif valmynd == "3":#Liður 3
        while True:
            print("\n---------------")
            try:
                staerd_kassa = int(input("Sláðu inn stærð kassa\n--->"))
                break
            except ValueError:
                print("Vinsamlegast sláðu inn heiltölu")
        ferningur_ur_stjornum(staerd_kassa)

    elif valmynd == "4":#Liður 4
        print("Þetta forrit finnur út hvort að talan sé slétt eða odda tala")
        print("Sláðu inn 0 til þess að hætta\n")
        while True:
            print("\n---------------")
            try:
                tala = int(input("Sláðu inn heiltölu\n--->"))
                break
            except ValueError:
                print("Vinsamlegast sláðu inn heiltölu")

        svar = er_slett_tala(tala)

        print()
        if svar is True:
            print(tala,"er slétt tala")
        else:
            print(tala,"er odda tala")
        
    elif valmynd == "5":#Liður 5
        print("Þetta forrit hjálpar við það að reikna flatarmál á hring")
        print("Sláðu inn mínustölu til þess að hætta\n")
        while True:
            try:
                print("----------")
                radius = float(input("Sláðu inn radíus\n--->"))
                if radius < 0:
                    raise Exception("Bless")

                flatarmal = flatramal_hrings(radius)
                print("\nflatarmal =",round(flatarmal,2))
            
            except ValueError:
                print("vinsamlegast sláðu inn tölu")

            except Exception as error:
                print(error)
                break

    elif valmynd == "6":#Liður 6
        pass

    elif valmynd == "7":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 7" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 7")
