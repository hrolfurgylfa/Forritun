'''
Tímaverkefni 2
Hrólfur Gylfason
2/11/2018
'''
import random

def tolur(*args):
    return list(filter(lambda x: x % 5 == 0, args))

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
        print(tolur(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20))

    elif valmynd == "2":#Liður 2
        listi1 = ["Konni", "Sigga", "Snorri"]
        listi2 = ["fótbolta", "handbolta", "blaki"]

        listi3 = [nafn+" er í "+random.choice(listi2) for nafn in listi1]
        print(listi3)
        
    elif valmynd == "3":#Liður 3
        pass

    elif valmynd == "4":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 4")
