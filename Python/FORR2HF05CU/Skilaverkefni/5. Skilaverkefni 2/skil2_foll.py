from math import sqrt as rot#Þetta er til þess að reikna rót tölu
from math import pi#Þetta er til þess að finna pi
from time import sleep#Þetta er til þess að láta tölvuna bíða

def langhlid(a, b):#Þetta notar Pythagoras regluna til þess að finna út langhlið þríhirnings
    a_i_odru = int(a) ** 2
    b_i_odru = int(b) ** 2

    a_plus_b = a_i_odru + b_i_odru

    rot_a_plus_b = rot(a_plus_b)

    return rot_a_plus_b

def margfeldi_af(tala1, tala2):#Þetta skilar True ef að tala1 deilt með tölu 2 hefur engan afgang, annars skilar þetta False
    if tala1 % tala2 == 0:
        return True
    else:
        return False

def ferningur_ur_stjornum(staerd_kassa):#Þetta notar tvær for slaufur til þess að gera kassa, ein þeirra prentar út "staerd_kassa" margar stjörnur í línu svo kemur enter og þetta gerist aftur(jafn of og "staerd_kassa")

    for haed in range(staerd_kassa):
        for breidd in range(staerd_kassa):
            print("★",end="")
        print()

def er_slett_tala(tala1):#Þetta skilar True ef að tala1 deilt með tveimur hefur engan afgang, annars skilar þetta False
    if tala1 % 2 == 0:
        return True
    else:
        return False

def flatramal_hrings(radius):#Þetta reiknar út flatarmál hrings og skilar því svo
    flatarmal = pi * radius ** 2

    return flatarmal

def bank_bank(sekundur):#Þetta fall tekur inn breytuna sekundur og prentar út Bank á 0.2 sekuntna fresti þangaðtil það er liðinn jafn langur tími og kom inn með breytunni sekundur
    while sekundur > 0:#Þetta gerist þangað til sekundur er jafnt og eða lægra en 0
        print("Bank")
        sleep(.2)#Þetta bíður bara í 0.2 sekúndur
        sekundur -= .2#Þetta mínusar 0.2 sekúndur af breytunni sekundur
