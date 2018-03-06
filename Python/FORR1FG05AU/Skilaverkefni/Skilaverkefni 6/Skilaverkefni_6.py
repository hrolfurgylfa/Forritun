'''
Hrólfur Gylfason 2017
Skilaverkefni 6
'''
import random#Hérna er ég að sækja random elementið
val="0"#Til þess að það komi ekki "NameError: 'val' is not defined"

while val!="11":#While lúppa til þess að þetta virki aftur og aftur án þess að þurfa að starta aftur
    print("--------------------------------------------------\n")
    print("1. Random tölur")
    print("2. Talnabil")
    print("3. Strengjalisti")
    print("4. Samanburður")
    print("5. Hætta")
    val=input("-------------------------------------> ")#Hérna velur notandinn í hvaða lið hann vill fara

    #Þetta er til þess að það verði til fínar línur í kringum hvern lið
    print()
    for tel in range(50):
        print("-", end="")
    print()

    if val=="1":#Hérna fer notandinn ef hann velur 1
        listi=[]
        for tel in range(50):
            listi.append(random.randint(5,71))#Þetta setir random tölu á bilinu 5-70 í listann
        sinnum_summa=1
        for tel in listi:#Keyrir eins oft og tölurnar eru margar í listanum og tel verður einu sinni hver einasta tala á listanunum
            sinnum_summa*=tel
        print("Þetta er talan sem kemur úr því að margfalda allar tölurnar í listanum saman:",sinnum_summa)
        print("Þetta er hæsta talan í listanum",max(listi))
        print("Þetta er lægsta talan í listanum",min(listi))
        print("Svona er listinn óraðaður",end=" ")
        for tel in listi:
            print(tel,end=" ")
        print()
        listi.sort()
        print("Svona er listinn raðaður",end=" ")
        for tel in listi:
            print(tel,end=" ")
        print()

    elif val=="2":#Hérna fer notandinn ef hann velur 2
        listi=[]
        for tala in range(2000,3201):#Fer í gegnum allar tölur frá 200 til 3200
            if tala % 7==0 and tel % 5 !=0:#Ef sjö gengur upp í töluna en ekki 5
                listi.append(tala)
        for tala in listi:
            if tala==listi[-1]:#Ef síðasta talan í listanum
                print(tala,end="")
            else:
                print(tala,end=", ")
        print()
        print("Summa talnana í listanum er",sum(listi))

    elif val=="3":#Hérna fer notandinn ef hann velur 3
        listi=[]
        numer=0
        teljari=0
        templisti=[]
        telur=0
        for tel in range(10):
            numer+=1
            nafn=input("Sláðu inn nafn númer "+str(numer)+" ").lower()#.lower() er vegna þess að ef það eru bæði stórir og litlir stafir ruglar það í stafrófsröðinni
            listi.append(nafn)
        print()#Print() gerir eitt enter og ég nota það til þess að það sé auðveldara að skilja útkomu forritsins
        for nafn in listi:
            if len(nafn)==4:#Er nafnið 4 stafir
                teljari+=1
        print("Fjöldi orða sem hafa fjóra stafi er",teljari)
        print()#Print() gerir eitt enter og ég nota það til þess að það sé auðveldara að skilja útkomu forritsins
        print("Svona er listinn ef annað hvert orð er skrifað öfugt:")
        tel2=1
        for nafn in listi:
            if tel2 % 2!=0:#Ef tel2 er oddatala tala
                print(nafn,end=" ")
            else:#Ef tel2 er slétt tala
                print(nafn[::-1],end=" ")#nafn[::-1] snýr strengnum við
            tel2+=1
        print()#Print() gerir eitt enter og ég nota það til þess að það sé auðveldara að skilja útkomu forritsins
        listi.sort()
        print("Svona er listinn raðaður:")
        for tel in listi:
            print(tel,end=" ")
        print("\n")
        stafur=input("Sláðu inn staf ")
        print("Öllum orðum verður eytt sem byrja á þessum staf")
        for nafn in listi:
            if stafur==nafn[0]:#nafn [0] er fyrsti stafurinn í nafn breytunni
                templisti.append(nafn)
        for nafn in templisti:
            listi.remove(nafn)
            telur+=1
        print("fjöldi orða eytt",telur)
        for tel in listi:
            print(tel,end=" ")
        print()

    elif val=="4":#Hérna fer notandinn ef hann velur 4
        listi1=[]
        listi2=[]
        samanlisti=[]
        print("Sláðu inn orð í lista 1")
        for tel in range(7):
            ord1=input("Sláðu inn orð ")
            listi1.append(ord1)
        print("\nSláðu inn orð í lista 2")
        for tel in range(6):
            ord1=input("Sláðu inn orð ")
            listi2.append(ord1)
        for ord1 in listi1:
            if ord1 in listi2:
                samanlisti.append(ord1)
        print()
        print("Þetta eru orð sem eru í báðum listunum: ",end=" ")
        for tel in samanlisti:
            print(tel,end=" ")
        print()        

    elif val=="5":
        pass#Þetta er til þess að forritið segi ekki error og hætti svo heldur hætti það bara

    else:#Hérna fer notandinn ef hann velur eitthverja tölu sem er ekki liður eða eitthvað annað en tölu
        print("ERROR\trangur innsláttur")

