'''
Höfundur Hrólfur
ifSetningar
'''
tala1=int(input("Sláðu inn tölu "))
tala2=int(input("Sláðu inn tölu "))
#einföld if setning
if tala1==tala2:
    print("tölurnar eru eins")
#if else setning
if tala1 >= tala2:
    print ("fyrri talan er stærri eða sama og seinni talan")
else:
    print ("fyrri talan er minni eða sama og seinni talan")
#if elif else setning
if tala1==tala2:
    print("tölurnar eru eins")
elif tala1>tala2 and (tala1==100 or tala1==150):
    print("fyrri talan er stærri en seinni talan og talan annað hvort 100 eða 150")
elif tala1<tala2:
    print("fyrri talan er minni en sú síðari")
else:
    print("talan þín er leiðinleg")
#hreiðraðar if uppsetningar
if tala1>tala2:
    print("fyrri talan er stærri en sú seinni ",end="")#skiptir ekki um línu
    #hreiðruð if setning
    if tala1<=100:
        print("en fyrri talan er samt minni eða sama og 100")
    else:
        print("en fyrri talan er samt stærri eða sama og 100")
else:
    ("þessar tölur eru lame :()")
