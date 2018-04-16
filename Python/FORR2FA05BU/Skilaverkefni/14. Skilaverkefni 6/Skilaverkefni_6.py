'''
-----Verkefni-----
Hrólfur Gylfason
-----Dagsetning-----

Það er eitthver villa í þessu forriti sem gerir það að verkum að ef hermennirnir eru með jafn mikinn styrk festist forritið í
lúppu þar sem hermennirnir hafa alltaf sama styrk og forritið klárast aldrei
'''
import random

class Hermadur:#Þessi klasi er til þess að búa til tilvitnanirnar lif afl og vopn sem eru svo settar á lista svo að þá er hægt að kalla sérstaklega á hverja tilvitnun í listanum með því að nota .afl, .lif eða .vopn
    def __init__(self, lif, afl, vopn):
        self.lif = lif
        self.afl = afl
        self.vopn = vopn

class Berjast:#Þessi klasi er þar sem hermennirnir berjast og sjá hvor lifir af
    def __init__(self, a, b):#Þetta býr til breyturnar self.a og self.b
        self.a = a
        self.b = b

    def berjast(self):
        if herdeild_A[self.a].afl > herdeild_B[self.b].afl:#Þetta gerist ef hermaðurinn frá herdeild A hefur meiri styrk
            if herdeild_B[self.b].lif == 1:#Þetta gerist ef hermaðurinn sem er að fara að missa líf hefur bara eitt líf eftir og þá þarf að eyða honum af listanum vegna þess að þá er hann dáinn
                herdeild_B.pop(b)
                print("hermaður",self.b,"í herdeild B er dáinn")
            else:
                herdeild_B[self.b].lif = herdeild_B[self.b].lif - 1#Hérna er bara tekið eitt lí frá hermanninum ef hann hefur meira en eitt lí eftir og er ekki að fara að deyja
                print("hermaður",self.b,"í herdeild B er búinn að missa eitt líf og er núna með",herdeild_B[self.b].lif,"líf eftir")

        elif herdeild_A[self.a].afl < herdeild_B[self.b].afl:#Þetta gerist ef hermaðurinn frá herdeild B hefur meiri styrk
            if herdeild_A[self.a].lif == 1:#Þetta gerist ef hermaðurinn sem er að fara að missa líf hefur bara eitt líf eftir og þá þarf að eyða honum af listanum vegna þess að þá er hann dáinn
                herdeild_A.pop(a)#Þetta gerist ef hermaðurinn sem er að fara að missa líf hefur bara eitt líf eftir og þá þarf að eyða honum af listanum vegna þess að þá er hann dáinn
                print("hermaður",self.a,"í herdeild A er dáinn")
            else:
                herdeild_A[self.a].lif = herdeild_A[self.a].lif - 1#Hérna er bara tekið eitt lí frá hermanninum ef hann hefur meira en eitt lí eftir og er ekki að fara að deyja
                print("hermaður",self.a,"í herdeild A er búinn að missa eitt líf og er núna með",herdeild_A[self.a].lif,"líf eftir")

        elif herdeild_A[self.a].afl == herdeild_B[self.b].afl:#Þetta gerist ef báðir hafa jafn mikið afl, prentar út að ekkert gerist vegna þess að þeir eru jafn kraftmiklir
            print("Hermennirnir eru með jafn mikin styrk svo að það gerðist ekkert")
            
        else:
            print("ERROR\tvilla í bardaga tveggja hermanna")

herdeild_A = []
herdeild_B = []

for x in range(5):#Þetta býr til random gildi fyrir lif, afl og vopn, skilar því svo í klasan Hermadur og er sett á listann herdeild_A
    lif = random.randint(1,5)
    afl = random.randint(1,5)
    vopn = random.randint(1,3)#Sverð: 1, Spjót: 2, Exi: 3
    h1 = Hermadur(lif, afl, vopn)
    herdeild_A.append(h1)

for x in range(5):#Þetta býr til random gildi fyrir lif, afl og vopn, skilar því svo í klasan Hermadur og er sett á listann herdeild_B
    lif = random.randint(1,5)
    afl = random.randint(1,5)
    vopn = random.randint(1,3)#Sverð: 1, Spjót: 2, Exi: 3
    h1 = Hermadur(lif, afl, vopn)
    herdeild_B.append(h1)

while herdeild_A and herdeild_B:#Þessi while lúppa heldur áfram þangað til annað liðið er tómt
    print()
    a = random.randint(0,len(herdeild_A)-1)
    b = random.randint(0,len(herdeild_B)-1)

    h1 = Berjast(a, b)
    h1.berjast()


if not herdeild_A and herdeild_B:#Þetta gerist ef listinn herdeil_A er tómur og herdeild_B hefur enþá eitthvað á sér
    print("Herdeild B vann með",len(herdeild_B),"hermenn eftir")

elif not herdeild_B and herdeild_A:#Þetta gerist ef listinn herdeil_B er tómur og herdeild_A hefur enþá eitthvað á sér
    print("Herdeild A vann með",len(herdeild_A),"hermenn eftir")

else:
    print("ERROR\tEnginn vann")