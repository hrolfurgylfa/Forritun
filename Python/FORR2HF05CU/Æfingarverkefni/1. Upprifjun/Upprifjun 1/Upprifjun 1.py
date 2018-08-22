import random

#1
def fjoldi_orda(strengur):
    tel = 0

    for stafur in strengur:
        if stafur == " ":
            tel += 1
    
    tel += 1
    return tel

#2
def fyrstu_5(strengur):
    strengur = strengur[0:5]
    return strengur

#3
def sidustu_4(strengur):
    strengur = strengur[-4::]
    return strengur

#4
def midjustafurinn(strengur):
    if len(strengur) % 2 == 0:
        return "Strengurinn er slétt tala og það er þessvegna engin myðja"
    else:
        return strengur[len(strengur) // 2]

#5
def finna_s(strengur):
    nyi_strengur = ""

    for stafur in strengur:
        if stafur != "s" and stafur != "S" and stafur != " ":
            nyi_strengur += "$"
        else:
            nyi_strengur += stafur
    
    return nyi_strengur

#6
def buaTilListaMed100():
    listi = []

    for tel in range(100):
        listi.append(random.randint(34,68))

    return listi

#7
def radaLista(listi):
    listi.sort()
    return listi

#8
def medaltalLista(listi):
    return sum(listi) / len(listi)

#9
def minnstaOgStaersta(listi):
    print("Minnsta:",min(listi),"| Stærsta:",max(listi))

#10
def listiUndir4500(listi):
    while sum(listi) > 4500:
        listi = listi[:-1]
    return listi

#11
def eydaGangaUppiFimm(listi):
    ruslatunna = []

    for tala in listi:
        if tala % 5 == 0:
            ruslatunna.append(tala)
    
    for tala in ruslatunna:
        listi.remove(tala)

    return listi

#12
def setja40iSerLista(listi):
    fjortiuListi = []

    for tala in listi:
        if tala == 40:
            fjortiuListi.append(tala)
    
    return fjortiuListi


string = "Þetta er prufu strengur"
string2 = "Sjávar kássan klesstist í sjóarann"

print("Strengjarallý")

#1
print("1. ",fjoldi_orda(string))

#2
print("2. ",fyrstu_5(string))

#3
print("3. ",sidustu_4(string))

#4
print("4. ",midjustafurinn(string))

#5
print("5. ",finna_s(string2))

print("\nListarallý")

#6
random_listi = buaTilListaMed100()
print("6. ",random_listi)

#7
print("7. ",radaLista(random_listi))

#8
print("8. ",round(medaltalLista(random_listi),2))

#9
print("9. ",end="")
minnstaOgStaersta(random_listi)

#10
print("10. ",listiUndir4500(random_listi))

#11
print("11. ",eydaGangaUppiFimm(random_listi))

#12
print("12. ",setja40iSerLista(random_listi))