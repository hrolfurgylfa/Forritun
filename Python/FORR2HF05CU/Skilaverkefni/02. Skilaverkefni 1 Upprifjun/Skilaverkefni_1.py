'''
Skilaverkefni 1 Upprifjun
Hrólfur Gylfason
5/9/2018
'''
def leitaIDict(dict1, leit):#Þessi for lúppa tekur inn dictionary og key sem fallið á að finna og ef að fallið finnur key-inn skilar það honum en ef ekki þá skilar hún 0000000
    for key in dict1:
        if key == leit:
            return dict1[key]
        
    return 0000000

def baetaVidIDict(dict1, key, value, key_til, successfull_str):#Þessi for lúppa tekur inn dictionary, key, value og strengi og skilar svo dictionary sem er búið að bæta lyklinum og gildinu í og svo koma annaðhvort key_til eða successfull_str oftir því hvort að það hepnist eða ekki
    dict2 = dict1.copy()

    for key2 in dict2:
        if key2 == key:
            print("\n"+str(key_til))
            return dict2

    dict2[key] = value
    print("\n"+str(successfull_str))
    return dict2

def eydaAfDict(dict1, key):#Þessi for lúppa tekur inn dictionary og key og skilar svo dictionary þar sem það er búið að eyða lyklinum
    dict2 = {}

    for key2 in dict1:
        if key2 == key:
            print()
            print(key,"hefur verið eytt")
        else:
            dict2[key2] = dict1[key2]

    return dict2

def breytaValueADict(dict1, key, breytt_value, engu_breytt_texti, eitthverju_breytt_texti):#Þessi for lúppa tekur inn dictionary, key, breytt gildi og strengi sem eru prentaðir út eftir því hvað gerist, svo skilar fallið dictionaryi þar sem það er búið að skipta út gildinu á lyklinum sem kom inn fyrir gildið sem kom inn
    dict2 = dict1.copy()

    for key2 in dict2:
        if key2 == key:
            dict2[key2] = breytt_value

            print(eitthverju_breytt_texti)
            return dict2
    
    print(engu_breytt_texti)

def buaTilHop(nafn_hops):#Þetta tekur inn nafn hóps til þess að prenta það út og tekur svo líka input frá notenda til þess að búa til hóp og skilar hópnum í lista
    listi = []

    fjoldi = int(input("Hversu margir eru skráðir í "+str(nafn_hops)+"?\n--->"))

    for tel in range(fjoldi):
        nemandi = input("\nSláðu inn nafn nemanda\n--->")
        listi.append(nemandi)

    return listi

def prentaLista(listi, sort, fyrirsogn):#Þessi for lúppa tekur inn lista, boolianið sort og fyrirsögn á listann, svo prentar þetta út listann, eitt nafn í línu með fyrir sögninni sem kom inn og flokkar listann ef sort er satt
    if sort == True:
        listi.sort()
    
    print(fyrirsogn)
    for hlutur in listi:
        print(hlutur)

def beraSamanLista(listi1, listi2):#Þessi for lúppa tekur inn tvo lista og skilar svo lista sem er með öllum hlutunum sem eru í báðum listunum
    i_badum = []

    for hlutur1 in listi1:
        for hlutur2 in listi2:
            if hlutur1 == hlutur2:
                i_badum.append(hlutur1)

    return i_badum

def hvorListiStaerri(listi1, listi2, nafn1, nafn2):#Þessi for lúppa tekur inn tvo lista og nöfnin á listunum og skilar svo nafninu á listanum sem er stærri eða J ef þeir eru jafn stórir
    if len(listi1) == len(listi2):
        return "J"#J er fyrir Jafn Stórir
    
    elif len(listi1) > len(listi2):
        return nafn1
    
    elif len(listi1) < len(listi2):
        return nafn2

    else:
        print("ERROR\tFallið hvorListiStaerri klikkaði")

def faeraMilliLista(listi1, listi2, numer_fra_listi1):#Þessi for lúppa tekur inn tvo lista og númer úr lista 1 svo eyðir for slaufan staki af lista 1 sem er með númer numer_fra_lista, bætir því við á lista 2 og skilar svo báðum listunum í lista
    listi2.append(listi1[numer_fra_listi1])
    listi1.pop(numer_fra_listi1)

    return [listi1,listi2]

def vixlaStreng(strengur, lastafir):#Þessi for slaufa tekur inn streng og hvort að þetta egi að koma í hástöfum eða lágstöfum
    strengur2 = ""
    sidasti_stafur = ""
    loka_strengur = ""
    listi = []

    if len(strengur) % 2 != 0:#Þetta bætir síðasta stafnum af strengnum við í breytu til þess að setja á í lokin ef að strengurinn er oddatala
        sidasti_stafur += strengur[-1]

    for tel in range(1,len(strengur),2):#Þessi for slaufaer til þess að bæta strengnum í lista og víxla stöfunum í leiðinni
        if lastafir:#Þetta er til þess að það sé hægt að nota þetta til þess að breyta stöfunum í ruglaða stafi og til baka
            strengur2 = strengur[tel].lower()
            strengur2 += strengur[tel-1].lower()
        else:
            strengur2 = strengur[tel].upper()
            strengur2 += strengur[tel-1].upper()

        listi.append(strengur2)
    
    for tempStrengur in listi:#Þessi for slaufa er til þess að bæta lokastafnum á sem við geymdum áðan ef strengurinn er oddatala
        loka_strengur += tempStrengur
    if lastafir:
        loka_strengur += sidasti_stafur.lower()
    else:
        loka_strengur += sidasti_stafur.upper()

    return loka_strengur

def lesaLykilordaSkra(skraarnafn):#Þessi for slaufa tekur inn skráarnafn, les skrá sem hefur semíkommu á milli tveggja hluta og enter í næsta par, setir það í dictionary og skilar dictionaryinu
    dict1 = {}
    skra = open(skraarnafn,"r")

    for line in skra:
        lina = line.split(";")
        dict1[lina[0]] = lina[1][0:-1]

    return dict1

def finnaKeyOgValueIDict(key, value, dict1, key_fundinn_txt, baedi_fundin_txt, hvorugt_fundid_txt):#Þessi for slaufa tekur inn key, value, dictionary og texta. Svo prentar hún út mismunandi skilaboð eftir því hvort að lykillinn hafi fundist, lykillinn og gildið hafi fundist eða hvorugt hafi fundist
    notandi_fundinn = False

    for key1 in dict1:
        if key1 == key:
            if dict1[key1] == value:
                print(baedi_fundin_txt)
                notandi_fundinn = True
                break
                
            else:
                print(key_fundinn_txt)
                notandi_fundinn = True
                break
    
    if not notandi_fundinn:
        print(hvorugt_fundid_txt)


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

        #Hérna er valmynd fyrir lið 1
        while val1 != "5":
            
            print("Ýttu á 1 til þess að finna símanúmer eftir nafni")
            print("Ýttu á 2 til þess að bæta við nafni og símanúmeri")
            print("Ýttu á 3 til þess að eyða út nafni og símanúmeri")
            print("Ýttu á 4 til þess að breyta símanúmeri")
            print("Ýttu á 5 til þess að hætta")
            val1 = input("-------------------->>> ")

            print("\n----------------------------------------")

            if val1 == "1":# A
                leitarnafn = input("Sláðu inn nafn til þess að leita að\n--->")
                print()

                simanumer = leitaIDict(simaskra, leitarnafn.lower())

                if simanumer == 0000000:#Þetta kemur ef nafnið er ekki fundið
                    print("Nafnið",leitarnafn,"er ekki í símaskránni")
                
                else:
                    print(leitarnafn,"er með símanúmerið",simanumer)
            
            elif val1 == "2":# B
                nafn = input("Sláðu inn nafn\n--->").lower()
                print()
                simanumer = input("Sláðu inn símanúmer\n--->")

                if simanumer.isdigit() == True:#Þetta passar að númerið sé int
                    simanumer = int(simanumer)
                    if simanumer >= 4000000 and simanumer <= 8999999:#Þetta passar að númerið sé alvöru númer
                        simaskra = baetaVidIDict(simaskra, nafn, simanumer, "Þessi persóna er núþegar til í símaskránni", "Tengiliði bætt í símaskránna")
                    else:
                        print("Þetta er ógillt símanúmer")
                else:
                    print("Þetta er ógillt símanúmer")

            elif val1 == "3":# C
                nafn = input("Sláðu inn nafn\n--->").lower()
                
                simaskra = eydaAfDict(simaskra, nafn)

            elif val1 == "4":# D
                nafn = input("Sláðu inn nafn\n--->").lower()
                print()
                simanumer = input("Sláðu inn símanúmer\n--->")

                print()
                breytaValueADict(simaskra, nafn, simanumer, "Þessi notandi var ekki fundinn", "Það hefur verið breytt símanúmeri tengiliðsins "+str(nafn)+" í "+str(simanumer))

            elif val1 == "5":#Þetta er til þess að forritið segi ekki ERROR þegar maður fer úr valmyndinni
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

        # Bera saman lista
        i_badum_hopum = beraSamanLista(hopur1, hopur2)

        if i_badum_hopum:#Þetta tékkar hvort að listinn sé nokkuð tómur svo að forritið prenti ekki út tóman lista
            prentaLista(i_badum_hopum, True, "Þessir nemendur eru í báðum hópunum:")
        
        else:
            print("Það eru engir nemendur í báðum hópunum")
        
        print()

        # Hvor er stærri
        hvor_er_staerri = hvorListiStaerri(hopur1, hopur2, "FOR1TÖ05CU", "GSÖ1TÖ05AU")
        
        if hvor_er_staerri == "J":
            print("Bekkirnir eru jafn stórir")
        else:
            print(hvor_er_staerri,"er stærri bekkurinn")
        
        #Að færa tvo öftustu nemendurna
        faeraMilliLista(hopur1, hopur2, -1)
        faeraMilliLista(hopur1, hopur2, -1)

    elif valmynd == "3":#Liður 3
        notendanafn = input("Sláðu inn notendanafnið þitt\n--->")
        print()
        lykilord = input("Sláðu inn lykilorð\n--->")

        password_dict = lesaLykilordaSkra("lykilord.txt")#Þetta er hérna til þess að það sé auðveldara að lesa kóðann en þetta gæti verið inni í kallinu á fallið sem er hérna fyrir neðan

        finnaKeyOgValueIDict(notendanafn, lykilord, password_dict, "\nRangt lykilorð", "\nVelkomin/n", "\nÞessi notandi er ekki til")

    elif valmynd == "4":#Liður 4
        strengur = input("Sláðu inn orð eða setningu til þess að víxla\n--->")
        print("\n"+str(vixlaStreng(strengur, False)))

        strengur = input("\nSláðu inn orð eða setningu til þess að laga víxl\n--->")
        print("\n"+str(vixlaStreng(strengur, True)))# Eini munurinn er það að það þarf að prenta út í lágstöfum en ekki hástöfum svo að ég gerði boolean fyrir það

    elif valmynd == "5":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 5" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 5")
