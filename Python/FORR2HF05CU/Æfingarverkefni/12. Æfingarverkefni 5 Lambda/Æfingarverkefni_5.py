'''
Æfingarverkefni 5 Lambda
Hrólfur Gylfason
26/10/2018
'''
import random

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
        random_tolu_listi = []
        for tel in range(50):
            random_tolu_listi.append(random.randint(-20, 20))
        
        absoloute_random_tolur = list(map((lambda x: -x if x < 0 else x),random_tolu_listi))

        print(absoloute_random_tolur)

    elif valmynd == "2":#Liður 2
        farToCel = lambda x: (x - 32) * (5/9)
        farenheitListi = []

        for tel in range(50):
            farenheitListi.append(random.randint(20, 70))
            
        celsiusListi = list(map(farToCel,farenheitListi))

        celsiusListi2 = []
        for tala in celsiusListi:
            tala = round(tala,2)
            celsiusListi2.append(tala)

        print(celsiusListi2)
        
    elif valmynd == "3":#Liður 3
        avaxta_listi = ["Mandarína","Epli","Appelsína","Klementína","Kiwi","Mango","Sítróna","Pera","Ananas","Plóma"]

        minna_en_fimm_stafir = list(filter((lambda x: len(x) <= 5),avaxta_listi))

        print(minna_en_fimm_stafir)

    elif valmynd == "4":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 4")
