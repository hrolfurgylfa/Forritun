'''
Höfundur: Hrólfur Gylfason
Skilaverkefni 2 Liður 1
'''
#Hérna spyr ég notandan um þrjár tölurnar
tala_1=int(input("Sláðu inn tölu 1 "))
tala_2=int(input("Sláðu inn tölu 2 "))
tala_3=int(input("Sláðu inn tölu 3 "))
#Hérna stoppa ég notandann ef hann er með tvær eða þrjár tölur eins
if tala_1==tala_2 or tala_1==tala_3 or tala_2==tala_3:
    print ("ERROR [engar tölur meiga vera eins]")
#Hérna finn ég út hvort tala eitt sé í myðjuni og ef hún er þá læt ég notandan vita
elif tala_1>tala_2 and tala_1<tala_3 or tala_1<tala_2 and tala_1>tala_3:
    print("Tala eitt er talan í miðjuni")
#Hérna finn ég út hvort tala tvö sé í myðjuni og ef hún er þá læt ég notandan vita
elif tala_2>tala_1 and tala_2<tala_3 or tala_2<tala_1 and tala_2>tala_3:
    print("Tala tvö er talan í miðjuni")
#Hérna finn ég út hvort tala þrjú sé í myðjuni og ef hún er þá læt ég notandan vita
elif tala_3>tala_2 and tala_3<tala_1 or tala_3<tala_2 and tala_3>tala_1:
    print("Tala þrjú er talan í miðjuni")
else:
    print("ERROR")
