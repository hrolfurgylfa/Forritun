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

def simaskra_leit(nafn,dict):
    afram = True
    for x in simaskra:
        if x == nafn:
            print("Símanúmer þessarar persónu er:",simaskra[x])
            return simaskra[x]#Þetta er ekki notað núna en þetta er ef ég vildi nota þetta í framtíðinni
            afram = False
            break

    if afram == True:
        print("Þetta nafn er ekki til í skránni")

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

    if valmynd == "1":#Liður 1
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

    elif valmynd == "2":#Liður 2
        simaskra = {"Magnús":8405385,"Kristján":8648096,"Stefán":6535365,"Jóhann":6805310,"Björn":6690398,"Elín":6037527,"Guðbjörg":6084992,"Ásta":7702612,"Katrín":7311023,"Ragnheiður":8784670}
        
        nafn = input("Sláðu inn nafn til þess að leita að í símaskránni: ")
        print()
        
        simaskra_leit(nafn,simaskra)

    elif valmynd == "3":#Liður 3
        pass

    elif valmynd == "4":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 4")
