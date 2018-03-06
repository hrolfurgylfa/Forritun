'''
Hlutapróf 1
Hrólfur Gylfason
12/2/2018
'''
def ofugur_strengur(strengur):
    strengur = strengur[::-1]
    return strengur

def agrodi_fall(innkaupsverð,virðusaukaskattur,söluverð):
    agrodi = söluverð - (innkaupsverð + virðusaukaskattur)
    return agrodi

def mismunur_fall(innkaupsverð,söluverð):
    if innkaupsverð > söluverð:
        print("Hér hefur eitthvað farið úrskeiðis")
    else:
        mismunur = söluverð - innkaupsverð
        print("Munurinn á innkaupsverði og söluverði er:",mismunur)

valmynd = ""

while valmynd != "4":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("1. Listi")
    print("2. Strengur")
    print("3. Föll")
    print("4. Hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        import random

        random_listi = []#Hérna bý ég til listann random_listi

        for tel in range(20):#Þessi for slaufa býr til 20 random tölur á bilinu 10-20 og bætir þeim á listann random_listi
            random_listi.append(random.randint(10,20))

        teljari = 0
        for tala in random_listi:#Þessi for lúppa rennur einusinni í gegn og svo verður breytan tala að næstu tölu í listanum random_listi
            if teljari != 19:#Þessi if setning er til þess að það komi ekki bandstrik eftir síðustu tölunna
                print(tala,end=" - ")
                teljari+=1
            else:
                print(tala)

        print()#Þetta er eitt enter og ég nota það til þess að gera forritið snirtilegt

        if random_listi.count(15) != 0:#Þessi if setning er til þess að forritið crashi ekki ef það er ekki 15 á listanum
            random_listi.remove(15)#.remove() eyðir tölunni af liustannum sem þú setir inn í svigann

        for tala in random_listi:#Þessi for lúppa prenntar út listann random_listi
            print(tala,end=", ")
        print()#Þetta er til þess að forritið dragi ekki næstu línu upp á sig vegna þess að ég notaði end=""

        print()#Þetta er eitt enter og ég nota það til þess að gera forritið snirtilegt

        random_listi_nyr = []

        for tala in random_listi:
            if tala == 20:
                random_listi_nyr.append(25)

            else:
                random_listi_nyr.append(tala)

        random_listi = random_listi_nyr

        for tala in random_listi:#Þessi for lúppa prenntar út listann random_listi
            print(tala,end=", ")
        print()#Þetta er til þess að forritið dragi ekki næstu línu upp á sig vegna þess að ég notaði end=""

        print()#Þetta er eitt enter og ég nota það til þess að gera forritið snirtilegt

        print("Meðaltal listans er:",sum(random_listi))
        print("Talan 25 kemur fram",random_listi.count(25),"sinnum")

    elif valmynd == "2":#Liður 2
        bil_teljari = 0
        stafa_teljari = 0
        b_teljari = 0
        tolustafa_teljari = 0

        strengur = input("Sláðu inn setningu ")

        for stafur in strengur:
            if stafur == " ":
                bil_teljari += 1

            if stafur == "b" or stafur == "B":
                b_teljari += 1

            if stafur == "0" or stafur == "1" or stafur == "2" or stafur == "3" or stafur == "4" or stafur == "5" or stafur == "6" or stafur == "7" or stafur == "8" or stafur == "9":
                tolustafa_teljari += 1

        print("Það eru",bil_teljari+1,"orð í þessari setningu")
        print("Setningin er",len(strengur),"stafa löng")
        print("Það eru",b_teljari,"B í setningunni")
        print("Það eru",tolustafa_teljari,"tölustafir í setningunni")
        print(ofugur_strengur(strengur))
        
    elif valmynd == "3":#Liður 3
        innkaupsverð = int(input("Sláðu inn innkaupsverð "))
        virðusaukaskattur = int(input("Sláðu inn virðusaukaskatt í krónum "))
        söluverð = int(input("Sláðu inn söluverð "))

        print()

        print("Ágróðinn er:",agrodi_fall(innkaupsverð,virðusaukaskattur,söluverð))
        mismunur_fall(innkaupsverð,söluverð)

    elif valmynd == "4":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 4")
