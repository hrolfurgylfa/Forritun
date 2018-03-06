'''
Hrólfur Gylfason 2017
Skilaverkefni 4
'''
val="0"#Til þess að það komi ekki "NameError: 'val' is not defined"

for tel in range(50):#Þetta er til þess að hreinsa skjáinn áður en þú byrjar að nota forritið
    print("\n")
            
while val!="9":
    print("\n--------------------------------------------------\n")
    print("Ýttu á 1 til þess að skoða lið eitt")
    print("Ýttu á 2 til þess að skoða lið tvö")
    print("Ýttu á 3 til þess að skoða lið þrjú")
    print("Ýttu á 4 til þess að skoða lið fjögur")
    print("Ýttu á 5 til þess að skoða lið fimm")
    print("Ýttu á 6 til þess að skoða lið sex")
    print("Ýttu á 7 til þess að skoða lið sjö")
    print("Ýttu á 8 til þess að skoða lið átta")
    print("Ýttu á 9 til þess að hætta")
    val=input("-------------------------------------> ")
    #Þetta er til þess að gera greinaskil, það tekur aðeins minna pláss að gera bara print og skrifa svo "-" 50 sinnum
    #en þá er ekki jafn auðvelt að breyta magninu af bandstrikunum
    print()
    for tel in range(50):
        print("-", end="")
    print()
    
    if val=="1":
        tala=int(input("Sláðu inn heiltölu "))#Hérna skrifar notandinn hvaða tölu hann langar að sjá
        h_oft=int(input("Hversu oft á að skrifa út töluna? "))#Hérna velur notandinn hversu oft honum langar að sjá töluna
        for tel in range(h_oft):#For lúppa
            print(tala, end=" ")#end er til þess að þetta komi allt í línu
            
    elif val=="2":
        for tel in range(2, 15, 2):#For lúppa sem prentar út tel sem byrjar á tvem, hoppar um 2 og fer svo ekki upp í 15
            print(tel, end=" ")#end er til þess að þetta komi allt í línu

    elif val=="3":
        tala_1=int(input("Sláðu inn fyrri heiltöluna "))
        tala_2=int(input("Sláðu inn seinni heiltöluna "))
        if tala_1>tala_2:#Þetta if og else er til þess að það sé hægt að prenta tölur sem fara niður
            for tel in range(tala_1, tala_2-1,-1):#for setning sem telur afturábak
                print(tel, end=" ")#end er til þess að þetta komi allt í línu
        else:
            for tel in range(tala_1, tala_2+1):#for setning sem telur áfram
                print(tel, end=" ")#end er til þess að þetta komi allt í línu

    elif val=="4":
        #Hérna er input fyrir notandann
        byrjun=int(input("Sláðu inn byrjun talnarununar "))
        endi=int(input("Sláðu inn enda talnarununar "))
        hækkun=int(input("Sláðu inn hækkun talnarununar "))
        for tel in range(byrjun, endi, hækkun):#For lúppa sem notar byrjun, endi og hækkun breyturnar
            print(tel, end=" ")#end er til þess að þetta komi allt í línu

    #Hjá mér byrjaði þetta á 101 vegna þess að ef maður hefur þetta gerir þetta eins og í sýnidæminu er maður með 11 í línu og endar með 9 og þrjá fjórðu af línu
    #eða að maður er með 10 línur og endar með 109        
    elif val=="5":
        tel2=100#til þess að þetta byrji ekki á 0
        for tel in range(10):#For lúppa sem lætur hina lúppuna gerast 10 sinnum
            for tel2 in range(tel2+1, tel2+11):#Ég gerði +1 til þess að þetta geri ekki sumar tölur tvisvar og +11 til þess að þetta fari alltaf 10 í hverri línu
                print(tel2, end=" ")#end er til þess að þetta komi allt í línu
            print()#Þetta er til þess að forritið skipti um línu eftir 10 tölur

    elif val=="6":
        summa=1#Þetta er til þess að það sé hægt að komast upp, ef ég myndi segja summa=0 væri summa alltaf 0 vegna þess að hvaða tala sem er sinnum 0 er alltaf 0
        tala=int(input("Sláðu inn heiltölu "))#Input fyrir notandann
        for tel in range(tala, 0, -1):#For lúppa
            summa=summa*tel#Þetta margfaldar saman í hvert sinn sem lúppan gengur
            if tel<2:#Þessi if setning lætur forritið fara annað ef þetta er síðasta talan (1) til þess að það komi ekki * eftir einn
                print(tel, end="=")
            else:
                print(tel, end="*")
        print(summa, end="")#Hérna prenta ég summuna og segi forritinu að gera ekki enter í lokin vegna þess að þá lítur þetta betur út vegna þess að enterið kemur seinna

    elif val=="7":
        strengur="*"#Hérna bý ég til streng sem ég bæti svo við seinna
        tala=int(input("Sláðu inn tölu á milli 1 og 9 "))# Input fyrir notanda
        for tel in range(tala):#Hérna er forlúppa sem gengur jafn oft og notandinn skráði að ofan
            print(strengur)#Hérna prenta ég út það sem var komið af "*"
            strengur=strengur+"*"#Hérna bæti ég við einni "*" og svo gerist lúppan aftur

#Í þessu dæmi var lausnin mín að minnka og minka það sem ég tók, ég byrjaði þá væntanlega á því að sjá hvort hún væri deilanleg með 400 og ef hún var prenta þá út að
#þetta væri hlaupár, svo tók ég sæst stærstu töluna sem var 100 og ef hún var deilanleg með hundrað prentaði ég út að þetta væri ekki hlaupár, svo tók ég 4 og ef hún var
#deilanleg með 4 prentaði ég að þetta væri hlaupár og svo ef þetta hafði ekki verið gripið af netunum fyrir ofan prentaði ég að þetta væri ekki hlaupár. Vonandi útskýrði ég
#þetta nógu vel svo þú ruglist ekki aftur á þessu dæmi :)
    elif val=="8":
            ar=int(input("Sláðu inn ár "))
            if ar % 400==0:#Hérna er fyrsta netið þar sem ég stoppa töluna ef hún er deilanleg með 400
                print("Þetta ár er hlaupár")
            elif ar % 100==0:#Hérna er annað netið þar sem ég stoppa töluna ef hún er deilanleg með 100
                print("Þetta ár er ekki hlaupár")
            elif ar % 4:#Hérna er þriðjað netið þar sem ég stoppa töluna ef hún er deilanleg með 4
                print("Þetta ár er hlaupár")
            else:#Hérna fer talan svo ef hún datt ekki í neitt af netunum að ofan
                print("Þetta ár er ekki hlaupár")

    elif val=="9":
        for tel in range(50):#Þetta er til þess að hreinsa skjáinn þegar þú hættir í forritinu
            print("\n")

    else:
        print("ERROR\trangur innsláttur")
