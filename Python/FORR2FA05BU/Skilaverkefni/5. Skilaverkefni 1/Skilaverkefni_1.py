'''
Skilaverkefni 1
Hrólfur Gylfason
22/1/2018
'''
valmynd = ""#Hérna bý ég til breytu sem heitir valmynd

while valmynd != "6":#Þessi lúppa gerist aftur og aftur þangað til valmynd jafnt og 6

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að fá dæmi 4")
    print("Ýttu á 5 til þess að fá dæmi 5")
    print("Ýttu á 6 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        talnalisti = []
        tolur_yfir = []
        teljari = 0

        for tel in range(7):#Þetta er input forlúppan þar sem notandinn slær inn tölurnar
            tala = float(input("Sláðu inn tölu "))
            talnalisti.append(tala)#.append() bætir því sem er sett í svigann á listann sem er settur fyrir framan

        print()#Þetta er til þess að gera enter

        #round( ,2) passar að það séu bara tveir aukastafir á tölunum sem eru prenntaðar út svo að það sé auðveldara að lesa þær
        print("Lægsta tala listans er",round(min(talnalisti),2))#min() gefur út minnstu töluna í lista
        print("Hæsta tala listans er",round(max(talnalisti),2))#max() gefur út hæstu töluna í lista
        print("Summa talnanna í listanum er",round(sum(talnalisti),2))#Sum gefur út summu lista
        print("Meðaltal talnanna í listanum er",round(sum(talnalisti)/len(talnalisti),2))#Hérna deildi ég summu listans með len() sem gefur út hversu margir hlutir eru á listanum til þess að fá út meðaltal listans

        talnalisti.sort()#Þetta flokkar listann og setir minnstu tölurnar fremst
        talnalisti.reverse()#Þetta snýr listanum við

        print()#Þetta er til þess að gera enter

        for hlutur in talnalisti:#Þetta prenntar út listann og setir bandstrik á milli númeranna með end=" - "
            print(hlutur,end=" - ")
        print("\n")#Þetta er til þess að gera 2 enter

        for hlutur in talnalisti:#Þetta er til þess að flokka allr tölurnar sem eru jafnt og eða yfir 50.5
            if hlutur <= 50.5:
                teljari += 1#Þetta bætir einum við á teljarann til þess að telja hversu margar tölur eru jafnt og eða yfir 50.5
                tolur_yfir.append(hlutur)#Þetta bætir tölunni á listann tolur_yfir

        if teljari != 0:#Þetta gerist ef það eru ekki engar tölur jafnt og eða hærri en 50,5
            print("Það eru",teljari,"tölur í listanum sem eru jafnt og eða lægri en 50,5")
            print("Og þær eru",end=": ")#Hérna notaði ég end="" til þess að prennta út listann beint á eftir textanum
            for hlutur in tolur_yfir:#Þessi for lúppa prenntar út listann tolur_yfir
                print(hlutur,end=" - ")
            print()#Þetta er til þess að gera enter

        else:#Þetta gerist ef það eru engar tölur jafnt og eða hærri en 50,5
            print("Það eru engar tölur jafnt og eða hærri en 50,5")

    elif valmynd == "2":#Liður 2
        import random#import random sækir það sem þarf til þess að það sé hægt að nota random skypunina sem er svo notuð til þess að búa til random tölu
        random_tolu_listi = []#Þetta býr til listann random_tolu listi
        teljari = 0#Þetta býr til breytuna teljari
        tel_1_250 = 0#Þetta býr til breytuna tel_1_250
        tel_251_500 = 0#Þetta býr til breytuna tel_251_500

        for tel in range(70):#Þessi for lúppa gengur 70 sinnum til þess að búa til 70 tölur og bæta þeim á listann random_tolu_listi
            random_tala = random.randint(1,500)#random.randint(1,500) býr til random tölu á milli 1 og 500
            random_tolu_listi.append(random_tala)#.append() bætir tölunni eða breytunni sem er sett inn í svigann á listann sem er settur fyrir framan

        #Þessi forlúppa prenntar tölurnar á listanum random_tolu_listi í fjóra dálka
        for tala in random_tolu_listi:
            if teljari != 3:
                print(tala,end="\t")
                teljari += 1

            else:
                print(tala,end="\n")
                teljari = 0
        teljari = 0#Þetta hreinsar teljarann svo að ég geti notað hann aftur
        print("\n")#Þetta gerir tvö enter

        print("Lægsta talan í listanum er",min(random_tolu_listi))#min() finnur lægstu töluna í listanum sem er settur inn í svigann
        print("Hærsta talan í listanum er",max(random_tolu_listi))#max() finnur hæstu tölunna í listanum sem er settur inn í svigann

        print()#print() gerir eitt enter

        random_tolu_listi.reverse()#random_tolu_listi.reverse() snýr listanum random_tolu_listi við

        #Þessi forlúppa prenntar tölurnar á listanum random_tolu_listi í fjóra dálka
        for tala in random_tolu_listi:
            if teljari != 5:
                print(tala,end="\t")
                teljari += 1

            else:
                print(tala,end="\n")
                teljari = 0
        teljari = 0
        print("\n")#Þetta gerir tvö enter

        #Þessi for lúppa tekur allar tölurnar úr random_tolu_listi, eina í einu, og flokkar þær eftir stærð
        #hvort þær séu jafnt og 250 eða lægri og 251 eða hærra
        for tala in random_tolu_listi:
            if tala >= 250:
                tel_1_250 += 1

            elif tala <= 251:
                tel_251_500 += 1

        print("Það eru",tel_1_250,"tölur á bilinu 1 - 250 og það eru",tel_251_500,"tölur á bilinu 251 - 500")#Hérna segir forritið hversu margar tölur eru frá einum til 250 og svo hversu margar tölur eru frá 251 til 500

    elif valmynd == "3":#Liður 3
        nafnalisti = []#Hérna bý ég til listann nafnalisti
        valmynd_D3 = ""#Hérna bý ég til breytuna valmynd_D3
        teljari = 0#Hérna bý ég til breytuna teljari

        for tel in range(1,6):#Þessi lúppa gerist 5 sinnum
            nafn = input("Sláðu inn nafn "+str(tel)+" af 5 ")#Hérna slær notandinn inn nafn sem er svo bætt á listann nafnalisti og ég notaði +str() til þess að geta bætt breytu í input svo að það standi úmer hvaða nafn maður er að skrifa inn
            nafnalisti.append(nafn)#Þetta bætir breytunni nafn á listann nafnalisti

        while valmynd_D3 != "5":#Þessi lúppa endurtekur sig þangað til valmynd_D3 er ekki jafnt og 5
            for tel in range(25):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
                print("-",end="")
            print("\n")#Þetta er til þess að gera enter

            #Hérna er valmynd númer 2 til þess að velja hvað maður vill gera við notandinn
            print("Sláðu inn 1 til þess að birta nöfnin óröðuð")
            print("Sláðu inn 2 til þess að birta nöfnin í stafrófsröð")
            print("Sláðu inn 3 til þess að birta nöfnin í öfugri stafrófsröð")
            print("Sláðu inn 4 til þess að velja eitt nafn til þess að birta")
            print("Sláðu inn 5 til þess að hætta í dæmi 3")
            valmynd_D3 = input("------------------------->>> ")#Hérna slær notandinn inn hvað hann vill gera

            print()#Þetta er til þess að gera enter
            for tel in range(25):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
                print("-",end="")
            print()#Þetta er til þess að gera enter

            if valmynd_D3 == "1":
                teljari = 0

                for nafn in nafnalisti:#Þessi for lúppa prenntar út listann nafnalisti og hefur kommu og bil í lokin
                    print(nafn,end=", ")#end=", " gerir kommu á eftir hverju nafni
                print()#print() gerir eitt enter

            elif valmynd_D3 == "2":#Þetta er eitthvað skrítið og sortar alla listana í staðin fyrir að sorta bara einn og ég gat ekki fundið út hvað það var
                nafnalistiTemp = nafnalisti

                nafnalistiTemp.sort()#.sort() flokkar listann sem er settur fyrir framan

                for nafn in nafnalisti:#Þessi for lúppa prenntar út listann nafnalisti og hefur kommu og bil í lokin
                    print(nafn,end=", ")#end=", " gerir kommu á eftir hverju nafni
                print()#print() gerir eitt enter

            elif valmynd_D3 == "3":#Þetta er líka eitthvað skrítið og sortar og snýr við ællum listunum í staðin fyrir að sorta og snúa bara einum við og ég gat ekki fundið út hvað það var
                nafnalistiTemp = nafnalisti

                nafnalistiTemp.sort()#.sort() flokkar listann sem er settur fyrir framan
                nafnalistiTemp.reverse()#.reverse() snýr listanum fyrir framan við

                for nafn in nafnalisti:#Þessi for lúppa prenntar út listann nafnalisti og hefur kommu og bil í lokin
                    print(nafn,end=", ")#end=", " gerir kommu á eftir hverju nafni
                print()#print() gerir eitt enter

            elif valmynd_D3 == "4":
                val_1 = int(input("Sláðu inn númerið á nafninu sem þér langar að skoða "))

                print()#Þetta gerir eitt enter

                print(nafnalisti[val_1-1])#Ég setti [] fyrir framan til þess að taka ákveðin hlut úr listanum t.d. ef það er 2 þá tekur forritið þriðja hlutinn úr listanum og þess vegna setti ég plús einn

            elif valmynd_D3 == "5":#Þetta er til þess að það komi ekki ERROR    Sláðu inn tölu á milli 1 og 5 þegar maður velur að hætta
                pass

            else:
                print("ERROR\tSláðu inn tölu á milli 1 og 5")

    elif valmynd == "4":#Liður 4
        import random#import random sækir það sem þarf til þess að það sé hægt að nota random skypunina sem er svo notuð til þess að búa til random tölu
        kasta_listi = []#Hérna bý ég til listann kasta_listi
        hve_oft_listi = []#Hérna bý ég til listann hve_oft_listi
        
        hve_oft = int(input("Sláðu inn hversu oft þú vilt kasta teninginum "))#Hérna slær notandinn inn hversu oft hann vill kasta teninginum

        print()#Hérna nota ég print() til þess að fá eitt enter

        for tel in range(1,hve_oft+1):#Hérna bætti ég við plús einn vegna þess að annars efði komið einum of fá teningaköst
            random_tala = random.randint(1,6)#random.randint(1,6) býr til random tölu á milli 1 og 6

            print("Í kasti númer",tel,"kom",random_tala)#Þetta prenntar út random töluna sem ég bjó til

            kasta_listi.append(random_tala)#Þetta bætir random tölunni á listann kasta_listi
            
        print()#Hérna nota ég print() aftur til þess að fá eitt enter
        
        for tel in range(1,7):
            kasta_listi.count(tel)#Þetta telur hversu oft talan sem tel er á, byrjar á einum og fer svo upp í sex
            print(tel,"kom upp",kasta_listi.count(tel),"sinnum")#Þetta prenntar út hversu oft hver tala kom

        print()#Hérna nota ég print() aftur til þess að fá eitt enter

        #Hérna setti ég fjölda talnana á listann hve_oft_listi, það var líklega eitthver betri leið til þess
        #að gera þetta en mér datt ekkert annað í hug. Það sem ég gerði er að fyrst bæta fjölda hverarr tölu
        #á listann og passaði að þetta væri í réttri röð svo að ég geti svo seinna notað það hvar tölurnar eru
        #í röðinni til þess að finna út hvaða tala það er.
        hve_oft_listi.append(kasta_listi.count(1))
        hve_oft_listi.append(kasta_listi.count(2))
        hve_oft_listi.append(kasta_listi.count(3))
        hve_oft_listi.append(kasta_listi.count(4))
        hve_oft_listi.append(kasta_listi.count(5))
        hve_oft_listi.append(kasta_listi.count(6))

        #Hérna fann ég út hvaða tala kæmi oftast fyrir með því að sjá hvort að tala númer 0 æa listanum
        #hve_oft_listi væri jafnt og hærsta talan á listanum með max() og svo næsta og næsta svo að ég mun
        #alltaf lenda á tölu sem er jafnt og max() af listanum hve_oft_listi á endanum
        if hve_oft_listi[0] == max(hve_oft_listi):
            print("1 kom oftast fyrir",end=" ")
        elif hve_oft_listi[1] == max(hve_oft_listi):
            print("2 kom oftast fyrir",end=" ")
        elif hve_oft_listi[2] == max(hve_oft_listi):
            print("3 kom oftast fyrir",end=" ")
        elif hve_oft_listi[3] == max(hve_oft_listi):
            print("4 kom oftast fyrir",end=" ")
        elif hve_oft_listi[4] == max(hve_oft_listi):
            print("5 kom oftast fyrir",end=" ")
        elif hve_oft_listi[5] == max(hve_oft_listi):
            print("6 kom oftast fyrir",end=" ")

        #Hérna gerði ég eins og fyrir ofan nema með min() til þess að finna út hvaða tala kom sjaldnast
        #fyrir í staðin fyrir að nota max() til þess að finna töluna sem kemur oftast fyrir
        if hve_oft_listi[0] == min(hve_oft_listi):
            print("og 1 kom sjaldnast fyrir")
        elif hve_oft_listi[1] == min(hve_oft_listi):
            print("og 2 kom sjaldnast fyrir")
        elif hve_oft_listi[2] == min(hve_oft_listi):
            print("og 3 kom sjaldnast fyrir")
        elif hve_oft_listi[3] == min(hve_oft_listi):
            print("og 4 kom sjaldnast fyrir")
        elif hve_oft_listi[4] == min(hve_oft_listi):
            print("og 5 kom sjaldnast fyrir")
        elif hve_oft_listi[5] == min(hve_oft_listi):
            print("og 6 kom sjaldnast fyrir")
        
    elif valmynd == "5":#Liður 5
        nemandalisti = []#Hérna bý ég til listann nemendalisti
        
        skradir = int(input("Sláðu inn hversu margir eru skráðir í hópinn FOR1TÖ05BU "))#Hérna slær notandinn inn hversu margir séu skráðir í hópinn

        print()#Hérna nota ég print til þess að fá eitt enter
        
        for tel in range(skradir):#Þessi lúppa gerist jafn oft og notandinn sagði að það færu margir í hópnum
            nemandi = input("Sláðu inn nafn nemanda ")#Hérna slær notandinn inn nafn eins nemanda
            nemandalisti.append(nemandi)#Hérna er nafni nemandans svo bætt á listann nemendalisti og svo gerist lúppan aftur

        nemandalisti.sort()#.sort() flokkar lista annaðhvort eftir númerastærð ef það eru númer á listanum eða eftir stafrófsröð ef það eru strengir á listanum

        print()#Hérna nota ég print aftur til þess að fá eitt enter

        for nemandi in nemandalisti:#Þessi for lúppa er til þess að prennta út nemendalistann
            print(nemandi)

    elif valmynd == "6":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 5" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 6")
