'''
Hrólfur Gylfason 2017
Skilaverkefni 5
'''
val="0"#Til þess að það komi ekki "NameError: 'val' is not defined"

while val!="4":#While lúppa til þess að þetta virki aftur og aftur án þess að þurfa að starta aftur
    
    print("--------------------------------------------------\n")
    print("1. Kennitala")
    print("2. Búa til nýtt orð")
    print("3. Sneið af streng")
    print("4. Hætta")
    val=input("-------------------------------------> ")#Hérna velur notandinn í hvaða lið hann vill fara

    #Þetta er til þess að það verði til fínar línur í kringum hvern lið
    print()
    for tel in range(50):
        print("-", end="")
    print()

    if val=="1":#Hérna fer notandinn ef hann velur 1
        k_tala_t_f=0#Hérna er resetter fyrir þetta variable til þess að þegar maður fer oftar en einu sinni í þennan lið detti maður ekki í gegn eins og maður hafi skrifað inn rétta kennitölu
        while k_tala_t_f==0:#While lúppa til þess að maður þurfi að gera aftur ef maður slær inn ranga kennitölu
            k_tala=input("Sláðu inn kennitölu ")#input fyrir notandann
            #Tala 1-2
            t1_2=k_tala[0:2]
            t1_2=int(t1_2)
            #Tala 3-4
            t3_4=k_tala[2:4]
            t3_4=int(t3_4)
            #Tala 5-6
            t5_6=k_tala[4:6]
            t5_6=int(t5_6)
            #Hérna er if setninginn þar sem ég nota and í staðin fyrir fullt af if setningum
            if len(k_tala)==10 and t1_2<32 and t1_2>0 and t3_4>0 and t3_4<13:
                if t5_6<17 and k_tala[-1]=="0":#Hérna fer maður ef kennitalan endar á núll og maður er fæddur á undan 2017 vegna þess að ef maður er fæddur eftir 2017 er maður ekki fæddur
                    print("Vel gert þú slóst inn rétta kennitölu,",k_tala)
                    k_tala_t_f=1#Hérna seti ég 1 á þetta og nota þetta eins og true/false tengt því hvort maður þurfi að gera þetta aftur
                elif k_tala[-1]=="9":#Hérna fer maður ef kennitalan endar á 9
                    print("Vel gert þú slóst inn rétta kennitölu,",k_tala)
                    k_tala_t_f=1#Hérna seti ég 1 á þetta og nota þetta eins og true/false tengt því hvort maður þurfi að gera þetta aftur
                else:#Hérna fer manneskjan ef hún skrifar inn vitlausa kennitölu
                    print("\nRöng kennitala\nsláðu inn rétta kennitölu\n")
            else:#Hérna fer manneskjan ef hún skrifar inn vitlausa kennitölu
                print("\nRöng kennitala\nsláðu inn rétta kennitölu\n")

    elif val=="2":#Hérna fer notandinn ef hann velur 2
        orð=""#þetta er til þess að while lúppan crashi ekki vegna þess að breytan orð sé ekki til
        while len(orð)<5:#While lúppa sem hleypir þér ekki út nema þú skrifir inn orð sem er lengra en fimm stafir
            orð=input("Sláðu inn orð/setningu sem er 5 stafir eða meira ")
            if len(orð)<5:#Hérna fernotandinn ef hann skrifar ekki inn orð sem er lengra en fimm stafir
                print("Vinsamlegast sláðu inn orð/setningu sem er 5 stafir eða meira\n")
        orð_1=orð[0:2]#Hérna tek ég tvo fyrstu stafina af orðinu
        orð_2=orð[-2:]#Hérna tek ég tvo fyrstu stafina af orðinu 
        orð_out=orð_1+orð_2#Hérna plúsa ég saman tvo fyrstu stafi orðsins og tvo síðustu
        print("Nýji strengurinn er:",orð_out)
        print("Nýji strengurinn í lágstöfum er:",orð_out.lower())#.lower() skipunin setir alla stafina í lágstafi
        print("Nýji strengurinn í hástöfum er:",orð_out.upper())#.upper() skipunin setir alla stafina í hástafi

    elif val=="3":#Hérna fer notandinn ef hann velur 3
        nafn=input("Sláðu inn nafn ")#Hérna fæ ég notandann til þess að skrifa inn nafn
        for tel in range(len(nafn)):#ég seti len(nafn) í range skipunina til þess að þetta sé endurtekið jafn oft og það eru stafir í nafninu
            print(nafn)
            nafn=nafn[1:]#[1:] þýðir 1 og aftari stafir(0 er fyrstur svo að þetta er stafur 2 og að endanum) svo að þetta klippir fyrsta stafinn af nafninu og svo er þetta gert aftur

    elif val=="4":
        pass#Þetta er til þess að forritið segi ekki error og hætti svo heldur hætti bara

    else:#Hérna fer notandinn ef hann velur eitthverja tölu sem er ekki liður eða eitthvað annað en tölu
        print("ERROR\trangur innsláttur")
