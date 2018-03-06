'''
Skilaverkefni 2 föll
Hrólfur Gylfason
02/02/2018
'''

import random#Ég importaði random efst í staðin fyrir að importa í hverju dæmi sem ég nota random í vegna þess að eitt fallið mitt notar random og þá munu allir notendur fara í gegnum fallið í byrjun og þurfa þá að vera búnir að importa random

#Dæmi 1
def reiknaFarenheit(celsius):#Þetta fall tekur inn celsius, margfaldar því með 3.785, bætir svo við 32 og skilar því svo og þá er búið að breyta því í farenheit
    farenheit_out = celsius * 1.8 + 32
    return farenheit_out

def reiknaCelsius(farenheit):#Þetta fall tekur inn celsius, deilir því með 3.785, dregur svo frá 32 og skilar því svo og þá er búið að breyta því í celsius
    celsius_out = (farenheit - 32) / 1.8
    return celsius_out

#Dæmi 2
def reiknaKelvinD2(celsius):#Þetta fall tekur inn celsius, bætir við það 273.15 og skilar því svo og þá er búið að breyta því í kelvin
    kelvin_out = celsius + 273.15
    return kelvin_out

def reiknaCelsiusD2(kelvin):#Þetta fall tekur inn kelvin, dregur frá því 273.15 og skilar því svo og þá er búið að breyta því í celsius
    celsius_out = kelvin - 273.15
    return celsius_out

#Dæmi 3
def reiknaVeldi(tala,veldi):#Þetta fall tekur inn tölu og veldi og marfaldar tölunna jafn oft með sjálfri sér og veldið er hátt og skilar því
    utkoma = 1
    for tel in range(veldi):
        utkoma *= tala
    return utkoma

#Dæmi 4
def reiknaSentinetra(tommur):#Þetta fall tekur inn tommur, deilir því með 2.54 og skilar því svo og þá er búið að breyta því í sentímetra
    sentimetrar_out = tommur / 2.54
    return sentimetrar_out

def reiknaTommur(sentimetrar):#Þetta fall tekur inn sentimetra, margfaldar því með 2.54 og skilar því svo og þá er búið að breyta því í tommur
    tommur_out = sentimetrar * 2.54
    return tommur_out

#Dæmi 5
def reiknaLítra(gallon):#Þetta fall tekur inn gallon, margfaldar því með 3.785 og skilar því svo og þá er búið að breyta því í lítra
    gallon_out = lítrar * 3.785
    return gallon_out

def reiknaGallon(litrar):#Þetta fall tekur inn lítra, deilir því með 3.785 og skilar því svo og þá er búið að breyta því í gallon
    litrar_out = gallon / 3.785
    return litrar_out
#Dæmi 6
def heilsa(nafn,kyn):#Þetta fall tekur inn nafn og kyn og prenntar svo út Sæll og blessaður eða sæl og blessuð eftir kyni
    if kyn == "kk":
        print("Sæll og blessaður",nafn)

    elif kyn == "kvk":
        print("Sæl og blessuð",nafn)

#Dæmi 7
def kasta():#Þetta fall tekur ekkert inn og skilar svo random tölu á milli 1 og 6
    return random.randint(1,6)

#Dæmi 8
def talnaleit(listi1,listi2):#Þetta fall tekur inn tvo lista, ber þá svo saman með tveimur for lúppum, býr til einn lista sem er með tölum sem eru á báðum listunum og returnar honum svo
    sameginlegt = []

    for tala1 in listi1:
        for tala2 in listi2:
            if tala1 == tala2:
                sameginlegt.append(tala1)

    return sameginlegt        

valmynd = ""#Hérna bý ég til breytuna valmynd

while valmynd != "9":#Þetta lætur dæmið gerast aftur og aftur þangað til að það er ýtt á 9 til þess að hætta

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að breyta á milli Celsius og Farenheit")
    print("Ýttu á 2 til þess að breyta á milli Kelvin og Celsius")
    print("Ýttu á 3 til þess að reikna veldi")
    print("Ýttu á 4 til þess að breyta á milli tomma og sentimetra")
    print("Ýttu á 5 til þess að breyta á milli gallon og lítra")
    print("Ýttu á 6 til þess að vera heilsað eftir kyni")
    print("Ýttu á 7 til þess að kasta teningi")
    print("Ýttu á 8 til þess að  leita að sömu tölu í tveimur listum")
    print("Ýttu á 9 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        print("Sláðu inn 1 ef þér langar að breyta úr celsius í farenheit")
        print("Sláðu inn 2 ef þér langar að breyta úr farenheit í celsius")
        val_D1 = input("---------->>> ")#Hérna velur notandinn hvort hann vilji breyta úr celsius í farenheit eða öfugt

        print()#Hérna er enter til þess að skilja að valmyndina í þessu dæmi og restina af dæminu

        if val_D1 == "1":#Hérna breyti ég celsius í farenheit
            celsius = int(input("Sláðu inn gráður í celsius "))#Hérna slær notandinn inn gráður í celsius
            print()#Hérna er enter til þess að skilja að staðinn þar sem notandinn slær inn upplýsingarnar og niðurstöðurnar til þess að það sé auðveldara að lesa niðurstöðurnar
            print(celsius,"gráður celsius eru",round(reiknaFarenheit(celsius),1),"gráður farenheit")#Hérna prennta ég út reiknaFarenheit og seti celsius inn í svigan til þess að gefa fallinu breytuna til þess að vinna með

        elif val_D1 == "2":#Hérna breyti ég farenheit í celsius
            farenheit = int(input("Sláðu inn gráður í farenheit "))#Hérna slær notandinn inn gráður í farenheit
            print()#Hérna er enter til þess að skilja að staðinn þar sem notandinn slær inn upplýsingarnar og niðurstöðurnar til þess að það sé auðveldara að lesa niðurstöðurnar
            print(farenheit,"gráður farenheit eru",round(reiknaCelsius(farenheit),1),"gráður celsius")#Hérna prennta ég út reiknaCelsius og seti farenheit inn í svigan til þess að gefa fallinu breytuna til þess að vinna með

    elif valmynd == "2":#Liður 2
        print("Sláðu inn 1 ef þér langar að breyta úr celsius í kelvin")
        print("Sláðu inn 2 ef þér langar að breyta úr kelvin í celsius")
        val_D2 = input("---------->>> ")#Hérna velur notandinn hvort hann vilji breyta úr celsius í kelvin eða öfugt

        print()#Hérna er enter til þess að skilja að valmyndina í þessu dæmi og restina af dæminu

        if val_D2 == "1":#Hérna breyti ég celsius í kelvin
            celsius = int(input("Sláðu inn gráður í celsius "))#Hérna slær notandinn inn gráður celsius
            print()#Hérna er enter til þess að skilja að staðinn þar sem notandinn slær inn upplýsingarnar og niðurstöðurnar til þess að það sé auðveldara að lesa niðurstöðurnar
            print(celsius,"gráður celsius eru",round(reiknaKelvinD2(celsius),1),"gráður kelvin")#Hérna prennta ég út reiknaKelvinD2 og seti celsius inn í svigan til þess að gefa fallinu breytuna til þess að vinna með

        elif val_D2 == "2":#Hérna breyti ég kelvin í celsius
            kelvin = int(input("Sláðu inn gráður í kelvin "))#Hérna slær notandinn inn gráður í kelvin
            print()#Hérna er enter til þess að skilja að staðinn þar sem notandinn slær inn upplýsingarnar og niðurstöðurnar til þess að það sé auðveldara að lesa niðurstöðurnar
            print(kelvin,"gráður kelvin eru",round(reiknaCelsiusD2(kelvin),1),"gráður celsius")#Hérna prennta ég út reiknaCelsiusD2 og seti kelvin inn í svigan til þess að gefa fallinu breytuna til þess að vinna með
        
    elif valmynd == "3":#Liður 3
        tala = int(input("Sláðu inn tölu "))#Hérna tek ég inn tölu og nota int() til þess að geta reiknað með hana seinna
        veldi = int(input("Sláðu inn veldi "))#Hérna tek ég inn veldi og nota int() til þess að geta reiknað með hana seinna

        print()#Hérna er enter til þess að skilja að staðinn þar sem notandinn slær inn upplýsingarnar og niðurstöðurnar til þess að það sé auðveldara að lesa niðurstöðurnar

        print(tala,"í",veldi,"veldi er",reiknaVeldi(tala,veldi))#Hérna prenta ég fallið reiknaVeldi og seti tala og veldi breyturnar inn í sviga þess til þess að gefa fallinnu þessar breytur til þess að vinna með

    elif valmynd == "4":#Liður 4
        print("Sláðu inn 1 ef þér langar að breyta úr tommum í sentimetra")
        print("Sláðu inn 2 ef þér langar að breyta úr sentimetrum í tommur")
        val_D3 = input("---------->>> ")#Hérna velur notandinn hvort hann vilji breyta úr tommum í sentímetra eða öfugt

        print()#Hérna er enter til þess að skilja að valmyndina í þessu dæmi og restina af dæminu

        if val_D3 == "1":#Hérna breyti ég tommum í sentímetra
            tommur = int(input("Sláðu inn tommur "))#Hérna slær notandinn inn tommur
            print()#Hérna er enter til þess að skilja að staðinn þar sem notandinn slær inn upplýsingarnar og niðurstöðurnar til þess að það sé auðveldara að lesa niðurstöðurnar
            print(tommur,"tommur eru",round(reiknaTommur(tommur),2),"sentimetrar")#Hérna prennta ég út reiknaTommur og seti tommur inn í svigan til þess að gefa fallinu breytuna til þess að vinna með

        elif val_D3 == "2":#Hérna breyti ég sentímetrum í tommur
            sentimetrar = int(input("Sláðu inn sentimetra "))#Hérna slær notandinn inn sentímetra
            print()#Hérna er enter til þess að skilja að staðinn þar sem notandinn slær inn upplýsingarnar og niðurstöðurnar til þess að það sé auðveldara að lesa niðurstöðurnar
            print(sentimetrar,"sentimetrar eru",round(reiknaSentinetra(sentimetrar),2),"tommur")#Hérna prennta ég út reiknaSentimetra og seti sentimetrar inn í svigan til þess að gefa fallinu breytuna til þess að vinna með
        
    elif valmynd == "5":#Liður 5
        print("Sláðu inn 1 ef þér langar að breyta úr gallonum í lítra")
        print("Sláðu inn 2 ef þér langar að breyta úr lítrum í gallon")
        val_D3 = input("---------->>> ")#Hérna velur notandinn hvort hann vilji breyta úr gallonum í lítra eða öfugt

        print()#Hérna er enter til þess að skilja að valmyndina í þessu dæmi og restina af dæminu

        if val_D3 == "1":#Hérna breyti ég gallon í lítra
            gallon = int(input("Sláðu inn gallon "))#Hérna slær notandinn inn gallon
            print()#Hérna er enter til þess að skilja að staðinn þar sem notandinn slær inn upplýsingarnar og niðurstöðurnar til þess að það sé auðveldara að lesa niðurstöðurnar
            print(gallon,"gallon eru",round(reiknaLítra(gallon),2),"lítrar")#Hérna prennta ég út reiknaLítra og seti gallon inn í svigan til þess að gefa fallinu breytuna til þess að vinna með

        elif val_D3 == "2":#Hérna breyti ég lítrum í gallon
            litrar = int(input("Sláðu inn lítra "))#Hérna slær notandinn inn lítra
            print()#Hérna er enter til þess að skilja að staðinn þar sem notandinn slær inn upplýsingarnar og niðurstöðurnar til þess að það sé auðveldara að lesa niðurstöðurnar
            print(litrar,"lítrar eru",round(reiknaGallon(litrar),2),"gallon")#Hérna prennta ég út reiknaGallon og seti litrar inn í svigan til þess að gefa fallinu breytuna til þess að vinna með

    elif valmynd == "6":#Liður 6
        nafn = input("Sláðu inn nafnið þitt ")#Hérna tek ég inn nafn notandans
        kyn = input("Sláðu inn kk ef þú ert karlkyns eða kvk ef þú ert kvennkyns ").lower()#Hérna tek ég inn nafn notandans og breyti því öllu í lágstafi með .lower()

        heilsa(nafn,kyn)#Hérna hef ég ekki print utanum vegna þess að í fallinu er print skipun en ekki return skipun svo að þá þarf ég ekki að hafa print skipun hérna

    elif valmynd == "7":#Liður 7
        print(kasta())#Hérna prennta ég út það sem kemur úr fallinu kasta

    elif valmynd == "8":#Liður 8
        listi1 = []#Hérna bý ég til listann listi1
        listi2 = []#Hérna bý ég til listann listi2

        for tel in range(25):#Þessi lúppa gerist 25 sinnum til þess að setja 25 random tölur á listann listi1
            random_tala = random.randint(0,99)#Þetta bér til random tölu og setir hana í breytuna random_tala
            listi1.append(random_tala)#Þetta bætir tölunni random_tala á listann listi1

        for tel in range(25):#Þessi lúppa gerist 25 sinnum til þess að setja 25 random tölur á listann listi2
            random_tala = random.randint(0,99)#Þetta bér til random tölu og setir hana í breytuna random_tala
            listi2.append(random_tala)#Þetta bætir tölunni random_tala á listann listi1

        for tala in talnaleit(listi1,listi2):#Þessi lúppa prentar út listann sem kemur frá fallinu talnaleit með kommu á eftir hverri tölu
            print(tala,end=", ")
        print()#Þetta gerir eitt enter svo að aðskilnaðar strikin sem skilja að valmyndina og dæmi sem maður gerir fari ekki upp á síðustu tölunna

    elif valmynd == "9":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 9" þegar maður er að hætta í forritinu
        pass

    else:#Þetta gerist ef notandinn slær inn vitlausa tölu eða bókstaf
        print("ERROR\tSláðu inn tölu á milli 1 og 9")
