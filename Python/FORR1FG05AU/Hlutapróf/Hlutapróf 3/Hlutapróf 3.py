import random
'''
Hrólfur Gylfason 2017
Hlutapróf 3
'''
val="0"#Til þess að það komi ekki "NameError: 'val' is not defined"

while val!="4":#While lúppa til þess að þetta virki aftur og aftur án þess að þurfa að starta aftur
    print("--------------------------------------------------\n")
    print("1. Skrifa út tölurnar 200-300 í eina línu")
    print("2. Vinna með tilviljanakenndar (random) tölur")
    print("3. Vinna með texta (streng)")
    print("4. Hætta")
    val=input("-------------------------------------> ")#Hérna velur notandinn í hvaða lið hann vill fara

    #Þetta er til þess að það verði til fínar línur í kringum hvern lið
    print()
    for tel in range(50):
        print("-", end="")
    print()

    if val=="1":#Hérna fer notandinn ef hann velur 1
        for tala in range(200,301):#Þetta skýrir tala breytuna 200, hún fer í gegn og þegar hún er búin er hækkar um einn þangað til hún er að fara að leggja á stað í 301 skipti og þá er hún stoppuð áður en hún byrjar
            print(tala,end="  ")
        print()

    elif val=="2":#Hérna fer notandinn ef hann velur 2
        listi=[]#Hérna bý ég til tvo tóma lista
        listi_1020_plus=[]
        for tel in range(150):#Þetta geri ég 150 sinnum
            random_tala=random.randint(1000,1030)#Þetta setir random tölu á milli 1000 og 1030 í breytuna random_tala 
            listi.append(random_tala)#Hérna bæti ég breytunni random_tala á listann listi
        listi_summa=sum(listi)
        listi_medaltal=listi_summa/150
        print("Meðaltal talnana með einum aukastaf er:",round(listi_medaltal,1),"\n")
        print("1005 kom upp",listi.count(1005),"sinnum\n")
        for tala in listi:
            if tala>1020:
                listi_1020_plus.append(tala)#Hérna bæti ég breytunni tala á listann listi_1020_plus
        print("Þetta eru allar tölurnar hærri en 1020:",end=" ")    
        for tala in listi_1020_plus:#Ég notaði þetta til þess að það kæmu ekki hornsvigar í kring um listann eins og kemur ef maður gerir print(listi_1020_plus)
            print(tala,end=", ")
        print("\n")
        print("Þetta eru allar tölurnar lægri en 1010:",end=" ")
        for tala in listi:#Hérna notaði ég það sama og í síðasta commenti til þess að eyða hornsvigunum
            if tala<1010:
                print(tala,end=", ")
        print()

    elif val=="3":#Hérna fer notandinn ef hann velur 3
        f_teljari=0
        texti=input("Sláðu inn texta ")#Hérna er input fyrir notandann
        texti_lower=texti.lower()#Hérna bjó ég til nýja breytu og notaði .lower() svo að þessi yrði bara í lágstöfum
        print("Svona er textinn í lágstöfum:",texti_lower)
        for stafur in texti:#Hérna tel ég hversu mörg f eru í breytuni texti
            if stafur=="f" or stafur=="F":
                f_teljari+=1
        print("f kom fyrir",f_teljari,"sinnum")
        for stafur in texti:#Hérna breytti ég öllum stöfum nema a í ?
            if stafur!="a" and stafur!="A":
                texti=texti.replace(stafur,"?")
        print(texti)
        
    elif val=="4":#Þetta er til þess að forritið segi ekki error og hætti svo heldur hætti það bara
        pass

    else:#Hérna fer notandinn ef hann velur eitthverja tölu sem er ekki liður eða eitthvað annað en tölu
        print("ERROR\trangur innsláttur")

