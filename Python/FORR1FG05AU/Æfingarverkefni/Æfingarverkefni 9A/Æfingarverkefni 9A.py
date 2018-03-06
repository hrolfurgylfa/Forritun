'''
Hrólfur Gylfason 2017
Æfingarverkefni 9A
'''
import random
val="0"#Til þess að það komi ekki "NameError: 'val' is not defined"

while val!="5":#While lúppa til þess að þetta virki aftur og aftur án þess að þurfa að starta aftur
    print("--------------------------------------------------\n")
    print("Ýttu á 1 til þess að skoða lið eitt")
    print("Ýttu á 2 til þess að skoða lið tvö")
    print("Ýttu á 3 til þess að skoða lið þrjú")
    print("Ýttu á 4 til þess að skoða lið fjögur")
    print("Ýttu á 5 til þess að hætta")
    val=input("-------------------------------------> ")#Hérna velur notandinn í hvaða lið hann vill fara

    #Þetta er til þess að það verði til fínar línur í kringum hvern lið
    print()
    for tel in range(50):
        print("-", end="")
    print()

    if val=="1":#Hérna fer notandinn ef hann velur 1
        listi=[]
        h_afram=""
        while h_afram!="nei":
            listi.append(input("Sláðu inn hlut sem þér langar að bæta við á innkaupalistann ").lower())#.lower() er vegna þess að stórir stafir fokka í stafrófstöðinni svo að ef sumt er með stórum stöfum og annað með litlum ruglar það í stafrófsröðinni
            print("Innkaupalistinn þinn er núna")
            listi.sort()
            print()
            for tel in listi:
                print(tel,end="\n")
            print()
            h_afram=input("Langar þér að bæta öðrum hlut á innkaupalistann? ").lower()

    elif val=="2":#Hérna fer notandinn ef hann velur 2
        summa=0
        listi=[]
        for tel in range(15):
            listi.append(random.randint(5,25))
        listi.sort()
        for tel in listi:
            print(tel,end=" ")
        print()
        print("Lægsta talan er",min(listi))
        print("Hæðsta talan er",max(listi))
        print("Summa talnana er",sum(listi))
        print("Listinn er",len(listi),"tölur")
            

    elif val=="3":#Hérna fer notandinn ef hann velur 3
        listi=[]
        for tel in range(20):
            listi.append(random.randint(0,99))
        listi2=[listi[0],listi[-1]]
        for tel in listi2:       
            print(tel,end=" ")  
        print()                 

    elif val=="4":#Hérna fer notandinn ef hann velur 4
        listi=[]
        tel=0
        while tel!=10:
            nafn=input("Sláðu inn nafn nemanda ")
            if nafn not in listi:
                listi.append(nafn)
                tel+=1
            else:
                print("Þetta nafn er núþegar á listanum, vinsamlegast sláðu inn annað nafn ")
        listi.reverse()
        for tel in listi:
            print(tel,end="\n")
    
    elif val=="5":
        pass#Þetta er til þess að forritið segi ekki error og hætti svo heldur hætti það bara

    else:#Hérna fer notandinn ef hann velur eitthverja tölu sem er ekki liður eða eitthvað annað en tölu
        print("ERROR\trangur innsláttur")

