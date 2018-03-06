'''
Höfundur: Hrólfur Gylfason
Skilaverkefni 2 Liður 2
'''
#Hérna spyr ég hvort notandinn vilji breyta tommum í sentimetra eða sentimetrum i tommur
print("Ef þú vilt breyta tommum í sentimetra ýttu á 1")
print("Ef þú vilt breyta sentimetrum í tommur ýttu á 2")
sentimetrar_tommur=input("--------------------------------------------------> ")
if sentimetrar_tommur==("1"):
    tommur=float(input("Hversu mörgum tommum langar þér að breyta í sentimetra? "))
    #Útreykningar fyrir tommur í sentimetra
    sentimetrar_reiknad=tommur*2.54
    print(tommur,"tommur eru",round(sentimetrar_reiknad,2),"sentimetrar")
elif sentimetrar_tommur==("2"):
    sentimetrar=float(input("Hversu mörgum sentimetrum langar þér að breyta í tommur? "))
    #Útreykningar fyrir sentimetra í tommur
    tommur_reiknad=sentimetrar/2.54
    print(sentimetrar,"sentimetrar eru",round(tommur_reiknad,2),"tommur")
else:
    print("ERROR [vitlaus tala]")
