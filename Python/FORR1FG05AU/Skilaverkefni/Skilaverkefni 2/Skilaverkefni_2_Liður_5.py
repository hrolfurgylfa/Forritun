'''
Höfundur: Hrólfur Gylfason
Skilaverkefni 2 Liður 5
'''
#Hérna spyr ég notandann um tölu sem er 0 eða lægri eða 10 eða hælrri
tala=int(input("Sláðu inn tölu sem er lægri en núll eða hærri en tíu "))
#Héra segi ég notanda hvort hann hafi sett tölu rétta tölu
if tala>=0 and tala<=10:
    print("Þessi tala er ekki lægri en núll eða hærri en 10")
else:
    print("Vel gert! :)")
