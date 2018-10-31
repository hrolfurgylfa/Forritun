'''
Æfingarverkefni 7 recursion
Hrólfur Gylfason
31/10/2018
'''
def finnaHeildarsummu(tala, summa = 0):
    if tala > 0:
        summa += tala
        return finnaHeildarsummu(tala-1, summa)
    else:
        return summa

def finnaHeildarsummuOdda(tala, summa = 0):
    if tala > 0 and tala % 2 == 1:
        summa += tala
        return finnaHeildarsummuOdda(tala-1, summa)
    elif tala > 0 and tala % 2 == 0:
        return finnaHeildarsummuOdda(tala-1, summa)
    else:
        return summa

valmynd = ""

while valmynd != "3":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        print("Úr return:",finnaHeildarsummu(7))

    elif valmynd == "2":#Liður 2
        tala = 24
        heildarsumma = finnaHeildarsummuOdda(tala)
        print("Heildarsumma oddatalna niður og með "+str(tala)+":",heildarsumma)

    elif valmynd == "3":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 3" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 3")
