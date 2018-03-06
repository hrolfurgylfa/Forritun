'''
Höfundur: Hrólfur Gylfason
Skilaverkefni 2 Liður 4
'''
#Hérna spyr ég notandan um kyn og nafn
nafn=input("Hvað heitirðu? ")
kyn=input("Hvort ertu karlkyns eða kvenkyns? kk/kvk? "). lower()
tala_1=int(input("Sláðu inn tölu eitt "))
tala_2=int(input("Sláðu inn tölu tvö "))
#Útreykningar
tala_1_100=tala_1+100
tala_2_100=tala_2+100
#Hérna finn ég út hvor talan er stærri og fyrir neðan það finn ég hvort munurinn
#á tölunum tveimur sé meiri eða minni en 100
if tala_1==tala_2:
    print("Tölurnar eru jafn stórar")
elif tala_1>tala_2:
    print("Tala eitt er stærri")
    if tala_1_100<tala_2:
        print("Mismunur talnana er meiri en 100")
    elif tala_2_100>tala_1:
        print("Mismunur talnana er minni en 100")
    elif tala_2_100==tala_1:
        print("Mismunur talnana er 100")
    else:
        print("ERROR")
elif tala_1<tala_2:
    print("Tala tvö er stærri")
    if tala_2_100<tala_1:
        print("Mismunur talnana er meiri en 100")
    elif tala_1_100>tala_2:
        print("Mismunur talnana er minni en 100")
    elif tala_1_100==tala_2:
        print("Mismunur talnana er 100")
    else:
        print("ERROR")
else:
    print("Error")
#Hérna heilsa ég notanda eftir kyni
if kyn=="kk":
    print("Blessaður",nafn)
elif kyn=="kvk":
    print("Blessuð",nafn)
else:
    print("Blessaður eða blessuð, ég veit ekki hvors kyns þú ert")
