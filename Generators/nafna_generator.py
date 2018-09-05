from random import shuffle

nofn = ["Jón","Sigurður","Guðmundur","Einar","Magnús","Kristján","Stefán","Jóhann","Björn","Árni","Bjarni","Helgi","Halldór","Pétur","Arnar","Kristinn","Gísli","Ragnar","Þorsteinn","Guðjón","Páll","Daníel","Sveinn","Birgir","Óskar","Davíð","Jóhannes","Karl","Guðrún","Anna","Sigríður","Kristín","Margrét","Helga","Sigrún","Ingibjörg","Jóhanna","María","Elín","Guðbjörg","Ásta","Katrín","Ragnheiður","Hildur","Erla","Guðný","Ólöf","Lilja","Hulda","Elísabet","Steinunn","Auður","Unnur","Inga","Eva","Þórunn","Sólveig","Þóra","Karl"]
shuffle(nofn)

hversu_oft = int(input("Sláðu inn hversu mörg nöfn þer vantar(max 60): "))
print()

if hversu_oft > 60:
    print("ERROR\tOf há tala")
else:
    for x in range(0,hversu_oft):
        print(nofn[x])