'''
Hlutapróf 2
Hrólfur Gylfason
5/2/2018
'''
import random
def litaSkrifari(tup):
    tel = 1
    for litur in tup:
        print("Litur",tel,"er",litur)
        tel += 1

def litaStafaTeljari(tup):
    fleiri_en_sex = []
    for litur in tup:
        if len(litur) >= 6:
            fleiri_en_sex.append(litur)
    return fleiri_en_sex

def buaTilDict(tup):
    random_sex_tolur = []
    random_tala = random.randint(1,21)
    for tel in range(6):
        while random_tala in random_sex_tolur:
            random_tala = random.randint(1,21)
        random_sex_tolur.append(random_tala)
    dictionary = {random_sex_tolur[0]:tup[0],random_sex_tolur[1]:tup[1],random_sex_tolur[2]:tup[2],random_sex_tolur[3]:tup[3],random_sex_tolur[4]:tup[4],random_sex_tolur[5]:tup[5]}
    return dictionary

def stafaleit(dictionary,strengur):
    stafaleit_listi = []
    for stafur in strengur:
        if stafur in dictionary:
            stafaleit_listi.append(dictionary[stafur])
    return stafaleit_listi

def haerraNafn(nafn1,nafn2,dictionary):
    stafaleit_listi1 = []
    stafaleit_listi2 = []

    for stafur in nafn1:
        if stafur in dictionary:
            stafaleit_listi1.append(dictionary[stafur])
    
    for stafur in nafn2:
        if stafur in dictionary:
            stafaleit_listi2.append(dictionary[stafur])

    if len(stafaleit_listi1) > len(stafaleit_listi2):
        return nafn1

    elif len(stafaleit_listi1) > len(stafaleit_listi2):
        return nafn2

    else:
        return "hvorugt"

valmynd = ""

while valmynd != "3":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        litir = ("rauður","appelsínugulur","gulur","grænn","blár","fjólublár")

        litaSkrifari(litir)

        print()

        for litur in litaStafaTeljari(litir):
            print(litur,end=", ")
        print("\n")

        print(buaTilDict(litir))

    elif valmynd == "2":#Liður 2
        dictionary = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"x":22,"y":23,"z":24,"þ":25,"æ":26,"ö":27}

        nafn = input("Sláðu inn nafn: ").lower()
        stafaleit_listi = stafaleit(dictionary,nafn)
        for tala in stafaleit_listi:
            print(tala,end=" ")
        print("\n")

        print("Meðaltal talnanna er",round(sum(stafaleit_listi)/len(stafaleit_listi),1))
        print()

        nafn_1 = input("Sláðu inn nafn 1: ")
        nafn_2 = input("Sláðu inn nafn 2: ")

        print("Skilagildið er:",haerraNafn(nafn_1,nafn_2,dictionary),"vegna þess að þetta nafn er með hærri summu")

    elif valmynd == "3":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 3" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 3")
