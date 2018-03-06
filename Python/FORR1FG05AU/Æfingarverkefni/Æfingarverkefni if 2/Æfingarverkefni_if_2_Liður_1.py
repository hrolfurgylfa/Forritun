'''
Höfundur: Hrólfur Gylfason
Æfingarverkefni if 2 Liður 1
'''
#Hérna spyr ég notandann um nafn blaðasalans og hversu mörg blöð voru keypt og seld
nafn=input("Hvað heitir blaðasalinn? ")
blod_keypt=int(input("Hvað voru keypt mörg blöð? "))
blod_seld=int(input("Hvað voru seld mörg blöð? "))
#Útreykningar
blod_keypt_verd=blod_keypt*100
blod_seld_verd=blod_seld*300
#Hérna segi ég notandanum hvort hann hafi tapað pening, grææt pening, eða hafi ekki grætt né tapað
if blod_keypt_verd==blod_seld_verd:
    print("Þú stendur á núlli")
elif blod_keypt_verd>blod_seld_verd:
