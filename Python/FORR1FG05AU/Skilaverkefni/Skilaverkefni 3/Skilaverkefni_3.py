'''
Höfundur: Hrólfur Gylfason
Skilaverkefni 3
'''
#til þess að forritið crasi ekki þegar það lendir á while loopum sem nota þessar breytur
d5_tel=0
val="Starter"
halda_afram_D_1="Starter"
halda_afram_D_2="Starter"
not_lykilord="Starter"
halda_afram_D_4="Starter"
halda_afram_D5="Starter"
while val!="7":#Endurtekning þangað til notandinn slær inn 7
    val="Starter"
    print("Sláðu inn 1 ef þú vilt sjá Lið 1")
    print("Sláðu inn 2 ef þú vilt sjá Lið 2")
    print("Sláðu inn 3 ef þú vilt sjá Lið 3")
    print("Sláðu inn 4 ef þú vilt sjá Lið 4")
    print("Sláðu inn 5 ef þú vilt sjá Lið 5")
    print("Sláðu inn 6 ef þú vilt sjá Lið 6")
    print("Sláðu inn 7 ef þú vilt hætta")
    val=input("----------------------------------> ")
    #Liður 1
    if val=="1":#Ef val er einn gerir hún það sem er fyrir neðan
        while halda_afram_D_1!="nei":#Þetta er endalaus loopa þangað til notandin segir nei
            #Hérna bið ég notandan um að slá inn tölu
            tala=int(input("Sláðu inn heiltölu "))
            #Hérna segi ég honum hvaða tölu hann sló inn
            print("Þú slóst inn töluna",tala)
            #Hérna spyr ég notandann hvort hann vilji gera þetta aftur
            halda_afram_D_1=input("Langar þig að gera þetta aftur?\nSláðu inn já eða nei ").lower()

    #liður 2
    elif val=="2":#Ef val er tveir gerir hún það sem er fyrir neðan
        while halda_afram_D_2!="nei":#Þetta er endalaus loopa þangað til notandin segir nei
            #Hérna spyr ég notandann um lengd og breidd ferhyrningsins
            lengd=int(input("Sláðu inn lengd ferhyrningsins "))
            breidd=int(input("Sláðu inn breidd ferhyrningsins "))
            #Útreykningar
            flatarmal=lengd*breidd
            #Úttak
            print("Flatarmál ferhyrningsins er",flatarmal)
            #Hérna spyr ég notandann hvort hann vilji gera þetta aftur
            halda_afram_D_2=input("Langar þig að gera þetta aftur?\nSláðu inn já eða nei ").lower()

    #Liður 3
    elif val=="3":#Ef val er þrír gerir hún það sem er fyrir neðan
        lykilord="lykilorðið"#Hérna er lykilorðið
        not_lykilord="Starter"#Til þess að forritið muni ekki lykilorðið
        #heldur áfram á meðan notandinn slær ekki inn rétta lykilorðið
        while not_lykilord!="lykilorðið":
            #hérna slær notandinn inn lykilorð
            not_lykilord=input("Sláðu inn lykilorðið ").lower()
            #gefur villuskylaboð ef maður slær inn rangt lykilorð
            if lykilord!=not_lykilord:
                #Úttak
                print("Rangt lykilorð, reyndu aftur")
        #Úttak ef maður gerir rétt lykilorð
        print("Velkomin/nn\n\n")

    #Liður 4
    elif val=="4":#Ef val er fjórir gerir hún það sem er fyrir neðan
        while halda_afram_D_4!="nei":
            tala_D4=int(input("Sláðu inn heiltölu "))
            #Útreykningar og Úttak
            if tala_D4%5==0:#Hérna fer notandinn ef það er hægt að deila töluni með 5 og afgangurinn er 0 
                print("Talan er í fimm sinnum töfluni")
            else:#Hérna fer notandinn ef það er ekki hægt að deila tölunni með fimm og fá 0 í afgang 
                print("Talan er ekki í fimm sinnum töfluni")
            halda_afram_D_4=input("Viltu gera þetta aftur?\nSláðu inn já eða nei ").lower()#Hérna spyr ég notandann hvort hann vilji gera þetta dæmi aftur

    #Liður 5
    elif val=="5":#Ef val er fimm gerir hún það sem er fyrir neðan
        while val!="3":
            d5_tel=d5_tel+1#til þess að telja hversu oft notandinn er búinn að gera þennan lið
            #Þetta passar að ef þú ert að fara í þetta aftur þá resettast þetta
            tel=0
            tala_1_D5=0
            summa=0
            #Hérna fyrir neðan er valmyndin fyrir lið 5
            print ("Sláðu inn 1 ef þú vilt finna summu tíu talna")
            print ("Sláðu inn 2 ef þú vilt athuga hvort tala sé slétt tala eða odda tala")
            print ("Sláðu inn 3 ef þú vilt hætta í forritinu")
            val=input("------------------------------------------> ")
            if val=="1":#Hérna fer notandinn ef hann velur 1
                #Til þess að þurfa ekki að gera hverja og eina spurningu
                while tel!=10:
                    tel=tel+1
                    tala_1_D5=int(input("Sláðu inn tölu "+str(tel)+" "))
                    summa=summa+tala_1_D5
                #Útreykningar til þess að finna summuna
                medaltal=summa/tel
                #Úttak
                print("Summa talnana er",summa)
                print("meðaltal talnana er",medaltal,"\n\n")
            elif val=="2":#Hérna fer notandinn ef hann velur 2
                tala_2_D5=int(input("Sláðu inn tölu til þess að sjá hvort hún er slétt tala eða odda tala "))
                if tala_2_D5%2==0:#Hérna fer notandinn ef það er hægt að deila töluni með 2 og afgangurinn er 0
                    print("Talan er slétttala\n\n")
                elif tala_2_D5%2==1:#Hérna fer notandinn ef það er ekki hægt að deila tölunni með fimm og fá 0 í afgang
                    print("Talan er oddatala\n\n")
                else:#Error skilaboð en ég held að það sé ekki hægt að triggera þau, maður veit samt aldrei
                    print("ERROR\n\n")
            elif val=="3":#Hérna fer notandinn ef hann velur 3
                tel=0#til þess að telarinn byrji á réttum stað
                #Til þess að þurfa ekki að skrifa 10 sinnum "print("Ég er frábær forritari")"
                while tel!=10:
                    tel=tel+1
                    print("Ég er frábær forritari")
                print("Þú ert búinn að gera þetta dæmi",d5_tel,"sinnum\n\n")

    #Liður 6
    elif val=="6":#Ef val er sex gerir hún það sem er fyrir neðan
        print("Efri kóðin telur frá einum og upp í tíu vegna þess að plús einn er eftir að while loopan kemur en samt áður en\nprint svo að þetta er 0 þegar þetta fer í gegn um while loopuna en þegar print skypunin kemur er þetta 1 og þegar\n þetta er níu fer þetta í gegnum while loopuna svo er +1 og svo print svo að þetta er 10 í print og stoppar svo á\nwhile loopuni næst.")
        print()
        print("Neðri kóðinn byrjar á að prenta þrjá vegna þess að það byrjar á einum og svo eftir while loopuna en á undan print\ner gert +2 en þessi loopa stoppar aldrei því að þetta á að halda áfram ámeðan i er ekki 10 en i verður aldrei 10\nvegna þess að þetta er +2 og hoppar á oddatölum svo að þetta mun hoppa yfir 10\n\n")

    #til þess að þegar maður ýtir á sjö, til þess að loka forritinu komi ekki "ERROR	Sláðu inn 1, 2, 3, 4, 5, 6 eða 7"
    elif val=="7":
        pass
    
    else:
        print("ERROR\tSláðu inn 1, 2, 3, 4, 5, 6 eða 7\n\n")

