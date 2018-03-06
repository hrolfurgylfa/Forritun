'''
Æfingarverkefni 1 Dictionaries
Hrólfur Gylfason
16/2/2018
'''
import random

#Dæmi 1 (Hannið dictionary sem innheldur 10 stök með númer sem key og liti value.)
ordabok = {1: "gulur",2: "rauður",3: "grænn",4: "blár",5: "svartur",6: "hvítur",7: "fjólublár",8: "brúnn",9: "bleikur",10: "appelsínugulur"}

#Dæmi 2 (Skrifið út dictionaryið í dæmi 1 þannig að hvert númer og litur er í einni línu.)
for x in ordabok:
    print(str(x)+" er "+str(ordabok[x]))

#Dæmi 3 (Skrifið út lit númer 4.)
print("Númer fjögur er: ",ordabok[4])

#Dæmi 4(Breyttu lit númer 5 í appelsínugult)
ordabok[5] = "appelsínugulur"

#Dæmi 5 (Skrifaðu út  breytt dictionary)
for x in ordabok:
    print(str(x)+" er "+str(ordabok[x]))

#Dæmi 6 (Fjarlægðu lit númer 2)
del ordabok[2]

#Dæmi 7 (Skrifaðu út  breytt dictionary)
for x in ordabok:
    print(str(x)+" er "+str(ordabok[x]))

#Dæmi 8 (Notaðu pop() aðferðina til að henda út random staki)
random_tala = random.randint(1,10)
while random_tala == 2:
    random_tala = random.randint(1,10)

ordabok.pop(random_tala)#Þetta eyðir valuinu hjá keyinum sem er talan inni í sviganum

#Dæmi 9 (Skrifaðu út breytt dictionary)
for x in ordabok:
    print(str(x)+" er "+str(ordabok[x]))

#Dæmi 10 (Gerðu afrit af dictionaryinu)
ordabok_rusl = ordabok.copy()

#Dæmi 11 (Eyddu öðru dictionaryinu)
ordabok_rusl.clear()

#Dæmi 12 (Reyndu að skrifa út dictionaryið sem þú eyddir. Hvaða melding kemur?)
halda_afram = input("Langar þér að forritið crashi (það er ekki búið að runna)? ja/nei ").lower()
if halda_afram == "ja":
    print(ordabok_rusl)
    print("LoL forritið crashaði ekki, úps")
elif halda_afram == "nei":
    pass
else:
    print("ERROR - þú ýttir á vitlausan takka, forritið mun halda áfram")

#Dæmi 13 (Búðu til nýtt dictionary með heiltölur sem key frá 1 til og með 5 og eitthvað annað sem values.)
ordabok_2 = {1: "Kind",2: "Kind Kind",3: "Kind Kind Kind",4: "Kind Kind Kind Kind",5: "Kind Kind Kind Kind Kind",}

#Dæmi 14 (Sýndu frá á notkun á eftirfarandi aðferðum tengdar dictionary.)

print(ordabok_2.items())

print(ordabok_2.keys())

print(ordabok_2.values())

ordabok_2.clear()
print(ordabok_2)
