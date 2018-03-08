'''
Skilaverkefni 3
Hrólfur Gylfason
24/2/2018
'''
import random
from random import shuffle

def prentaTuple(tup):
    for nafn in tup:
        print(nafn,end=" ")

def paraTuple(tup1,tup2):
    for x in range(len(tup1)):
        print(tup1[x],"og",tup2[x])

def paraRandom(tup1,tup2):
    for tel in range(len(tup1)):
        randomStrakur = random.randint(0,len(tup1)-1)
        randomStelpa = random.randint(0,len(tup2)-1)

        print(tup1[randomStelpa],"og",tup2[randomStrakur])

def paraRandomStakur(tup1,tup2):
    listi1 = []
    listi2 = []

    for nafn in tup1:
        listi1.append(nafn)

    for nafn in tup2:
        listi2.append(nafn)

    shuffle(listi1)
    shuffle(listi2)

    for x in range(len(tup1)):
        print(listi1[x],"og",listi2[x])

def finnaNafn(stafur,tup1,tup2):
    nafnaleit = []

    for nafn in tup1:
        for stafur_i_nafni in nafn:
            if stafur_i_nafni.lower() == stafur.lower():
                nafnaleit.append(nafn)
                break

    for nafn in tup2:
        for stafur_i_nafni in nafn:
            if stafur_i_nafni.lower() == stafur.lower():
                nafnaleit.append(nafn)
                break

    return nafnaleit

def finnaNafnUpphafsstafur(stafur,tup1,tup2):
    nafnaleit = []

    for nafn in tup1:
        if nafn[0].lower() == stafur.lower():
            nafnaleit.append(nafn)

    for nafn in tup2:
        if nafn[0].lower() == stafur.lower():
            nafnaleit.append(nafn)

    return nafnaleit

def finnaNN(tup1,tup2):
    nn_Listi = []
    n_counter = 0

    for nafn in tup1:
        for stafur in nafn:
            if stafur == "n".lower():
                n_counter += 1

            else:
                n_counter = 0

            if n_counter == 2:
                nn_Listi.append(nafn)
                break
    
    for nafn in tup2:
        for stafur in nafn:
            if stafur == "n".lower():
                n_counter += 1

            else:
                n_counter = 0

            if n_counter == 2:
                nn_Listi.append(nafn)
                break
    
    return nn_Listi

def simaskra_leit(nafn_leita,dict):
    afram = True#Hérna hef ég True til þess að geta stoppað lúppuna hvenær sem ég vill
    for nafn in simaskra:
        if nafn == nafn_leita:#Þetta gerist ef lúpppan hefur fundið nafnið
            print("Símanúmer þessarar persónu er:",simaskra[x])
            return simaskra[x]#Þetta er ekki notað núna en þetta er ef ég vildi nota þetta í framtíðinni
            afram = False#Hérna er ég búinn að finna símanúmer persónunnar sem var verið að leita að svo að þá þarf bara að stoppa
            break

    if afram == True:#Hérna fer notandinn ef hann sló inn rangt nafn til þess að leita að
        print("Þetta nafn er ekki til í skránni")

def bekkurAllur(dict1):#Þetta fall tekur inn eitt dictionary og prentar það
    for nafn in dict1:
        print(nafn,"---\t---\t---",dict1[nafn])

def sjalfradaLeitari(dict1):#Þetta fall tekur inn dictionary, prentar alla sem eru yfir 18 og gefur svo upp hversu margir það eru
    sjalfradaTeljari = 0

    print("Hérna eru allir sem eru yfir 18:\n")
    for nafn in dict1:
        if dict1[nafn] >= 18:
            sjalfradaTeljari += 1
            print(nafn)
    print("\nÞað eru samtals",sjalfradaTeljari,"í þessum bekk sem eru yfir 18")

def medalaldurDict(dict1):#Þetta fall tekur inn eitt dictionary og skilar svo meðalaldrinum á því dictionary(svo lengi sem aldurinn er sem value á dictionary-inu)
    aldur = []

    for nafn in dict1:
        aldur.append(dict1[nafn])
    
    return round(sum(aldur)/len(aldur),2)

def heildaraldurDict(dict1):#Þetta fall tekur inn eitt dictionary og skilar svo heildaraldrinum á því dictionary(svo lengi sem aldurinn er sem value á dictionary-inu)
    aldur = []

    for nafn in dict1:
        aldur.append(dict1[nafn])

    return sum(aldur)

def leitaDict(dict1):#Þetta fall tekur inn dictionary, býr til copy af því sem dict_temp og eyðir svo öllu útaf því sem byrjar ekki á stafnum sem notandinn valdi
    dict_temp = dict1.copy()
    eyda = []
    leitaStafur = input("Sláðu inn staf sem þér langar að í byrjun nafna nemendana í bekknum: ").upper()

    for nafn in dict_temp:
        if nafn[0] != leitaStafur:
            eyda.append(nafn)

    for nafn in eyda:
        del dict_temp[nafn]
    
    return dict_temp

valmynd = ""

while valmynd != "4":
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Dæmi 1
        dansHerrar = ("Jón","Jonni","Unnbjörn","Daníel","Bent","Þorgeir")
        dansDomur = ("Ingdís","Valey","Hallvör","Ýma","Gerður","Ögmunda")

        prentaTuple(dansHerrar)
        print()
        prentaTuple(dansDomur)       
        print("")

        print("--------------------------------------------------")

        paraTuple(dansHerrar,dansDomur)

        print("--------------------------------------------------")

        paraRandom(dansHerrar,dansDomur)

        print("--------------------------------------------------")

        paraRandomStakur(dansHerrar,dansDomur)

        print("--------------------------------------------------")

        stafur = input("Sláðu inn staf sem þér langar að leita að í nöfnum keppenda: ")
        print()
        for nafn in finnaNafn(stafur,dansHerrar,dansDomur):
            print(nafn,end=", ")
        print()

        print("--------------------------------------------------")

        stafur = input("Sláðu inn staf sem þér langar að leita að í upphafsstöfum keppenda: ")
        print()
        for nafn in finnaNafnUpphafsstafur(stafur,dansHerrar,dansDomur):
            print(nafn,end=", ")
        print()

        print("--------------------------------------------------")

        print('Hérna eru nöfnin með "nn" í þeim: ',end="")
        for nafn in finnaNN(dansHerrar,dansDomur):
            print(nafn,end=", ")
        print()

    elif valmynd == "2":#Dæmi 2
        simaskra = {"Magnús":8405385,"Kristján":8648096,"Stefán":6535365,"Jóhann":6805310,"Björn":6690398,"Elín":6037527,"Guðbjörg":6084992,"Ásta":7702612,"Katrín":7311023,"Ragnheiður":8784670}#Hérna bý ég til dictionary-ið simaskra
        
        nafn = input("Sláðu inn nafn til þess að leita að í símaskránni: ")
        print()#Print er ég að nota til þess að gera enter og það er til þess að gera þetta snirtilegra
        
        simaskra_leit(nafn,simaskra)#Hérna kalla ég á fallið simaskra_leit til þess að leita að nafninu sem notandinn sló inn í dictionary-inu simaskra

    elif valmynd == "3":#Dæmi 3
        bekkur = {"Helgi":17,"Jóhann":19,"Elín":17,"Bjarni":19,"Sveinn":20,"Birgir":17,"Björn":19,"Guðrún":20,"Steinunn":19,"María":19,"Jóhannes":16,"Ingibjörg":20,"Þórunn":18,"Auður":18}
        val_D3 = ""

        while val_D3 != "6":
            for tel in range(30):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
                print("-",end="")
            print("\n")#Þetta er til þess að gera tvö enter

            print("Ýttu á 1 til þess að prennta allan bekkinn")
            print("Ýttu á 2 til þess að prennta alla yfir 18")
            print("Ýttu á 3 til þess að fá meðalaldur bekjarins")
            print("Ýttu á 4 til þess að fá heildaraldur bekjarins")
            print("Ýttu á 5 til þess að prennta alla með eitthverjum upphafsstaf")
            print("Ýttu á 6 til þess að hætta")
            val_D3 = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

            print()#Þetta er til þess að gera enter
            for tel in range(30):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
                print("-",end="")
            print()#Þetta er til þess að gera enter  

            if val_D3 == "1":#Liður 1
                bekkurAllur(bekkur)#Hérna kalla ég í fallið bekkurAllur

            elif val_D3 == "2":#Liður 2
                sjalfradaLeitari(bekkur)#Hérna kalla ég í fallið sjalfradaLeitari

            elif val_D3 == "3":#Liður 3
                print("Meðalaldur bekkjarins er:",medalaldurDict(bekkur))#Hérna kalla ég á fall sem reiknar meðalaldur dictionary-s(ef dictionary-ið er með aldur sem value)

            elif val_D3 == "4":#Liður 4
                print("Heildaraldur bekkjarins er:",heildaraldurDict(bekkur))#Hérna er fall sem reiknar heildaraldurinn í dictionary(ef dictionary-ið er með aldur sem value)

            elif val_D3 == "5":#Liður 5
                akvedin_stafur = leitaDict(bekkur)#Hérna seti ég return-ið úr fallinu leitaDict í breytuna akvedin_stafur til þess að geta unnið oftar en einu sinni með niðurstöðunna án þess að þurfa að kalla oft á sama fallið

                if len(akvedin_stafur) == 0:#Þetta er til þess að forritið chrash-i ekki ef það finnur engann
                    print("Það er enginn sem byrjar á þessum staf")

                else:#Hingað fer forritið ef það var eitthver fundinn
                    medalaldur = medalaldurDict(akvedin_stafur)#Hérna gat ég notað fall aftur sem ég bjó til áðan fyrir annan lið og seti útkamuna úr því falli í breytuna medalaldur

                    for nafn in akvedin_stafur:#Hérna prennta ég alla sem fundust
                        print(nafn,"---\t---\t---",akvedin_stafur[nafn])
                    print()

                    print("Meðalaldurinn í þessum hópi er:",medalaldur)#Hérna prennta ég meðalaldurinn á öllum sem fundust

            elif val_D3 == "6":#Þetta er til þess að það komi ekki ERROR þegar maður er að fara
                pass
            
            else:
                print("ERROR\tSláðu inn tölu á milli 1 og 6")

    elif valmynd == "4":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 4")
