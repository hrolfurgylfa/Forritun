def geraSkraUrLista(skraarnafn,listi):
    skra = open(skraarnafn,"w")

    for hlutur in listi:
        skra.write(str(hlutur)+str(","))
    
    skra.close()

def veldi(haestaVeldi):
    listi = []

    for veldi in range(0,haestaVeldi+1):
        tala = pow(2,veldi)
        listi.append(tala)

    return listi

def skraILista(skraarnafn):
    skra = open(skraarnafn,"r")
    listi = []
    listi2 = []

    for line in skra:
        lina = line.split(",")
        for tala in lina:
            listi.append(tala)
    
    for tala in listi:
        if tala != "":
            listi2.append(tala)

    return listi2

def prentaLista10ILinu(listi):
    tel = 0

    for tala in listi:
        tel += 1

        if tel != 10:
            print(tala,end=" ")

        else:
            tel = 0
            print(tala)
    
    print()

def endaA6INyjanLista(listi):
    listi = list(map(str, listi))
    listi2 = []

    for tala in listi:
        if tala[-1] == "6":
            listi2.append(tala)

    return listi2

def eydaAfListaAfOdrum(listi,listi2):
    listi3 = []

    listi = list(map(str, listi))
    listi2 = list(map(str, listi2))

    for hlutur in listi:
        if hlutur not in listi2:
            listi3.append(hlutur)
    
    return listi3

def prentaLista(listi):
    tel = 0
    for hlutur in listi:
        if tel + 1 != len(listi):
            tel += 1
            print(hlutur,end=", ")
        
        else:
            print(hlutur)

def SkraIDict(skraarnafn):
    skra = open(skraarnafn,"r")
    dict1 = {}
    listi = []
    tel = 0

    for line in skra:
        lina = line.split(",")
        for tala in lina:
            listi.append(tala)
    
    for tala in listi:
        if tala != "":
            tel += 1
            dict1[tel] = tala

    return dict1

def prentaDict(tempDict):
    for key in tempDict:
        print(str(key)+", "+str(tempDict[key]))


skraarnafn = "Skra.txt"
skraarnafn2 = "Skra2.txt"

#Gera skránna
geraSkraUrLista(skraarnafn,veldi(20))

#A
print("1. \n",skraILista(skraarnafn))

#B
print("\n2. ")
prentaLista10ILinu(skraILista(skraarnafn))

#C
print("\n3.")
geraSkraUrLista(skraarnafn2,endaA6INyjanLista(veldi(20)))
geraSkraUrLista(skraarnafn,eydaAfListaAfOdrum(veldi(20),endaA6INyjanLista(veldi(20))))

#D
print("\n4.")
prentaLista(skraILista(skraarnafn))
prentaLista(skraILista(skraarnafn2))

#E
print("\n5.")
prentaDict(SkraIDict(skraarnafn))