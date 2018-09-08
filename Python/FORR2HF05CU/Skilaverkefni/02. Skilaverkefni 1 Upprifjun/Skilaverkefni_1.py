'''
Skilaverkefni 1 Upprifjun
Hrólfur Gylfason
5/9/2018
'''
def leitaIDict(dict1, leit):
    for key in dict1:
        if key == leit:
            return dict1[key]
        
    return 0000000

def baetaVidIDict(dict1, key, value, key_til, successfull_str):
    dict2 = dict1.copy()

    for key2 in dict2:
        if key2 == key:
            print("\n"+str(key_til))
            return dict2

    dict2[key] = value
    print("\n"+str(successfull_str))
    return dict2

def eydaAfDict(dict1, key):
    dict2 = {}

    for key2 in dict1:
        if key2 == key:
            print()
            print(key,"hefur verið eytt")
        else:
            dict2[key2] = dict1[key2]

    return dict2

def breytaValueADict(dict1, key, breytt_value, engu_breytt_texti, eitthverju_breytt_texti):
    dict2 = dict1.copy()

    for key2 in dict2:
        if key2 == key:
            dict2[key2] = breytt_value

            print(eitthverju_breytt_texti)
            return dict2
    
    print(engu_breytt_texti)

def buaTilHop(nafn_hops):
    listi = []

    fjoldi = int(input("Hversu margir eru skráðir í "+str(nafn_hops)+"?\n--->"))

    for tel in range(fjoldi):
        nemandi = input("\nSláðu inn nafn nemanda\n--->")
        listi.append(nemandi)

    return listi

def prentaLista(listi, sort, fyrirsogn):
    if sort == True:
        listi.sort()
    
    print(fyrirsogn)
    for hlutur in listi:
        print(hlutur)

def beraSamanLista(listi1, listi2):
    i_badum = []

    for hlutur1 in listi1:
        for hlutur2 in listi2:
            if hlutur1 == hlutur2:
                i_badum.append(hlutur1)

    return i_badum

def hvorListiStaerri(listi1, listi2, nafn1, nafn2):
    if len(listi1) == len(listi2):
        return "J"#J er fyrir Jafn Stórir
    
    elif len(listi1) > len(listi2):
        return nafn1
    
    elif len(listi1) < len(listi2):
        return nafn2

    else:
        print("ERROR\tFallið hvorListiStaerri klikkaði")

def faeraMilliLista(listi1, listi2, numer_fra_listi1):
    listi2.append(listi1[numer_fra_listi1])
    listi1.pop(numer_fra_listi1)

    return [listi1,listi2]

def vixlaStreng(strengur, lastafir):
    strengur2 = ""
    sidasti_stafur = ""
    loka_strengur = ""
    listi = []

    if len(strengur) % 2 != 0:
        sidasti_stafur += strengur[-1]

    for tel in range(1,len(strengur),2):
        if lastafir:
            strengur2 = strengur[tel].lower()
            strengur2 += strengur[tel-1].lower()
        else:
            strengur2 = strengur[tel].upper()
            strengur2 += strengur[tel-1].upper()

        listi.append(strengur2)
    
    for tempStrengur in listi:
        loka_strengur += tempStrengur
    if lastafir:
        loka_strengur += sidasti_stafur.lower()
    else:
        loka_strengur += sidasti_stafur.upper()

    return loka_strengur


valmynd = ""

while valmynd != "5":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að fá dæmi 4")
    print("Ýttu á 5 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        simaskra = {"inga": "6965964", "karl": "7913812", "guðný": "7484947", "sólveig": "6123435", "halldór": "8050842", "elín": "8475938", "kristján": "8909915", "daníel": "8596066", "jón": "6683621", "björn": "6889840"}
        val1 = ""

        while val1 != "5":
            
            print("Ýttu á 1 til þess að finna símanúmer eftir nafni")
            print("Ýttu á 2 til þess að bæta við nafni og símanúmeri")
            print("Ýttu á 3 til þess að eyða út nafni og símanúmeri")
            print("Ýttu á 4 til þess að breyta símanúmeri")
            print("Ýttu á 5 til þess að hætta")
            val1 = input("-------------------->>> ")

            print("\n----------------------------------------")

            if val1 == "1":
                leitarnafn = input("Sláðu inn nafn til þess að leita að\n--->")
                print()

                simanumer = leitaIDict(simaskra, leitarnafn.lower())

                if simanumer == 0000000:
                    print("Nafnið",leitarnafn,"er ekki í símaskránni")
                
                else:
                    print(leitarnafn,"er með símanúmerið",simanumer)
            
            elif val1 == "2":
                nafn = input("Sláðu inn nafn\n--->").lower()
                print()
                simanumer = input("Sláðu inn símanúmer\n--->")

                if simanumer.isdigit() == True:
                    simanumer = int(simanumer)
                    if simanumer >= 4000000 and simanumer <= 8999999:
                        simaskra = baetaVidIDict(simaskra, nafn, simanumer, "Þessi persóna er núþegar til í símaskránni", "Tengiliði bætt í símaskránna")
                    else:
                        print("Þetta er ógillt símanúmer2")
                else:
                    print("Þetta er ógillt símanúmer")

            elif val1 == "3":
                nafn = input("Sláðu inn nafn\n--->").lower()
                
                simaskra = eydaAfDict(simaskra, nafn)

            elif val1 == "4":
                nafn = input("Sláðu inn nafn\n--->").lower()
                print()
                simanumer = input("Sláðu inn símanúmer\n--->")

                print()
                breytaValueADict(simaskra, nafn, simanumer, "Þessi notandi var ekki fundinn", "Það hefur verið breytt símanúmeri tengiliðsins "+str(nafn)+" í "+str(simanumer))

            elif val1 == "5":
                pass
            
            else:
                print("ERROR\tSláðu inn tölu á milli 1 og 5")

            print("----------------------------------------\n")

    elif valmynd == "2":#Liður 2
        # Búa til listana
        hopur1 = buaTilHop("FOR1TÖ05CU")
        print()
        hopur2 = buaTilHop("GSÖ1TÖ05AU")

        # Prenta út hóp
        print()
        prentaLista(hopur1, True, "Nemendur í FOR1TÖ05CU:")
        print()
        prentaLista(hopur2, True, "Nemendur í GSÖ1TÖ05AU:")
        print()

        #Bera saman lista
        i_badum_hopum = beraSamanLista(hopur1, hopur2)

        if i_badum_hopum:
            prentaLista(i_badum_hopum, True, "Þessir nemendur eru í báðum hópunum:")
        
        else:
            print("Það eru engir nemendur í báðum hópunum")
        
        print()

        #Hvor er stærri
        hvor_er_staerri = hvorListiStaerri(hopur1, hopur2, "FOR1TÖ05CU", "GSÖ1TÖ05AU")
        
        if hvor_er_staerri == "J":
            print("Bekkirnir eru jafn stórir")
        else:
            print(hvor_er_staerri,"er stærri bekkurinn")
        
        #Að færa tvo öftustu nemendurna
        faeraMilliLista(hopur1, hopur2, -1)
        faeraMilliLista(hopur1, hopur2, -1)

    elif valmynd == "3":#Liður 3
        pass

    elif valmynd == "4":#Liður 4
        strengur = input("Sláðu inn orð eða setningu til þess að víxla\n--->")
        print("\n"+str(vixlaStreng(strengur, False)))

        strengur = input("\nSláðu inn orð eða setningu til þess að laga víxl\n--->")
        print("\n"+str(vixlaStreng(strengur, True)))

    elif valmynd == "5":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 5" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 5")
