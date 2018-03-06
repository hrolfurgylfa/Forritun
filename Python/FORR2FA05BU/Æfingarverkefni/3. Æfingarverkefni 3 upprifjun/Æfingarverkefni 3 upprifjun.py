'''
Æfingarverkefni 3 upprifjun
Hrólfur Gylfason
19/1/2018
'''
valmynd = ""

while valmynd != "8":

    for tel in range(50):
        print("-",end="")
    print("\n")

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að fá dæmi 4")
    print("Ýttu á 5 til þess að fá dæmi 5")
    print("Ýttu á 6 til þess að fá dæmi 6")
    print("Ýttu á 7 til þess að fá dæmi 7")
    print("Ýttu á 8 til þess að hætta")
    valmynd = input("-------------------->>> ")

    print()
    for tel in range(50):
        print("-",end="")
    print()

    if valmynd == "1":
        listi = []

        tala_1 = input("Sláðu inn tölu 1 ")
        tala_2 = input("Sláðu inn tölu 2 ")
        tala_3 = input("Sláðu inn tölu 3 ")

        print()

        listi.append(tala_1)
        listi.append(tala_2)
        listi.append(tala_3)

        if tala_1 == tala_2 and tala_2 == tala_3:
            print("Allar tölurnar eru jafn stórar")

        else:
            print(str(min(listi))+", "+str(max(listi)))

    elif valmynd == "2":
        import datetime
        nuna = datetime.datetime.now()

        aldur = int(input("Hversu gamall ert þú? "))

        print()

        print("Þú verður",2100 - (nuna.year - aldur)+1,"ára næstu áramót ef þú hefur átt afmæli í ár")

    elif valmynd == "3":
        allar_tolur = []
        tala = ""

        while tala != 0:
            tala = int(input("Sláðu inn tölu "))
            if tala != 0:
                allar_tolur.append(tala)
            else:
                pass

        print()

        medaltal = sum(allar_tolur)/len(allar_tolur)
        print("Summa talnanna sem voru slegnar inn er",sum(allar_tolur))
        print("Fjöldi talnanna sem voru slegnar inn er",len(allar_tolur))
        print("Meðaltal talnanna sem voru slegnar inn er",round(medaltal,3))

    elif valmynd == "4":
        radius = float(input("Sláðu inn radíus kúlu "))

        rummal = (4*(radius*radius*radius)*3.14159)/3
        flatarmal = 4*3.14159*(radius*radius)

        print()

        print("Rúmmál kúlunnar er",round(rummal,3))
        print("Yfirborðsflatarmál kúlunnar er",round(flatarmal,3))
        
    elif valmynd == "5":
        lykilord = input("Sláðu inn lykilorð ")

        fjoldi_bokstafa = 0
        fjoldi_numera = 0

        for stafur in lykilord:
            if stafur.isalpha():
                fjoldi_bokstafa += 1

            elif stafur.isdigit():
                fjoldi_numera += 1

            else:
                pass

        print()

        if len(lykilord) >= 6:
            if fjoldi_bokstafa != 0:
                if fjoldi_numera != 0:
                    pass
                else:
                    print("Lykilorðið þarf að hava allavegana einn tölustaf")
            else:
                print("Lykilorðið þarf að hafa allavegana einn bókstaf")
        else:
            print("Lykilorðið þarf að vera sex stafir eða lengra")

    elif valmynd == "6":
        texti = input("Sláðu inn texta ")

        ha_stafir = 0
        la_stafir = 0

        for stafur in texti:
            if stafur.isupper():
                ha_stafir += 1

            elif stafur.islower():
                la_stafir += 1

        print()

        print("Í þessum texta eru",ha_stafir,"hástafir og",la_stafir,"lágstafir")

    elif valmynd == "7":
        tala_1 = int(input("Sláðu inn tölu sem er stærri en 0 "))
        tala_2 = int(input("Sláðu inn tölu sem er stærri en 0 "))

        if tala_1 > tala_2:
            staerri_talan = tala_1
            minni_talan = tala_2

        elif tala_1 < tala_2:
            staerri_talan = tala_2
            minni_talan = tala_1

        else:
            staerri_talan = tala_1
            minni_talan = tala_1

        if tala_1 > 0 and tala_2 > 0:
            for x in range(1,minni_talan+1):
                if tala_1 % x == 0 and tala_2 % x == 0:
                    samnefnari = x

        else:
            print("\nERROR\tSláðu inn tölur sem eru stærri en 0")

        print("\nStærsti samnefnarinn er",samnefnari)

    elif valmynd == "8":
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 8")
