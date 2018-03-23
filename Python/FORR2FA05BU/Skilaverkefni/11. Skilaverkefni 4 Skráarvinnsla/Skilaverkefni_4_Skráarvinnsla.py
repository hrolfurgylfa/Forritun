'''
Skilaverkefni 4 Skráarvinnsla
Hrólfur Gylfason
9/3/2018
'''
def buaTilListaSlettarTolur(byrja,enda):#Þetta fall tekur inn byrjunarpunkt og endapunkt og skilar svo öllum sléttum tölum á því bili
    slettar_tolur = []

    for tala in range(byrja,enda + 1):
        if tala % 2 == 0:
            slettar_tolur.append(tala)

    return slettar_tolur

def buaTilSkraUrLista(skraarnafn,listi):#Þetta fall tekur inn skráarnafn og lista og býr svo til skrá sem geimir þennan lista
    strengur = ""

    skra = open(skraarnafn,"w")
    for tala in listi:
        strengur += str(tala)+"|"

    skra.write(strengur)
    skra.close()

def lesaSkraEinLinaTolur(skraarnafn):#Þetta fall tekur inn skráarnafn og skilar svo lista sem var í skjalinu svo lengi sem þessi skrá er bara ein lína og skráin inniheldur bara tölur
    skra = open(skraarnafn,"r")

    for line in skra:
        lina = line.split("|")

    tolu_listi = lina
    tolu_listi.pop()
    tolu_listi = list(map(int,tolu_listi))

    return tolu_listi

def medaltalLista(listi):#Þetta fall tekur inn lista og skilar svo meðaltali talnanna á listanum svo lengi sem listinn inniheldur bara int tölur
    return sum(listi)/len(listi)

def gangaUppI8(listi):#Þetta fall tekur inn lista og skilar svo lista af tölum af listanum sem ganga upp í átta svo lengi sem listinn inniheldur bara int tölur
    gangaUppI8_listi = []

    for tala in listi:
        if tala % 8 == 0:
            gangaUppI8_listi.append(tala)

    return gangaUppI8_listi

def skraarPrentari(skraarnafn):#Þetta fall tekur inn skráarnafn og prentar hana (skilar ekki neinu)
    skra = open(skraarnafn,"r")
    skraar_listi = []
    tel = 0

    for line in skra:
        lina = line.split("|")
        lina.pop()
        for hlutur in lina:
            skraar_listi.append(hlutur)

    for hlutur in skraar_listi:
        tel += 1
        if tel == 11:
            print("\n")
            tel = 1
        print(hlutur,end=" ")
    print()

def frumToluLeitari(byrjun,endir):#Þetta fall tekur inn byrjunarpunkt og endapunkt og skilar svo öllum frumtölunum á milli byrjunarpuntsins og endapuntsins í lista
    frum_tolu_listi = []

    for tala in range(byrjun,endir + 1):
        if tala > 1:
            for tala2 in range(2,tala):
                if tala % tala2 == 0:
                    break
            else:
                frum_tolu_listi.append(tala)
    return frum_tolu_listi

def listaPrentari(listi):#Þetta fall tekur inn lista og prenntar hann út fallega svo að það er komma á milli allra stafanna en ekki á eftir síðasta stafnum
    teljari = 0
    for hlutur in listi:
        teljari += 1
        if teljari == len(listi):
            print(hlutur)
        else:
            print(hlutur,end=", ")

def sjouPrentari_int(listi):#Þetta fall tekur inn lista og prenntar út allar tölur í listanum sem eru með 7 eitthverstaðar
    listi = list(map(str,listi))

    for hlutur in listi:
        if "7" in hlutur:
            print(hlutur,end=" ")
    print()

def fjordaHver(listi):#Þetta fall tekur inn lista og skilar svo fjórðu hverri tölu í lista
    fjorda_hver_listi = []
    tel = 0

    for hlutur in listi:
        tel += 1
        if tel == 4:
            fjorda_hver_listi.append(hlutur)
            tel = 0

    return fjorda_hver_listi

def nyTuple():#Þetta fall skilar bara tuple með oftast notuðu aðgangsorðum 2017 sem ég fann á wikipedia: https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
    return ("123456","password","12345678","qwerty","12345","123456789","letmein","1234567","football","iloveyou")

def buaTilSkjalUrDict(skraarnafn,dict_1):#Þetta fall tekur inn skráarnafn og dict og skrifar dict-ið svo í skránna
    skra = open(skraarnafn,"w")

    strengur = "{"
    for key in dict_1:
        strengur += str(key)+":"+str(dict_1[key])+","
    strengur = strengur[:-1]
    strengur += "}\n"

    skra.write(strengur)
    skra.close()

def baetaViðDictUrLista(skraarnafn,dict_1):#Þetta fall tekur inn skráarnafn og dict og bætir dict-inu svo við í skránna
    skra = open(skraarnafn,"a")

    strengur = "{"
    for key in dict_1:
        strengur += str(key)+":"+str(dict_1[key])+","
    strengur = strengur[:-1]
    strengur += "}\n"

    skra.write(strengur)
    skra.close()

def buaTilDictUrSkjali(skraarnafn):#Þetta fall tekur inn skráarnafn og tekur svo eitt eða fleiri dict úr skjalinu (tekur öll sem eru þar sem gæti verið frá einu og upp í 1000 eða jafnvel meira)
    skra = open(skraarnafn,"r")
    dict_1 = {}
    linur = []
    teljari = 0

    for line in skra:
        line = line[1:-2]
        lina = line.split(",")
        linur.append(lina)
    
    for lina in linur:
        for hlutur in lina:
            key_og_value = hlutur.split(":")
            dict_1.update({key_og_value[0]:key_og_value[1]})

    skra.close()
    return dict_1

def dictPrentari(dict_1):#Þetta fall tekur inn dict með nöfnum sem key og prentar þau snirtilega út svo að liklarnir og value-in séu alltaf á sama stað og eins dót fyrir ofan og neðan
    for tel in dict_1:
        if len(tel) >= 7:
            print(tel,"\t",dict_1[tel])
        else:
            print(tel,"\t\t",dict_1[tel])

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

    if valmynd == "1":#Dæmi 1
        buaTilSkraUrLista("Slettartolur.txt",buaTilListaSlettarTolur(1,1000))

        slettar_tolur_listi = lesaSkraEinLinaTolur("Slettartolur.txt")

        print("A. Prennta út allan listann:")#Dæmi 2 liður A
        print(slettar_tolur_listi)
        print()

        print("B. Meðaltal listans með tveimur aukastöfum:")#Dæmi 2 liður B
        print(round(medaltalLista(slettar_tolur_listi),2))
        print()

        print("C. Prennta út listann með tölum sem ganga upp í átta:")#Dæmi 2 liður C
        ganga_upp_i_8 = gangaUppI8(slettar_tolur_listi)
        print(ganga_upp_i_8)
        print()

        print("D. Listi úr C skrifaður í skjal")#Dæmi 2 liður D
        buaTilSkraUrLista("sumarslettartolur.txt",ganga_upp_i_8)
        print()

        print("E. Prenta út skránna með bil milli talnana og 10 tölum í línu")#Dæmi 1 liður E
        skraarPrentari("sumarslettartolur.txt")

    elif valmynd == "2":#Dæmi 2
        buaTilSkraUrLista("frumtolur.txt",frumToluLeitari(1,100))

        print("A. Lesa skránna og skila lista")#Dæmi 2 liður A
        frumtolur = lesaSkraEinLinaTolur("frumtolur.txt")
        print()

        print("B. Prenta út listann")#Dæmi 2 liður B
        listaPrentari(frumtolur)
        print()

        print("C. Prennta út allar tölurnar sem eru með 7 í þeim")#Dæmi 2 liður C
        sjouPrentari_int(frumtolur)
        print()

        print("D. Taka listann úr A, prennta út fjórðu hverja tölu og setja svo inn í aðra skrá")#Dæmi 2 liður D
        fjordaHverFrumtala_listi = fjordaHver(frumtolur)
        listaPrentari(fjordaHverFrumtala_listi)
        buaTilSkraUrLista("fjordaHverFrumtala.txt",fjordaHverFrumtala_listi)
        print()

        print("E. Prenta út skránna í D")#Dæmi 2 liður E
        skraarPrentari("fjordaHverFrumtala.txt")
        print()
        
    elif valmynd == "3":#Dæmi 3
        tuple_1 = (1,2,3,4,5,6,7,8,9)
        tuple_2 = ("a","b","c","d","e","f","g","h")
        tuple_3 = ("konni",123,"sponni",234)

        print("A. Prenta út tuplein")#Dæmi 3 liður A
        listaPrentari(tuple_1)
        listaPrentari(tuple_2)
        listaPrentari(tuple_3)
        print()

        print("B. Bæta við nýrri tuple að eigin vali")#Dæmi 3 liður B
        tuple_4 = nyTuple()
        print(tuple_4)
        print()

        print("C. Finna meðaltal fyrstu tuplunar")
        print(medaltalLista(tuple_1))

    elif valmynd == "4":#Dæmi 4
        #Hérna bý ég til dict-in sem ég mun svo nota seinna í dæminu
        dict_1 = {"Konni":1,"Snorri":2,"Kalli":3,"Palli":4}
        dict_2 = {"Elín":4,"Kristín":3,"Ragnheiður":2,"Elísabet":1}
        dict_3 = {"Óskar":2,"Björn":4,"Sólveig":1,"Hildur":3}

        print("A. Búa til skrá og setja dictionary-ið í hana")#Dæmi 4 liður A
        buaTilSkjalUrDict("dictionary.txt",dict_1)
        print()

        print("B. Skrifa út dictionary-ið")#Dæmi 4 liður B
        print(buaTilDictUrSkjali("dictionary.txt"))
        print()

        print("C. Bæta við tveimur dictionary-s")#Dæmi 4 liður C
        baetaViðDictUrLista("dictionary.txt",dict_2)
        baetaViðDictUrLista("dictionary.txt",dict_3)
        print()

        print("D. Skrifa út dictionary-in")#Dæmi 4 liður D
        dictPrentari(buaTilDictUrSkjali("dictionary.txt"))

    elif valmynd == "5":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 5" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 5")
